#!/usr/bin/env python3
"""
Generiert pro Display-Verzeichnis unter docs/ ein kombiniertes PDF.

Konventionen:
- Jedes Unterverzeichnis von docs/ ist ein Display.
- Unterseiten (Dateien mit parent: <Kategorie> in der Front Matter)
  werden nach nav_order sortiert zusammengeführt.
- Der Titel stammt aus docs/<display>/index.md.
- Das PDF landet unter _site/assets/pdf/<slug>.pdf.
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


def collect_pages(display_dir: Path) -> list[tuple[int, dict, str]]:
    pages: list[tuple[int, dict, str]] = []
    for md in display_dir.glob("*.md"):
        if md.name == "index.md":
            continue
        meta, body = parse_front_matter(md.read_text(encoding="utf-8"))
        if not meta.get("parent"):
            continue
        pages.append((int(meta.get("nav_order", 999)), meta, clean_markdown(body)))
    pages.sort(key=lambda p: p[0])
    return pages


def display_metadata(display_dir: Path) -> dict:
    index = display_dir / "index.md"
    if not index.exists():
        return {"title": display_dir.name.replace("-", " ").title()}
    meta, _ = parse_front_matter(index.read_text(encoding="utf-8"))
    return meta


def build_combined_markdown(display_dir: Path) -> tuple[Path, str, str, Path] | None:
    pages = collect_pages(display_dir)
    if not pages:
        return None

    slug = display_dir.name
    meta = display_metadata(display_dir)
    title = meta.get("title", slug)

    chunks: list[str] = []
    warnbox_seen = False
    for i, (_, _, body) in enumerate(pages):
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
    return combined, title, slug, display_dir


def format_date_german() -> str:
    today = date.today()
    return f"{MONTHS_DE[today.month]} {today.year}"


def run_pandoc(combined_md: Path, title: str, slug: str, source_dir: Path) -> Path:
    SITE_PDF_DIR.mkdir(parents=True, exist_ok=True)
    output = SITE_PDF_DIR / f"{slug}.pdf"

    cmd = [
        "pandoc",
        str(combined_md),
        "-o", str(output),
        "--pdf-engine=xelatex",
        "--template", str(TEMPLATE),
        "--resource-path", str(source_dir),
        "--toc",
        "--toc-depth=2",
        "--highlight-style=monochrome",
        "--from", "markdown+raw_tex+pipe_tables+backtick_code_blocks+fenced_code_attributes",
        "-V", f"title={title}",
        "-V", "subtitle=Anleitung",
        "-V", f"date={format_date_german()}",
        "-V", f"logo={LOGO}",
        "-V", "lang=de-DE",
        "-V", "documentclass=article",
        "-V", "fontsize=11pt",
        "-V", "papersize=a4",
    ]
    print(f"  pandoc → {output.relative_to(ROOT)}", flush=True)
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(f"pandoc fehlgeschlagen für {slug}")
    return output


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

    generated: list[Path] = []
    for display_dir in sorted(DOCS.iterdir()):
        if not display_dir.is_dir():
            continue
        print(f"[{display_dir.name}]")
        result = build_combined_markdown(display_dir)
        if result is None:
            print("  übersprungen (keine Unterseiten)")
            continue
        combined, title, slug, source_dir = result
        pdf = run_pandoc(combined, title, slug, source_dir)
        generated.append(pdf)

    if not generated:
        print("Keine PDFs erzeugt.")
        return 0
    print(f"\nFertig: {len(generated)} PDF(s) unter {SITE_PDF_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
