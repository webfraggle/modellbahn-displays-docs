---
title: Einrichtung & Bedienung
layout: anleitung
parent: Tankstellenanzeige
nav_order: 1
---

# Tankstellenanzeige — Einrichtung & Bedienung

Diese Anleitung beschreibt die Ersteinrichtung und die Konfiguration der Preisanzeige.

> **Hinweis:** Die Tankstellenanzeige kann ab Version 3.0.14 mehr als nur Tankstellenpreise zeigen — sie kann nacheinander mehrere Inhalte durchlaufen (z. B. Wetter, Börsenkurse, eigene Bilder oder Preise verschiedener Tankstellen). Diese Seite erklärt die **Preisanzeige**. Wie du weitere Inhalte ergänzt, steht unter [Weitere Inhalte anzeigen](anzeige-reihenfolge.md).

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Anschluss und erster Start

Prüfe, dass das Flachbandkabel zwischen Controller und Display richtig eingesteckt ist (siehe [Flachbandkabel anschließen](../allgemein/flachbandkabel-anschliessen.md)). Verbinde den Controller per USB-C-Kabel mit einer Stromquelle (USB-Netzteil oder Powerbank). Nach wenigen Sekunden erscheint das Startbild auf dem Display und die LED am Controller leuchtet.

> **Tipp:** Willst du den Controller stattdessen über die Anlage versorgen — aus einem Modellbahn-Trafo, dem digitalen Gleisstrom oder einem Gleichstrom-Netzteil —, brauchst du den als Zubehör erhältlichen Spannungswandler. Er wird an den 2-Pin-Stromeingang des Controllers angeschlossen und nimmt **Gleichstrom von 8 bis 27 Volt** oder **Wechselstrom von 8 bis 19 Volt** an.

> **Wichtig:** Ältere Spannungswandler vertragen **nur Gleichstrom**. Wechselstrom nimmt erst der aktuelle an. Bist du dir nicht sicher, welchen du hast, bleib beim Gleichstrom.

---

## WLAN einrichten und IP-Adresse herausfinden

Die WLAN-Einrichtung ist bei allen Displays gleich. Die vollständige Anleitung findest du unter [WLAN einrichten](../allgemein/wlan-einrichten.md).

> **Hinweis:** Die allgemeinen Seiten unterscheiden zwischen „Ab Firmware 3.2“ und „Bis Firmware 3.1“. Bei der Tankstellenanzeige gilt der Abschnitt **Ab Firmware 3.2** ab Version **3.2.15**. Mit älteren Versionen (bis 3.0.14) folgst du dem Abschnitt **Bis Firmware 3.1**. Welche Version dein Display hat, siehst du, wenn du kurz **BTN 0** drückst: Die Info-Anzeige zeigt die Nummer ganz unten.

