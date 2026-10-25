# Review-Status der Anleitungen

Diese Datei hält fest, welche Seiten fachlich gegengelesen und freigegeben sind.
Sie ist kein Teil der veröffentlichten Site (in `_config.yml` unter `exclude`).

**Status-Werte:**

- `offen` — noch nicht gegengelesen
- `in Arbeit` — wird gerade geprüft
- `Änderung nötig` — geprüft, aber es fehlt oder stimmt noch etwas (siehe Notizen)
- `freigegeben` — inhaltlich geprüft und korrekt

Datum im Format `JJJJ-MM-TT`, bezogen auf die Freigabe bzw. die letzte Prüfung.

---

## Start

| Seite | Titel | Status | Datum | Notizen |
|---|---|---|---|---|
| `index.md` | Startseite | freigegeben | 2026-08-08 | |

## Allgemein

| Seite | Titel | Status | Datum | Notizen |
|---|---|---|---|---|
| `docs/allgemein/index.md` | Allgemein | offen | — | 2026-09-26: Link auf Hintergrundbeleuchtung ergänzt |
| `docs/allgemein/flachbandkabel-anschliessen.md` | Flachbandkabel anschließen | freigegeben | 2026-08-08 | |
| `docs/allgemein/wlan-einrichten.md` | WLAN einrichten | freigegeben | 2026-10-25 | Aufteilung ab 3.2 / bis 3.1 gegengelesen. Danach beim Gegenlesen ergänzt: BTN-0-Hinweis bei Name/Passwort, Tipp „Rückmeldung erscheint nicht immer → LED grün + BTN 0“ |
| `docs/allgemein/controller-aktualisieren-wlan.md` | Controller aktualisieren (über WLAN) | offen | — | |
| `docs/allgemein/controller-aktualisieren-usb.md` | Controller aktualisieren (per USB) | offen | — | |
| `docs/allgemein/hintergrundbeleuchtung.md` | Hintergrundbeleuchtung | freigegeben | 2026-10-25 | Ab 3.2 BTN 0 lang, bis 3.1 BTN 3 |

## Bildgeneratoren

| Seite | Titel | Status | Datum | Notizen |
|---|---|---|---|---|
| `docs/bildgeneratoren/index.md` | Bildgeneratoren | freigegeben | 2026-08-08 | |
| `docs/bildgeneratoren/wetter.md` | Wetter | freigegeben | 2026-08-08 | |
| `docs/bildgeneratoren/markt.md` | Markt | freigegeben | 2026-08-08 | |

## Tankstellenanzeige

| Seite | Titel | Status | Datum | Notizen |
|---|---|---|---|---|
| `docs/tankstellenanzeige/index.md` | Tankstellenanzeige | freigegeben | 2026-08-08 | |
| `docs/tankstellenanzeige/anleitung.md` | Einrichtung & Bedienung | freigegeben | 2026-08-08 | 2026-09-13: Spannungswandler-Angaben ergänzt (DC 8–27 V / AC 8–19 V) — nachgezogen aus dem ZZA-Kapitel |
| `docs/tankstellenanzeige/anzeige-reihenfolge.md` | Weitere Inhalte anzeigen | freigegeben | 2026-08-08 | |
| `docs/tankstellenanzeige/api.md` | Eigene API-URL | freigegeben | 2026-08-08 | |
| `docs/tankstellenanzeige/backup-restore.md` | Backup & Wiederherstellung | freigegeben | 2026-08-08 | |

## Video-Display

| Seite | Titel | Status | Datum | Notizen |
|---|---|---|---|---|
| `docs/video-display/index.md` | Video-Display | offen | — | |
| `docs/video-display/inbetriebnahme.md` | Video-Controller in Betrieb nehmen | offen | — | 2026-09-13: Spannungswandler-Angaben ergänzt (DC 8–27 V / AC 8–19 V) |
| `docs/video-display/medien-verwalten.md` | Medien verwalten | offen | — | |
| `docs/video-display/videos-konvertieren.md` | Videos konvertieren | offen | — | |
| `docs/video-display/datenformate.md` | Datenformate und eigene Dateien | offen | — | |

## Zugzielanzeiger

Zum Abhaken beim Gegenlesen, in der Reihenfolge der Navigation.

- [x] **Zugzielanzeiger** (Kapitelübersicht) — `index.md`
      · gegengelesen 2026-09-20 · neu gefasste Einleitung bestätigt · Frage 03 beantwortet, keine offenen Fragen mehr
- [x] **Zugzielanzeiger in Betrieb nehmen** — `inbetriebnahme.md`
      · gegengelesen 2026-10-25 · Änderungen 3.2 (Info-Anzeige 60 s, BTN 0) und vom 2026-09-26 bestätigt
      · 2026-09-26 geändert: „Danebengedrückt?“ um BTN 3 lang drücken (ab 3.1.10) ergänzt, Link auf `allgemein/hintergrundbeleuchtung.md`, Hinweis zum Ausprobieren bei dunklem Display
      · gegengelesen 2026-09-13 · Frage 11 eingearbeitet (Spannungen ergaenzt!) · offen 03, 19
