#!/usr/bin/env python3
"""
Generiert pro Display-Verzeichnis unter docs/ ein kombiniertes PDF.

Konventionen:
- Jedes Unterverzeichnis von docs/ ist ein Display.
- Unterseiten (Dateien mit parent: <Kategorie> in der Front Matter)
  werden nach nav_order sortiert zusammengeführt.
- Der Titel stammt aus docs/<display>/index.md.
- Das PDF landet unter _site/assets/pdf/<slug>.pdf.

Zusätzlich bekommt jede Unterseite ein eigenes PDF unter
_site/assets/pdf/<slug>/<seitenname>.pdf — allerdings nur in den
Bereichen, die in _config.yml unter `pdf_single_pages` stehen.
So lässt sich eine einzelne Anleitung weitergeben, ohne den
ganzen Bereich mitzuschicken.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FEHLER: PyYAML fehlt – `pip install pyyaml`", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "_config.yml"
DOCS = ROOT / "docs"
SITE_PDF_DIR = ROOT / "_site" / "assets" / "pdf"
TMP_DIR = ROOT / "tmp" / "pdfgen"
TEMPLATE = ROOT / "scripts" / "pandoc" / "template.tex"
LOGO = ROOT / "assets" / "images" / "logo.png"

MONTHS_DE = {
    1: "Januar", 2: "Februar", 3: "März", 4: "April",
    5: "Mai", 6: "Juni", 7: "Juli", 8: "August",
    9: "September", 10: "Oktober", 11: "November", 12: "Dezember",
}


def parse_front_matter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, m.group(2)


def single_page_slugs() -> set[str]:
    """Bereiche, die zusätzlich Einzelseiten-PDFs bekommen.

    Steht in _config.yml, damit Skript und Jekyll-Layout dieselbe
    Liste lesen und die Bereichsnamen nicht doppelt gepflegt werden.
    """
    try:
        cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        print(f"WARNUNG: _config.yml nicht lesbar ({exc})", file=sys.stderr)
        return set()
    return set(cfg.get("pdf_single_pages") or [])


def split_heading(body: str) -> tuple[str | None, str]:
    """Trennt die erste H1 vom übrigen Text.

    Im Einzelseiten-PDF steht die Überschrift schon auf dem Deckblatt —
    im Fließtext wäre sie doppelt.
    """
    m = re.search(r"^#\s+(.+?)\s*$", body, flags=re.MULTILINE)
    if not m:
        return None, body
    return m.group(1), (body[: m.start()] + body[m.end():]).lstrip("\n")


def clean_markdown(body: str) -> str:
    """Entfernt kramdown-Spezifika, die pandoc nicht kennt."""
    # Liquid-Kommentare raus. Jekyll wertet die beim Bauen der Website aus,
    # pandoc liest die Markdown-Quelle aber direkt — ohne diesen Schritt
    # landen interne Notizen im PDF. Muss als Erstes laufen, damit der
    # Inhalt der Kommentare die folgenden Regeln nicht durcheinanderbringt.
    body = re.sub(
        r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}[ \t]*\n?",
        "",
        body,
        flags=re.DOTALL,
    )
    # Kompletten Inhaltsblock (Überschrift + Attribut + TOC-Platzhalter) raus
    body = re.sub(
        r"^##\s+Inhalt\s*\n\{:\s*\.no_toc[^\}]*\}\s*\n\s*\n-\s*TOC\s*\n\{:toc\}\s*\n?",
        "",
        body,
        flags=re.MULTILINE,
    )
    # kramdown max-width auf Bildern → pandoc width-Attribut
    def convert_image_width(m: re.Match) -> str:
        img = m.group(1)
        width_match = re.search(r'max-width:\s*(\d+)%', m.group(2))
        if width_match:
            return f"{img}{{ width={width_match.group(1)}% }}"
        return img
    body = re.sub(
        r'(!\[[^\]]*\]\([^)]+\))\{:\s*([^\}]*)\}',
        convert_image_width,
        body,
    )
    # Blockquote mit {: .warnung } → orange Warn-Box (siehe template.tex).
    # Muss vor dem generischen Entfernen der kramdown-Attribute laufen.
    def convert_warnung(m: re.Match) -> str:
        inner = re.sub(r"^>[ \t]?", "", m.group(1), flags=re.MULTILINE).strip()
        return (
            "```{=latex}\n\\begin{warnbox}\n```\n\n"
            f"{inner}\n\n"
            "```{=latex}\n\\end{warnbox}\n```\n"
        )
    body = re.sub(
        r"^((?:>.*(?:\n|$))+)\{:\s*\.warnung\s*\}[ \t]*(?:\n|$)",
        convert_warnung,
        body,
        flags=re.MULTILINE,
    )
    # Verbleibende inline kramdown-Attribute entfernen
    body = re.sub(r"\{:\s*[^\}]*\}", "", body)
    # Eingerückte Bilder (in Listen) als eigene Absätze herausziehen
    body = re.sub(r"^[ \t]+(!\[[^\]]*\]\([^)]+\)(?:\{[^}]*\})?)\s*$", r"\n\1\n", body, flags=re.MULTILINE)
    # Übriggebliebenes {:toc}
    body = re.sub(r"^\{:toc\}\s*$\n?", "", body, flags=re.MULTILINE)
    # Führende horizontale Linie nach Einleitung ist in der PDF überflüssig
    body = re.sub(r"^---\s*$\n", "", body, flags=re.MULTILINE, count=1)
    return body.strip() + "\n"


def collect_pages(display_dir: Path) -> list[tuple[int, dict, str, str]]:
    pages: list[tuple[int, dict, str, str]] = []
    for md in display_dir.glob("*.md"):
        if md.name == "index.md":
            continue
        meta, body = parse_front_matter(md.read_text(encoding="utf-8"))
        if not meta.get("parent"):
            continue
        pages.append((int(meta.get("nav_order", 999)), meta, clean_markdown(body), md.stem))
    pages.sort(key=lambda p: p[0])
    return pages


def display_metadata(display_dir: Path) -> dict:
    index = display_dir / "index.md"
    if not index.exists():
        return {"title": display_dir.name.replace("-", " ").title()}
    meta, _ = parse_front_matter(index.read_text(encoding="utf-8"))
    return meta


def build_combined_markdown(display_dir: Path, pages: list) -> Path:
    slug = display_dir.name

    chunks: list[str] = []
    warnbox_seen = False
    for i, (_, _, body, _) in enumerate(pages):
        # Der Warnhinweis steht auf jeder Web-Seite, im zusammengefassten
        # PDF reicht er einmal ganz vorne.
        if "\\begin{warnbox}" in body:
            if warnbox_seen:
                body = re.sub(
                    r"```\{=latex\}\n\\begin\{warnbox\}\n```\n\n"
                    r".*?"
                    r"```\{=latex\}\n\\end\{warnbox\}\n```\n+",
                    "",
                    body,
                    flags=re.DOTALL,
                )
            warnbox_seen = True
        if i > 0:
            chunks.append("\n\n```{=latex}\n\\clearpage\n```\n\n")
        chunks.append(body)

    TMP_DIR.mkdir(parents=True, exist_ok=True)
    combined = TMP_DIR / f"{slug}.md"
    combined.write_text("\n".join(chunks), encoding="utf-8")
    return combined


def format_date_german() -> str:
    today = date.today()
    return f"{MONTHS_DE[today.month]} {today.year}"


def run_pandoc(
    source_md: Path,
    output: Path,
    title: str,
    subtitle: str,
    source_dir: Path,
    extra_args: tuple[str, ...] = (),
) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(source_md),
        "-o", str(output),
        "--pdf-engine=xelatex",
        "--template", str(TEMPLATE),
        "--resource-path", str(source_dir),
        "--toc",
        "--toc-depth=2",
        "--highlight-style=monochrome",
        "--from", "markdown+raw_tex+pipe_tables+backtick_code_blocks+fenced_code_attributes",
        "-V", f"title={title}",
        "-V", f"subtitle={subtitle}",
        "-V", f"date={format_date_german()}",
        "-V", f"logo={LOGO}",
        "-V", "lang=de-DE",
        "-V", "documentclass=article",
        "-V", "fontsize=11pt",
        "-V", "papersize=a4",
        *extra_args,
    ]
    print(f"  pandoc → {output.relative_to(ROOT)}", flush=True)
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(f"pandoc fehlgeschlagen für {output.name}")
    return output


def build_single_page_pdfs(display_dir: Path, pages: list, bereich: str) -> list[Path]:
    """Ein eigenständiges PDF pro Unterseite.

    Die Überschriften rücken über --shift-heading-level-by eine Ebene
    hoch: Was im Bereichs-PDF ein Unterkapitel ist, wird hier zum
    Kapitel — die Seite liest sich dann als eigene Anleitung.
    """
    slug = display_dir.name
    out_dir = SITE_PDF_DIR / slug
    generated: list[Path] = []
    for _, meta, body, stem in pages:
        heading, rest = split_heading(body)
        title = heading or meta.get("title", stem)
        # Eine zweite H1 würde beim Hochrücken zur Ebene 0 und damit von
        # pandoc still verschluckt. Kommt in den Anleitungen nicht vor,
        # soll aber auffallen, falls doch mal eine hineinrutscht.
        if re.search(r"^#\s+", rest, flags=re.MULTILINE):
            print(f"  WARNUNG: {stem}.md hat mehr als eine H1", file=sys.stderr)
        single = TMP_DIR / f"{slug}--{stem}.md"
        single.write_text(rest, encoding="utf-8")
        generated.append(
            run_pandoc(
                single,
                out_dir / f"{stem}.pdf",
                title,
                bereich,
                display_dir,
                extra_args=("--shift-heading-level-by=-1",),
            )
        )
    return generated


def main() -> int:
    if not TEMPLATE.exists():
        print(f"FEHLER: Template fehlt: {TEMPLATE}", file=sys.stderr)
        return 1
    if shutil.which("pandoc") is None:
        print("FEHLER: pandoc nicht installiert", file=sys.stderr)
        return 1
    if shutil.which("xelatex") is None:
        print("FEHLER: xelatex nicht installiert", file=sys.stderr)
        return 1

    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR)
    TMP_DIR.mkdir(parents=True)

    single_slugs = single_page_slugs()

    generated: list[Path] = []
    for display_dir in sorted(DOCS.iterdir()):
        if not display_dir.is_dir():
            continue
        slug = display_dir.name
        print(f"[{slug}]")
        pages = collect_pages(display_dir)
        if not pages:
            print("  übersprungen (keine Unterseiten)")
            continue
        bereich = display_metadata(display_dir).get("title", slug)
        combined = build_combined_markdown(display_dir, pages)
        generated.append(
            run_pandoc(combined, SITE_PDF_DIR / f"{slug}.pdf", bereich, "Anleitung", display_dir)
        )
        if slug in single_slugs:
            generated.extend(build_single_page_pdfs(display_dir, pages, bereich))

    if not generated:
        print("Keine PDFs erzeugt.")
        return 0
    print(f"\nFertig: {len(generated)} PDF(s) unter {SITE_PDF_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
