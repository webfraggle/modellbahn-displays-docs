---
title: Datenformate und eigene Dateien
layout: anleitung
parent: Video-Display
nav_order: 4
---

# Datenformate und eigene Dateien

> **Vorabversion:** Diese Anleitung beschreibt eine Firmware, die noch nicht veröffentlicht ist. Beschriftungen, Menüpunkte und Abläufe können sich noch ändern, und einzelne Angaben können falsch sein. Sobald die Version fertig ist, verschwindet dieser Hinweis.
{: .warnung }

Das Video-Display kann verschiedene Arten von Inhalten anzeigen. Diese Seite erklärt, welche Formate es gibt, wofür sich welches eignet und wie du eigene Dateien vorbereitest.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Die Formate im Überblick

| Format | Was es ist | Wofür geeignet |
|---|---|---|
| **PNG** | Ein einzelnes, unbewegtes Bild | Logos, Plakate, Standbilder |
| **GIF** | Ein bewegtes Bild aus mehreren Einzelbildern | Kurze, einfache Animationen |
| **MJPEG** | Ein Video im Anzeige-Format des Displays | Echte Videoclips (aus dem [Video-Konverter](videos-konvertieren.md)) |
| **URL** | Ein Web-Bild, das bei jedem Durchlauf frisch aus dem Internet geladen wird | Aktuelle Inhalte wie Wetter oder Börsenkurse |

Alle vier Arten fügst du über die [Medien-Verwaltung](medien-verwalten.md) hinzu.

---

## Die richtige Bildgröße

Jedes Display hat eine feste Größe im Hochformat (zum Beispiel 120 Pixel, also Bildpunkte, breit und 240 Pixel hoch). Ein Bild wirkt am besten, wenn es genau in dieses Format passt.

Du musst die Zahlen aber nicht selbst ausrechnen: Nutze den Weg **Bild zuschneiden & hochladen** in der [Medien-Verwaltung](medien-verwalten.md). Dort ziehst du dein Bild passend zurecht, und es wird automatisch auf die richtige Größe deines Displays gebracht. Auch der [Video-Konverter](videos-konvertieren.md) zeigt dir oben die Zielauflösung an und schneidet das Video passend zu.

> **Tipp:** Zu kleine Bilder wirken auf dem Display unscharf, weil sie hochgerechnet werden. Verwende lieber ein Bild, das mindestens so groß ist wie die Anzeige.

---

## Standbilder (PNG)

PNG ist das beste Format für ruhige Inhalte wie ein Werbeplakat oder ein Logo. Fertige PNG-Dateien lädst du direkt über **Datei hochladen** hoch. Passt ein Bild noch nicht ins Hochformat, nimm **Bild zuschneiden & hochladen**.

Für jedes Standbild stellst du in der [Medien-Verwaltung](medien-verwalten.md) die **Dauer** ein (wie lange es zu sehen ist) und optional einen **Einblenden**-Effekt.

---

## Bewegte Inhalte: GIF oder MJPEG?

Für Bewegung gibt es zwei Wege:

- **GIF** eignet sich für kurze, einfache Animationen. Fertige GIF-Dateien lädst du direkt über **Datei hochladen** hoch.
- **MJPEG** ist das Format für echte Videoclips. Ein normales Video (zum Beispiel **.mp4**) wandelst du dafür einmal mit dem [Video-Konverter](videos-konvertieren.md) um.

Bei beiden legst du in der [Medien-Verwaltung](medien-verwalten.md) über den **Modus** fest, ob der Clip einmal, für eine feste Zeit oder mehrfach in einer Schleife läuft.

---

## Web-Bilder (URL)

Ein Web-Bild ist keine gespeicherte Datei, sondern eine **Adresse (URL)**. Das Display holt das Bild bei jedem Durchlauf frisch aus dem Internet — so bleibt der Inhalt immer aktuell. Die Adresse muss ein Bild liefern und mit `http://` oder `https://` beginnen.

Für fertige Wetter- und Marktbilder musst du keine Adresse selbst zusammenbauen: Der Knopf **Vorlagen (Wetter, Aktien, Krypto)** im URL-Fenster erledigt das. Alle Einzelheiten dazu stehen unter [Bildgeneratoren](../bildgeneratoren/).

---

## Speicherort: internen Speicher oder Speicherkarte

Das Display speichert deine Inhalte in seinem internen Speicher. Dieser ist bewusst klein gehalten und reicht für einige Bilder und kurze Clips. Wie viel Platz noch frei ist, siehst du in der [Medien-Verwaltung](medien-verwalten.md) rechts oben im Bereich **Mediendateien**.

Steckt eine **Speicherkarte (microSD)** im Controller, nutzt das Display automatisch diese — dann hast du deutlich mehr Platz für längere Videos und mehr Inhalte.

> **Hinweis:** Ob dein Modell einen Steckplatz für eine Speicherkarte hat, hängt von der Ausführung ab. Ohne Speicherkarte funktioniert das Display trotzdem — dann steht dir nur der interne Speicher zur Verfügung.

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Mein Bild wird unscharf angezeigt | Verwende ein größeres Bild (mindestens so groß wie die Anzeige) und schneide es mit **Bild zuschneiden & hochladen** zu |
| Mein Video lässt sich nicht hochladen | Videos müssen erst mit dem [Video-Konverter](videos-konvertieren.md) in **MJPEG** umgewandelt werden |
| Das Bild ist verzerrt oder abgeschnitten | Bringe das Bild mit **Bild zuschneiden & hochladen** ins richtige Hochformat |
| Der Speicher ist voll | Lösche nicht benötigte Inhalte oder verwende eine Speicherkarte (microSD), falls dein Modell einen Steckplatz hat |
