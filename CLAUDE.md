# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projekt

Jekyll-Dokumentation für die Displays von [modellbahn-displays.de](https://www.modellbahn-displays.de), veröffentlicht unter <https://docs.modellbahn-displays.de> via GitHub Pages. Theme: `just-the-docs` als Remote Theme, eigenes Farbschema unter `_sass/color_schemes/modellbahn.scss`.

## Zielgruppe

Vom jungen Modellbahner bis zum älteren, technikbegeisterten Mann — überwiegend männlich. Grundsätzlich Hobbyisten mit Interesse an Technik, aber **ohne vertieftes IT-Wissen**.

Konsequenz für Texte und Anleitungen:

- **Keine Fachsprache voraussetzen** (WLAN-Modus, Flashing, API, JSON müssen kurz erklärt werden, wenn sie auftauchen)
- **Schritt-für-Schritt**, keine Abkürzungen oder "ist ja klar"-Annahmen
- Konkrete Buttons, Tasten und Beschriftungen **fett** nennen (z.B. **BTN 0**, **Konfiguration speichern**)
- Fehlermöglichkeiten direkt mitdenken und an Ort und Stelle als Tipp/Hinweis einbauen (Blockquote → wird als türkise Tip-Karte gerendert)
- Begriffe aus der realen Welt des Nutzers verwenden (Modellbahn-Trafo, Heim-WLAN, Smartphone) — keine Developer-Begriffe
- Duzen (nicht siezen), freundlicher Tonfall, keine Ironie

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

Lokal: `bundle install && bundle exec jekyll serve --livereload` → <http://localhost:4000/>
