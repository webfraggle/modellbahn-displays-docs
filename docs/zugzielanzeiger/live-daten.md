---
title: Echte Fahrplandaten anzeigen
layout: anleitung
parent: Zugzielanzeiger
nav_order: 5
---

# Echte Fahrplandaten anzeigen

In der Anzeigeart **Live** übernimmt der Zugzielanzeiger den Fahrplan eines realen Bahnhofs aus dem Internet — mit den aktuellen Abfahrtszeiten, Verspätungen und Störungsmeldungen.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Was der Live-Betrieb macht

Der Anzeiger fragt **jede Minute** die aktuellen Abfahrten deines Wunschbahnhofs ab und zeigt die nächsten drei Züge — oben den nächsten, darunter die beiden folgenden. Verspätungen, Zielbahnhöfe und Hinweise wie **Abweichende Wagenreihung** oder **Universal-WC fehlt** stammen von der Bahn selbst.

Ein Zug, der am Bahnhof endet und nicht weiterfährt, wird als **Nicht einsteigen** angezeigt.

Die Daten laufen dabei über einen Server von Modellbahn Displays (`zza.yuv.de`). Der holt sie bei der Deutschen Bahn beziehungsweise der SBB ab, kürzt lange Bahnhofsnamen und bereitet sie für die Anzeige auf.

> **Hinweis:** Dafür muss dein Anzeiger ins Internet kommen. Ein Heim-WLAN ohne Internetzugang reicht nicht aus. Schränkst du den Internetzugang deiner Geräte ein, muss `zza.yuv.de` erreichbar bleiben.

---

## Den Live-Betrieb einschalten

1. Öffne mit dem Zahnrad **⚙** die Einstellungen des Gleises
2. Wähle oben die Anzeigeart **Live**
3. Trage bei **Live-Bahnhof** die Nummer deines Bahnhofs ein (siehe unten)
4. Trage bei **Gleis** die Nummer des Bahnsteiggleises ein, zum Beispiel `3`
5. **Speichern**

Die Anzeige aktualisiert sich sofort nach dem Speichern.

> **Wichtig:** Ohne eine gültige Gleisnummer ab `1` passiert nichts — der Anzeiger holt dann keine Daten. Das Feld **Gleis** ist im Live-Betrieb also Pflicht.

---

## Die Bahnhofsnummer finden

Bahnhöfe werden nicht über ihren Namen abgefragt, sondern über eine Nummer.

### Deutschland

Für deutsche Bahnhöfe brauchst du die **EVA-Nummer** (auch IBNR genannt) — eine siebenstellige Zahl, die jeden Bahnhof eindeutig bezeichnet.

Die Nummern der deutschen Bahnhöfe stehen gesammelt in dieser [Tabelle der Bahnhofsnummern](https://docs.google.com/spreadsheets/d/1RUnR_lhxsDev5cRRcTUD57F1jyW4TrYMpy6W-X7JiUg/edit?usp=sharing). Such dort deinen Bahnhof und übertrage die Nummer in das Feld **Live-Bahnhof**.

> **Tipp:** Alternativ gibt es eine [Online-Suche nach der IBNR](https://www.michaeldittrich.de/ibnr/online.php), bei der du den Bahnhofsnamen eintippst.

Ab Werk steht im Feld die Nummer `8000115` — das ist Fulda.

### Schweiz

Für Schweizer Bahnhöfe stellst du der Bahnhofsnummer (BPUIC) die drei Ziffern **`111`** voran. Daran erkennt der Anzeiger, dass er die Daten bei der SBB holen soll statt bei der Deutschen Bahn.

Die Nummer findest du über eine Suche, die du im Browser aufrufst:

```
http://zza.yuv.de/searchSBB.php?query=Luzern
```

Ersetze `Luzern` durch den Namen deines Bahnhofs. Die Antwort ist eine schlichte Liste:

```
8505000 - Luzern
8508219 - Luzern Littau
8517336 - Luzern Verkehrshaus
```

Nimm die Nummer deines Bahnhofs und setze die `111` davor. Aus `8505000` für Luzern wird also `1118505000` — und genau das trägst du im Feld **Live-Bahnhof** ein.

> **Hinweis:** Diese Suche ist ein Behelf, solange es dafür noch kein Eingabefeld im Webinterface gibt.

---

## Was im Live-Betrieb anders ist

| | Im Live-Betrieb |
|---|---|
| **Weiterschalten** | Die Knöpfe **‹** und **›** haben keine Wirkung. Auch Taster, DCC und MQTT schalten nicht weiter — welcher Zug zu sehen ist, bestimmt der Fahrplan |
| **Deine Zugliste** | Bleibt gespeichert, wird aber nicht angezeigt. Schaltest du zurück auf **Manuell** oder **Intervall**, ist sie unverändert da |
| **Intervall-Zeit** | Wirkt nicht. Aktualisiert wird fest im Minutentakt |
| **Wagenreihung** | Wird nicht angezeigt — die Fahrplanquelle liefert diese Angabe nicht mit |
| **Zielbahnhöfe** | Werden teilweise gekürzt, damit sie auf die Tafel passen (aus `Frankfurt(Main)Hbf` wird `Frankfurt/M Hbf`) |

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Es werden keine Züge angezeigt | Prüfe, ob bei **Gleis** eine Zahl ab `1` steht und ob die Bahnhofsnummer stimmt |
| Schweizer Bahnhof zeigt nichts an | Fehlt die `111` vor der Nummer, wird der Bahnhof bei der Deutschen Bahn gesucht und nicht gefunden |
| Die Anzeige bleibt leer, obwohl alles eingetragen ist | Prüfe, ob dein Anzeiger ins Internet kommt. Ein WLAN ohne Internetzugang reicht nicht |
| Es kamen Daten, jetzt plötzlich nicht mehr | Das kann auch am Server liegen, über den die Abfrage läuft. Probier es später noch einmal |
| Es stehen weniger als drei Züge auf der Tafel | Dann fahren an diesem Gleis gerade nicht mehr Züge. Leere Plätze bleiben leer |
| Die Zeiten sind veraltet | Aktualisiert wird einmal pro Minute. Zusätzlich speichern die Server die Daten kurz zwischen — ein paar Minuten Verzögerung sind normal |
| **‹** und **›** tun nichts | Das ist im Live-Betrieb so. Für eigenes Schalten die Anzeigeart **Manuell** oder **Intervall** wählen |
| Meine Wagenreihung fehlt | Im Live-Betrieb gibt es keine Wagenreihung — siehe [Wagenreihung darstellen](wagenreihung.md) |
| An meinem Gleis fährt nie etwas | Prüfe im Fahrplan des Bahnhofs, ob an diesem Bahnsteiggleis überhaupt Züge halten |
