# Modellbahn Displays – Anleitungen

Dokumentation zu den Displays von [modellbahn-displays.de](https://www.modellbahn-displays.de), gebaut mit [Jekyll](https://jekyllrb.com/) und dem Theme [just-the-docs](https://just-the-docs.com/), veröffentlicht via GitHub Pages.

## Lokal entwickeln

Voraussetzung: Ruby 3.2+ und Bundler.

```sh
bundle install
bundle exec jekyll serve --livereload
```

Die Seite ist dann unter <http://localhost:4000/> erreichbar.

Live unter: <https://docs.modellbahn-displays.de>

## Struktur

```
.
├── _config.yml                  # Jekyll-Konfiguration
├── _sass/color_schemes/         # Eigenes Farbschema (CI)
├── assets/images/               # Logo und Bilder
├── docs/                        # Anleitungen (eine Unterseite pro Display)
│   └── tankstellenanzeige/
│       ├── index.md             # Kategorie-Übersicht
│       ├── anleitung.md
│       └── api.md
├── index.md                     # Startseite
└── .github/workflows/pages.yml  # Deploy nach GitHub Pages
```

## Neue Anleitung hinzufügen

1. Neues Verzeichnis unter `docs/` anlegen (z.B. `docs/bahnhofsanzeige/`).
2. `index.md` mit Front Matter anlegen (`has_children: true`, eigene `nav_order`).
3. Unterseiten mit `parent: <Kategorie>` und eigener `nav_order` hinzufügen.
4. Auf der Startseite (`index.md`) in die Liste eintragen.