Ab 3.2.15 kann die Tankstellenanzeige sich **zwei WLANs** merken, zum Beispiel dein Heim-WLAN und das im Vereinsheim. Außerdem lassen sich die WLAN-Daten direkt am Controller mit **BTN 0** löschen. Beides steht unter [WLAN einrichten](../allgemein/wlan-einrichten.md#ab-firmware-32).

---

## Taster und Hintergrundbeleuchtung

Ab Version 3.2.15 bedienst du die Tankstellenanzeige mit **BTN 0** genauso wie den Zugzielanzeiger:

- **kurz drücken** — Info-Anzeige mit IP-Adresse und Version ein- oder ausschalten. Nach einer Minute schließt sie sich auch von selbst.
- **zwei Sekunden halten** bei normaler Anzeige — Hintergrundbeleuchtung umschalten
- **lange halten bei offener Info-Anzeige** — Countdown, nach acht Sekunden werden die WLAN-Daten gelöscht. Loslassen bricht ab.

Die Displays gibt es mit zwei verschiedenen Schaltungen für die Hintergrundbeleuchtung. Beim Controller mit den Tastern **BTN 0** und **BTN 3** findet die Tankstellenanzeige beim ersten Start heraus, welche angeschlossen ist — dazu braucht sie einmal deine Hilfe. Auf dem Display steht dann **Jetzt BTN0 druecken**, und du bestätigst mit **BTN 0**, während das Display **hell** ist. Wie das genau geht und was du tust, wenn das Display danach dunkel bleibt, steht unter [Hintergrundbeleuchtung](../allgemein/hintergrundbeleuchtung.md) im Abschnitt **Ab Firmware 3.2**.

> **Wichtig:** Diese Abfrage erscheint auch **einmal nach dem Update** von einer älteren Version (bis 3.0.14) auf 3.2.15 oder neuer, weil die alten Versionen die Beleuchtung noch nicht gespeichert haben. Die Tankstellenanzeige startet erst weiter, wenn du **BTN 0** gedrückt hast. Danach kommt die Abfrage nicht wieder.

> **Hinweis:** Die Wege mit **BTN 3** im laufenden Betrieb aus dem Abschnitt „Bis Firmware 3.1“ gibt es bei der Tankstellenanzeige nicht. Die Versionen bis 3.0.14 kennen nur die ursprüngliche Schaltung und lassen sich nicht umschalten.

> **Tipp:** Auf dem 1,14"-Display steht der Countdown zum WLAN-Löschen in zwei Zeilen: **WLAN loeschen** und darunter **in 6 s**.

---

## Helligkeit einstellen

Ab Version 3.2.15 stellst du die Helligkeit der Beleuchtung im Webinterface ein. Öffne **Konfiguration**. Direkt unter der Anzeige-Reihenfolge findest du den Bereich **Helligkeit** mit einem Schieberegler von 20 bis 100 %.

Die neue Helligkeit gilt sofort, sobald du den Regler loslässt. **Konfiguration speichern** brauchst du dafür nicht. Die Einstellung bleibt auch nach einem Neustart erhalten.

> **Hinweis:** Die Helligkeit gehört nicht zum [Backup](backup-restore.md). Wie die WLAN-Daten ist sie direkt im Controller gespeichert. Nach dem Wiederherstellen auf einem anderen Controller stellst du sie dort einmal neu ein.

---

## Das Webinterface und das Menü

Öffne im Browser die IP-Adresse deines Displays (z. B. `192.168.178.41`). Auf der Startseite findest du:

- **Konfiguration** — die Anzeige einrichten (Preise, Inhalte, Einstellungen)
- **WLAN-Konfiguration** — WLAN-Zugangsdaten ändern
- **Controller-Upgrade** — Software des Controllers aktualisieren (Firmware-Update)

Auf allen Seiten gibt es unten links ein **Menü-Symbol** (drei Striche). Ein Klick darauf öffnet das Menü, über das du jederzeit zwischen **Startseite**, **Konfiguration**, **Backup & Restore**, **WLAN-Konfiguration** und **Controller-Upgrade** wechseln kannst.

Klicke auf **Konfiguration**. Du siehst die **Anzeige-Reihenfolge** — die Liste der Inhalte, die das Display nacheinander zeigt. Direkt nach dem Kauf steht dort ein einziger Eintrag: **Tankstelle**. Das ist deine Preisanzeige.

![Das Webinterface mit der Anzeige-Reihenfolge — oben die Liste der Inhalte, unten die Knöpfe zum Aktualisieren und Speichern](webinterface-anzeige-reihenfolge.png)

---

## Die Tankstellen-Einstellungen öffnen

Alle Einstellungen der Preisanzeige (Design, Tankstelle, Preise, Zeilen) stecken im Eintrag **Tankstelle**. Klicke in dessen Zeile auf **Bearbeiten** — es öffnet sich ein Fenster mit allen folgenden Einstellungen. Wenn du fertig bist, klickst du im Fenster unten auf **Übernehmen** und anschließend auf der Hauptseite auf **Konfiguration speichern**.

> **Tipp:** Du kannst auch **mehrere Tankstellen** nacheinander anzeigen — jede ist ein eigener Eintrag mit eigenen Einstellungen (Design, ID, Preise, Zeilen). Wie du weitere hinzufügst, steht unter [Mehrere Tankstellen](anzeige-reihenfolge.md#mehrere-tankstellen).

---

## Template wählen

Unter **Template** (Vorlage) findest du eine Liste aller verfügbaren Anzeige-Designs. Wähle das Template, das zu deiner Tankstelle passt.

---

## Tankstelle auswählen (Tankstellen-ID)

Damit Live-Preise einer bestimmten Tankstelle angezeigt werden, brauchst du deren **Tankstellen-ID**. Am einfachsten findest du sie über die eingebaute Suche:

1. Gib in das Feld **Tankstellen-ID** deine **Postleitzahl** ein (5 Ziffern).
2. Es klappt eine Liste der Tankstellen in der Umgebung auf. Mit dem Schieberegler **Umkreis** stellst du den Suchradius ein (1 bis 25 km).
3. Klicke deine Tankstelle in der Liste an — die ID und der Name werden automatisch übernommen.

> **Tipp:** Du kannst statt der Postleitzahl auch eine bereits bekannte Tankstellen-ID (langer Text aus Buchstaben, Zahlen und Bindestrichen) direkt in das Feld einfügen.

> **Hinweis:** Wird keine Tankstelle ausgewählt (Feld leer), werden die Preise nicht automatisch online aktualisiert. Du kannst sie dann nur von Hand eintragen.

---

## Preise einstellen

Im Bereich **Preise** siehst du alle Kraftstoffarten. Es gibt zwei Gruppen:

**Absolute Preise** (oberer Bereich):
- **e10** (Super E10), **e5** (Super), **diesel** (Diesel) — Hier stehen die tatsächlichen Preise (z. B. 1,85). Bei ausgewählter Tankstelle werden diese drei Preise automatisch online aktualisiert.

**Relative Preise** (unterer Bereich, unterhalb der Trennlinie):
- **superplus** (SuperPlus), **lkwdiesel** (LKW-Diesel), **erdgas** (Erdgas/CNG), **lpg** (Autogas), **adblue** (AdBlue) — Diese werden als Auf- oder Abschlag zu e10 berechnet. Beispiel: SuperPlus ist oft 10 Cent teurer als E10 — dann gibst du hier `0,10` ein. Für LKW-Diesel, der 5 Cent günstiger ist, trägst du `-0,05` ein.

Die relativen Preise musst du nur einmal einstellen — danach werden sie automatisch anhand des aktuellen E10-Preises berechnet.

---

## Zeilen zuordnen

Im Bereich **Zeilen** legst du fest, welche Kraftstoffart in welcher Zeile auf dem Display angezeigt wird. Für jede der bis zu 6 Zeilen gibt es ein Auswahlfeld — wähle dort die gewünschte Kraftstoffart aus. Zeilen, die du nicht benötigst, lässt du einfach leer.

---

## Update-Intervall

Das **Intervall** legt fest, wie oft die Preise automatisch online abgerufen werden (in Minuten). Der Mindestwert ist 5 Minuten, um den Preisserver nicht zu überlasten. Auch die Server speichern die Preise bis zu 10 Minuten zwischen, so dass es 15 bis 20 Minuten dauern kann, bis Preise aktuell sind. Das Intervall gilt geräteweit für **alle** Tankstellen gemeinsam — du findest das Feld zwar in jedem Tankstellen-Eintrag, der Wert wirkt aber überall gleich, egal wo du ihn änderst.

---

## Eigene Datenquelle (für Fortgeschrittene)

Das Feld **API-URL** (die Adresse eines eigenen Preisservers) kann normalerweise leer gelassen werden — die Tankstellenanzeige nutzt dann automatisch den Server von Modellbahn Displays. Nur wenn du einen eigenen Preisserver betreibst, trägst du hier dessen Adresse ein. Wie das Intervall gilt auch die API-URL geräteweit für **alle** Tankstellen gemeinsam. Details siehe [Eigene Datenquelle](api.md).

> **Wichtig:** Auch bei einer eigenen URL muss eine Tankstelle ausgewählt sein, damit die Preisabfrage funktioniert.

---

## Einstellungen speichern

Wenn du alle Einstellungen vorgenommen hast, klicke auf **Konfiguration speichern**. In der Statusleiste am unteren Rand erscheint **Gespeichert** und die Anzeige auf dem Display aktualisiert sich.

Mit dem Knopf **Live-Preise aktualisieren** kannst du jederzeit die neuesten Preise für **alle** Tankstellen-Einträge vom Server abrufen, ohne auf das nächste automatische Update zu warten. Auch hier gilt, dass der Server selbst Preise zwischenspeichert und es ein paar Minuten dauern kann, bis die Preise aktuell sind.

---

## Weitere Inhalte und Sicherung

- Du möchtest neben den Preisen noch Wetter, Börsenkurse oder eigene Bilder anzeigen? Das richtest du unter [Weitere Inhalte anzeigen](anzeige-reihenfolge.md) ein.
- Bevor du viel einstellst, lohnt sich eine Sicherung: Mit [Backup & Wiederherstellung](backup-restore.md) sicherst du deine komplette Konfiguration in einer Datei.

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Display bleibt dunkel | Prüfe die Stromversorgung (USB-C-Kabel und Netzteil) sowie das Flachbandkabel zum Display. Ab 3.2.15: Halte **BTN 0** zwei Sekunden gedrückt, um die Beleuchtung umzuschalten, siehe [Hintergrundbeleuchtung](../allgemein/hintergrundbeleuchtung.md) |
| Nach dem Update steht **Jetzt BTN0 druecken** auf dem Display | Das ist die einmalige Erkennung der Beleuchtung. Drücke **BTN 0**, während das Display hell ist, siehe [Taster und Hintergrundbeleuchtung](#taster-und-hintergrundbeleuchtung) |
| Der Bereich **Helligkeit** fehlt in der Konfiguration | Die Firmware ist älter als 3.2.15. Aktualisiere den Controller |
| Preise werden nicht aktualisiert | Prüfe, ob eine Tankstelle ausgewählt ist und die WLAN-Verbindung steht (LED grün) |
| Falsche Preise angezeigt | Prüfe die ausgewählte Tankstelle im **Tankstelle**-Eintrag unter **Bearbeiten** |
| Ich finde die Einstellungen nicht mehr | Alle Preis-Einstellungen liegen im Eintrag **Tankstelle** → **Bearbeiten**. Zwischen den Seiten wechselst du über das **Menü** unten links |

> **Tipp:** Bei Problemen mit dem WLAN oder dem Webinterface schau in die allgemeine Anleitung [WLAN einrichten](../allgemein/wlan-einrichten.md).
