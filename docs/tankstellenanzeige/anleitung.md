---
title: Einrichtung & Bedienung
layout: anleitung
parent: Tankstellenanzeige
nav_order: 1
---

# Tankstellenanzeige — Anleitung

Diese Anleitung beschreibt die Ersteinrichtung und Konfiguration der Tankstellenanzeige.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Anschluss und erster Start

Prüfe, dass das Flachbandkabel zwischen Controller und Display richtig eingesteckt ist (siehe [Flachbandkabel anschließen](../allgemein/flachbandkabel-anschliessen.md)). Verbinde den Controller per USB-C-Kabel mit einer Stromquelle (USB-Netzteil, Modellbahn-Trafo mit USB-Ausgang oder Powerbank). Nach wenigen Sekunden erscheint das Boot-Logo auf dem Display und die LED am Controller leuchtet.

---

## WLAN einrichten und IP-Adresse herausfinden

Die WLAN-Einrichtung ist bei allen Displays gleich. Die vollständige Anleitung findest du unter [WLAN einrichten](../allgemein/wlan-einrichten.md).

---

## Webinterface

Auf der Startseite findest du drei Bereiche:

- **Konfiguration** — Preise, Template und Einstellungen
- **WLAN-Konfiguration** — WLAN-Zugangsdaten ändern
- **Controller-Upgrade** — Firmware aktualisieren

Klicke auf **Konfiguration**, um zu den Einstellungen zu gelangen.

---

## Template wählen

Unter **Template** findest du eine Liste aller verfügbaren Anzeige-Designs (z.B. Aral, Shell, LED). Wähle das Template, das zu deiner Tankstelle passt.

---

## Tankstellen-ID eingeben

Wenn du Live-Preise für eine bestimmte Tankstelle anzeigen möchtest, musst du die Tankstellen-ID eingeben. So findest du die ID:

1. Klicke im Webinterface auf den Link **ID finden** unterhalb des Eingabefeldes (oder öffne [https://creativecommons.tankerkoenig.de/TankstellenFinder/index.html](https://creativecommons.tankerkoenig.de/TankstellenFinder/index.html)).
2. Schiebe auf der Karte den blauen Marker in den Bereich deiner Tankstelle.
3. Klicke die gewünschte Tankstelle an.
4. Klicke auf **Tankstelle übernehmen** — jetzt wird die ID angezeigt.
5. Markiere die ID (langer Text aus Buchstaben, Zahlen und Bindestrichen) und kopiere sie.
6. Wechsle zurück zum Webinterface und füge die ID in das Feld **Tankstellen-ID** ein.

> **Hinweis:** Wird die Tankstellen-ID leer gelassen, werden die Preise nicht automatisch online aktualisiert. Du kannst die Preise dann nur manuell über das Webinterface eingeben.

---

## Preise einstellen

Im Bereich **Preise** siehst du alle Kraftstoffarten. Es gibt zwei Gruppen:

**Absolute Preise** (oberer Bereich):
- **e5, e10, diesel** — Hier stehen die tatsächlichen Preise (z.B. 1,85). Bei eingerichteter Tankstellen-ID werden diese drei Preise automatisch online aktualisiert.

**Relative Preise** (unterer Bereich, unterhalb der Trennlinie):
- **superplus, lkwdiesel, lpg, erdgas, adblue** — Diese werden als Auf- oder Abschlag zu e10 berechnet. Beispiel: SuperPlus ist oft 10 Cent teurer als E10 — dann gibst du hier `+0,10` ein. Für LKW-Diesel, der 5 Cent günstiger ist, trägst du `-0,05` ein.

Die relativen Preise musst du nur einmal einstellen — danach werden sie automatisch anhand des aktuellen E10-Preises berechnet.

---

## Zeilen zuordnen

Im Bereich **Zeilen** legst du fest, welche Kraftstoffart in welcher Zeile auf dem Display angezeigt wird. Du hast bis zu 6 Zeilen zur Verfügung. Nicht benötigte Zeilen einfach leer lassen.

---

## Update-Intervall

Das **Intervall** legt fest, wie oft die Preise automatisch online abgerufen werden (in Minuten). Der Mindestwert ist 5 Minuten, um den Preisserver nicht zu überlasten.

---

## API-URL (für Fortgeschrittene)

Das Feld **API-URL** kann normalerweise leer gelassen werden — die Tankstellenanzeige nutzt dann automatisch den richtigen Server. Nur wenn du einen eigenen Preisserver betreibst, trägst du hier dessen URL ein. Details siehe [Eigene API-URL](api.md).

> **Wichtig:** Auch bei einer eigenen URL muss eine Tankstellen-ID eingetragen werden, damit die Preisabfrage funktioniert.

---

## Einstellungen speichern

Wenn du alle Einstellungen vorgenommen hast, klicke auf **Konfiguration speichern**. In der Statusleiste am unteren Rand erscheint **Gespeichert** und die Anzeige auf dem Display aktualisiert sich.

Mit dem Knopf **Live-Preise aktualisieren** kannst du jederzeit die neuesten Preise vom Server abrufen, ohne auf das nächste automatische Update zu warten.

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Display bleibt dunkel | Prüfe die Stromversorgung (USB-C-Kabel und Netzteil) sowie das Flachbandkabel zum Display |
| Preise werden nicht aktualisiert | Prüfe, ob eine Tankstellen-ID eingetragen ist und die WLAN-Verbindung steht (LED grün) |
| Falsche Preise angezeigt | Prüfe die Tankstellen-ID — möglicherweise ist eine andere Tankstelle zugeordnet |

> **Tipp:** Bei Problemen mit dem WLAN oder dem Webinterface schau in die allgemeine Anleitung [WLAN einrichten](../allgemein/wlan-einrichten.md).
