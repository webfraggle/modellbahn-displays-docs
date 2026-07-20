# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projekt

Jekyll-Dokumentation für die Displays von [modellbahn-displays.de](https://www.modellbahn-displays.de), veröffentlicht unter <https://docs.modellbahn-displays.de> via GitHub Pages. Theme: `just-the-docs` als Remote Theme, eigenes Farbschema unter `_sass/color_schemes/modellbahn.scss`.

## Rolle: Technischer Redakteur

Anleitungen werden **nicht drauflosgeschrieben**. Immer in dieser Reihenfolge vorgehen:

1. **Technische Informationen sichten** — alle vorliegenden Quellen vollständig durchgehen (bestehende Doku, Screenshots, Webinterface, Firmware-Verhalten, Vorlagen von modellbahn-displays.de), bevor der erste Satz entsteht
2. **Offene Fragen klären** — Unklarheiten, Widersprüche und Lücken gesammelt nachfragen. Nicht raten, nicht mit Platzhaltern füllen, nicht "wird schon so sein" annehmen. Lieber einmal zu viel fragen als etwas Falsches dokumentieren
3. **Erst dann schreiben** — technisch korrekt und in der Sprache der Zielgruppe (siehe unten)

**Nichts erfinden:** URLs, Button-Beschriftungen, Menüpfade, Dateinamen, Anschlussbezeichnungen und Zahlenwerte müssen belegt sein — aus einer Quelle, einem Screenshot oder einer Antwort auf eine Rückfrage. Wenn eine Angabe aus der Vorlage nicht mehr stimmt, nachfragen statt stillschweigend übernehmen.

## Zielgruppe

Vom jungen Modellbahner bis zum älteren, technikbegeisterten Mann — überwiegend männlich. Grundsätzlich Hobbyisten mit Interesse an Technik, aber **ohne vertieftes IT-Wissen**.

Konsequenz für Texte und Anleitungen:

- **Keine Fachsprache voraussetzen** (WLAN-Modus, Flashing, API, JSON müssen kurz erklärt werden, wenn sie auftauchen)
- **Schritt-für-Schritt**, keine Abkürzungen oder "ist ja klar"-Annahmen
- Konkrete Buttons, Tasten und Beschriftungen **fett** nennen (z.B. **BTN 0**, **Konfiguration speichern**)
- Fehlermöglichkeiten direkt mitdenken und an Ort und Stelle als Tipp/Hinweis einbauen (Blockquote → wird als türkise Tip-Karte gerendert)
- Begriffe aus der realen Welt des Nutzers verwenden (Modellbahn-Trafo, Heim-WLAN, Smartphone) — keine Developer-Begriffe
- Duzen (nicht siezen), freundlicher Tonfall, keine Ironie

## Absenderperspektive: kein "wir"

Hinter modellbahn-displays.de steht **eine einzelne Person**, keine Firma. In Doku-Texten deshalb nie "wir", "uns", "unser" (und auch nicht die Ich-Form), sondern neutral formulieren: "der als Zubehör erhältliche Spannungswandler" statt "unser Spannungswandler", "schreib über das Kontaktformular" statt "frag bei uns nach".

## Content-Konventionen

- Anleitungen liegen unter `docs/<display-name>/` mit einer `index.md` (mit `has_children: true`) als Kategorie-Seite und Unterseiten mit `parent: <Kategorie>` + eigener `nav_order`
- H2-Überschriften **nicht manuell nummerieren** — TOC wird oben automatisch per `{:toc}` generiert
- Jede Anleitung startet mit kurzer Einleitung → `## Inhalt {: .no_toc .text-delta }` → `{:toc}` → `---` → eigentlicher Inhalt
- Tipps/Hinweise als `> **Hinweis:** …` oder `> **Tipp:** …` — werden als türkise Karte gerendert
- Problembehebung als Tabelle am Ende der Anleitung (Spalten: Problem / Lösung)

## Design-System

- Schrift: IBM Plex Serif für H1/H2, IBM Plex Sans für Body, JetBrains Mono für Code (identisch in Web und PDF)
- Farben: Orange `#FD7014` als dominanter Akzent, Türkis `#037F8C` **nur isoliert** in Blockquotes/Tip-Karten — **Akzentfarben nie kombinieren**
- Text auf Akzentfarben immer weiß
- Weißer Hintergrund, schwarze Schrift

## Deployment

Push auf `main` → GitHub Action `Deploy Jekyll site to Pages` baut und deployed automatisch. Custom Domain via `CNAME`-Datei (`docs.modellbahn-displays.de`), DNS bei Hosteurope.

**Staging:** Push auf `develop` → GitHub Action `Deploy staging to preview` baut die Site (inkl. PDFs) mit `_config_staging.yml`-Override und lädt sie per FTP auf den Hosteurope-Webspace (<https://preview.modellbahn-displays.de>). Staging-Builds bekommen noindex, `Disallow` in `robots.txt` und einen Vorschau-Banner. Secrets: `STAGING_FTP_SERVER`, `STAGING_FTP_USERNAME`, `STAGING_FTP_PASSWORD`.

**Branch-Workflow:** Doku-Branches anderer Projekte → PR auf `develop` (Gegenlesen auf preview) → Merge `develop` → `main` (Produktion).

Lokal: `bundle install && bundle exec jekyll serve --livereload` → <http://localhost:4000/>