- [x] **Züge anlegen und anzeigen** — `zuege-verwalten.md`
      · gegengelesen 2026-09-13 · offen bleiben Fragen 02, 27
- [ ] **Anzeigeart und Einstellungen** — `anzeigearten.md`
      · **2026-10-25 geändert, neu gegenlesen:** Tabelle um Client: Bild / Client: Züge ergänzt, Überschrift „Die fünf Anzeigearten“ → „Die Anzeigearten“
      · gegengelesen 2026-09-13 · Fragen 04 und 06 eingearbeitet, offen bleiben 18, 24
- [x] **Wagenreihung darstellen** — `wagenreihung.md`
      · gegengelesen 2026-09-20 · Einleitung um Hinweis-Codierung ergänzt, Strg/Cmd+C und +V bei **Kopieren** nachgetragen
      · Befund: Knopf **Kopieren** ist defekt (Befund 12 in `70-befunde-firmware-ui.md`) · keine offenen Fragen mehr
- [x] **Echte Fahrplandaten anzeigen** — `live-daten.md`
      · gegengelesen 2026-09-20 · Bahnhofsnummern und Serverhinweis eingearbeitet · keine offenen Fragen mehr
- [x] **Bilder statt Züge anzeigen** — `bilder-anzeigen.md`
      · gegengelesen 2026-09-20 · Abschnitt „Bilder aus dem Web" in zwei Wege getrennt (Standbild herunterladen vs. Image-URL)
      · Anzeigeart-Bedingung für die Image-URL ergänzt (nur Manuell/Intervall/Live, nicht in den Bild-Modi) · keine offenen Fragen mehr
- [x] **Über die Modellbahnzentrale steuern (DCC)** — `dcc-steuern.md`
      · gegengelesen 2026-09-20 · sieben Fotos von der alten Website ergänzt (Reihenschaltung, mobile-station-Keyboard und Fahrpult,
        neuer Abschnitt „Beispiel: die virtuelle Lok in der Märklin mobile station")
      · offen bleibt Frage 15 (Hinweis zu F0 auf Gleis A fliegt nach dem Firmware-Fix raus)
- [x] **Anbindung an TrainController, iTrain und Rocrail** — `steuerungsprogramme.md`
      · gegengelesen 2026-09-20 · Frage 10 vollständig erledigt: PDF von Andri Müller wieder verlinkt, mit Warnkarte zum Namenswechsel
        (`mbd-tc.exe`/`mbd-tc-hidden.exe` → `mbd-cli.exe`, Flags unverändert, `-hidden` fällt ersatzlos weg)
      · drei TrainController-Screenshots von der alten Website ergänzt · keine offenen Fragen mehr
- [x] **Fernsteuerung über MQTT** — `mqtt.md`
      · gegengelesen 2026-09-20 · Frage 20 entschieden: dokumentieren ja, aber Beta-Warnkarte oben auf der Seite
      · neuer Abschnitt „Win-Digipet" (Anlass für die MQTT-Anbindung, noch ungetestet) · offen: eigener oder externer Broker bei Win-Digipet
- [x] **Zugdaten sichern und wiederherstellen** — `backup.md`
      · gegengelesen 2026-09-20 · Abschnitt zu Konfiguration und Bildern ergänzt · keine offenen Fragen mehr
- [x] **Zwei Anzeiger gleich schalten (Client-Modus)** — `client-modus.md`
      · gegengelesen 2026-10-25 · Tipp umgedreht (zuerst Client: Bild), Vorder-/Rückseite präzisiert, Gleis/Abschnitt/Folgezüge-Pflicht gestrichen (Züge kommen vollständig vom Master) · offen bleiben 28, 30, 31, 32
      · **2026-10-25 neu** (Firmware 3.2.11): Screenshots an QUAD .107 (Master) und DUAL .97 (Client) · offen 28–32

**Stand: 11 von 12 gegengelesen — offen: `anzeigearten.md` (Tabelle um Client-Arten ergänzt, 2026-10-25).**

> Die nummerierten Fragen stehen in `ZZA-RECHERCHE/50-offene-fragen.md`.
> Im Text sind sie als `{% raw %}{% comment %} OFFEN-NN: … {% endcomment %}{% endraw %}` markiert
> und mit `grep -rn "OFFEN-" docs/zugzielanzeiger/` auffindbar.
> Ein Haken heißt: Text ist gelesen und in Ordnung. Die dort genannten offenen Fragen
> können trotzdem noch Änderungen an der Seite nach sich ziehen.
