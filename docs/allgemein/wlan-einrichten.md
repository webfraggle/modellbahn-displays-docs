---
title: WLAN einrichten
layout: anleitung
parent: Allgemein
nav_order: 1
---

# WLAN einrichten

Diese Anleitung beschreibt, wie du dein Display mit deinem Heim-WLAN verbindest. Die Schritte sind bei allen Displays gleich.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## So funktioniert die WLAN-Einrichtung

Beim ersten Einschalten (oder wenn keine WLAN-Daten gespeichert sind) erstellt dein Display ein eigenes WLAN-Netzwerk. Die Zugangsdaten werden auf dem Display angezeigt, wenn du kurz die Taste **BTN 0** am Controller drückst:

- **WLAN-Name:** MoBaDi-XXXXXX (die Zeichen sind bei jedem Controller anders)
- **Passwort:** MoBaDi_XXXXXX

## Schritt für Schritt

1. Verbinde dich mit deinem Smartphone oder Computer mit dem WLAN deines Displays (Name und Passwort stehen auf dem Display).
2. Normalerweise öffnet sich automatisch eine Konfigurationsseite. Falls nicht, öffne einen Browser und gib `192.168.4.1` ein.
3. Klicke auf **WLAN-Konfiguration**.
4. Wähle dein Heim-WLAN aus der Liste und gib das Passwort ein.
5. Klicke auf **Speichern**.
6. Das Display startet neu und verbindet sich mit deinem WLAN.

> **Hinweis:** Falls dein WLAN nicht in der Liste auftaucht, kannst du den Netzwerknamen (SSID) auch von Hand in das Eingabefeld eintippen. Die Liste wird nicht automatisch aktualisiert.

---

## LED-Status

Die LED am Controller zeigt dir den Verbindungsstatus an:

- **Grün** — Mit WLAN verbunden
- **Lila** — WLAN-Konfigurationsmodus (eigenes Netzwerk aktiv)
- **Rot** — Keine Verbindung

---

## WLAN-Daten ändern

Wenn du die WLAN-Daten ändern möchtest, drücke zweimal kurz hintereinander die **Reset**-Taste am Controller. Dann startet das Display wieder im Konfigurationsmodus und du kannst die Schritte oben wiederholen.

---

## IP-Adresse herausfinden

Sobald das Display mit deinem WLAN verbunden ist, bekommt es eine IP-Adresse. Diese brauchst du, um das Webinterface zu öffnen.

Drücke kurz die Taste **BTN 0** am Controller — auf dem Display wird die aktuelle IP-Adresse angezeigt (z.B. `192.168.178.41`).

Gib diese Adresse in einem Browser auf deinem Computer oder Smartphone ein.

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Kein WLAN-Netzwerk sichtbar | Warte 30 Sekunden nach dem Einschalten. Drücke ggf. zweimal Reset für den Konfigurationsmodus |
| Webinterface nicht erreichbar | Drücke die Taste BTN 0 am Controller, um die IP-Adresse auf dem Display anzuzeigen |
