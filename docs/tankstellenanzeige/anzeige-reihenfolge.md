---
title: Weitere Inhalte anzeigen
layout: anleitung
parent: Tankstellenanzeige
nav_order: 2
---

# Weitere Inhalte anzeigen

Deine Tankstellenanzeige kann mehr als nur Spritpreise zeigen. Sie durchläuft eine
Liste von Inhalten (genannt **Views**) immer wieder der Reihe nach — zum Beispiel:
erst die Preise, dann eine Wettervorschau, dann ein eigenes Foto. Du legst selbst
fest, welche Inhalte in welcher Reihenfolge und wie lange erscheinen.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## So funktioniert die Anzeige-Reihenfolge

Öffne das Webinterface und klicke auf **Konfiguration**. Unter **Anzeige-Reihenfolge**
siehst du die Liste der Inhalte. Das Display zeigt sie nacheinander und beginnt danach
wieder von vorn.

![Die Anzeige-Reihenfolge: jede Zeile ist ein Inhalt mit Anzeigedauer, Bearbeiten- und Löschen-Knopf](webinterface-anzeige-reihenfolge.png)

Jede Zeile steht für einen Inhalt und zeigt:
- links ein **Ziehgriff**-Symbol (drei Striche) zum Umsortieren,
- den **Typ** und darunter einen Hinweis auf den Inhalt — bei einer Tankstelle den Namen und die echten Preise (E5, E10, Diesel) als kleine Kacheln, bei einer URL die Adresse, bei einem Bild eine Mini-Vorschau,
- die **Anzeigedauer** in Sekunden,
- die Knöpfe **Bearbeiten** und **Löschen**.

> **Wichtig:** Änderungen werden erst übernommen, wenn du unten auf **Konfiguration speichern** klickst.

---

## Die drei Inhalts-Typen

| Typ | Was es zeigt |
|---|---|
| **Tankstelle** | Die klassische Spritpreis-Anzeige. Einrichtung siehe [Einrichtung & Bedienung](anleitung.md). |
| **URL / Web-Bild** | Ein Bild von einer Internet-Adresse, z. B. eine Wettervorschau oder ein Börsenkurs. |
| **Eigenes Bild** | Ein selbst hochgeladenes Bild, passend zugeschnitten. |

> **Hinweis:** Du kannst jeden Typ auch mehrfach aufnehmen — auch **mehrere Tankstellen**. Jede ist dabei völlig eigenständig (eigenes Template, eigene Tankstellen-ID, eigene Preise und Zeilen). So zeigst du z. B. eine Aral und eine Shell nacheinander, jede im passenden Design. Mehr dazu unter [Mehrere Tankstellen](#mehrere-tankstellen).

---

## Einen Inhalt hinzufügen

1. Wähle unter der Liste im Auswahlfeld den gewünschten **Typ** (Tankstelle, URL / Web-Bild oder Eigenes Bild).
2. Klicke auf **View hinzufügen**. Der neue Eintrag erscheint am Ende der Liste.
3. Klicke beim neuen Eintrag auf **Bearbeiten** und richte den Inhalt ein (siehe unten).
4. Klicke abschließend auf **Konfiguration speichern**.

---

## Mehrere Tankstellen

Du kannst beliebig viele **Tankstellen** anlegen — jede zeigt eine eigene Tankstelle, völlig unabhängig voneinander:

- eigenes **Template** (Design),
- eigene **Tankstelle** (über die **Tankstellen-ID**),
- eigene **Preise** und **Zeilen-Zuordnung**.

So richtest du eine (weitere) Tankstelle ein:

1. Wähle unter der Liste **Tankstelle** und klicke **View hinzufügen**.
2. Klicke beim neuen Eintrag auf **Bearbeiten**. Template, Tankstelle, Preise und Zeilen stellst du genauso ein wie bei der ersten — siehe [Einrichtung & Bedienung](anleitung.md).
3. **Konfiguration speichern**.

> **Tipp:** Eine neu hinzugefügte Tankstelle startet bereits mit sinnvollen Vorgaben (übliche Auf- und Abschläge für die relativen Sorten sowie eine fertige Zeilen-Aufteilung). Du musst meist nur das Template wählen und die Tankstelle suchen.

In der Liste zeigt jede Tankstelle ihre **echten Preise** (E5, E10, Diesel) als kleine Kacheln — so siehst du auf einen Blick, was angezeigt wird.

**Live-Preise aktualisieren:** Der Knopf **Live-Preise aktualisieren** unter der Liste holt die aktuellen Preise für **alle** Tankstellen auf einmal. Nach einem Klick auf **Konfiguration speichern** wird außerdem automatisch ein Abruf gestartet, sodass eine neu hinzugefügte Tankstelle sofort echte Preise zeigt.

> **Hinweis:** Das **Update-Intervall** und die **API-URL** (Adresse des Preisservers) gelten geräteweit für alle Tankstellen gemeinsam — sie werden nicht pro Tankstelle festgelegt.

---

## Reihenfolge und Anzeigedauer ändern

- **Reihenfolge:** Ziehe einen Eintrag am **Ziehgriff** (drei Striche links) nach oben oder unten an die gewünschte Stelle.
- **Dauer:** Trage im Feld **Sek.** ein, wie viele Sekunden der Inhalt angezeigt werden soll (zwischen 3 und 3600 Sekunden).

Vergiss auch hier das Speichern nicht.

---

## Bearbeiten und Löschen

- **Bearbeiten** öffnet die Einstellungen des jeweiligen Inhalts.
- **Löschen** entfernt den Eintrag aus der Liste. Bei einem eigenen Bild wird die zugehörige Bilddatei beim nächsten **Konfiguration speichern** automatisch vom Controller entfernt.

---

## URL / Web-Bild einrichten (mit Assistent)

Ein **URL / Web-Bild** zeigt ein Bild, das von einer Internet-Adresse geladen wird.
Klicke beim Eintrag auf **Bearbeiten**. Du kannst die Adresse direkt in das Feld
**Bild-URL** eintragen — oder bequem mit dem **Assistenten** zusammenstellen lassen:

1. Klicke auf **Assistent**.
2. Wähle unter **Funktion** aus, was angezeigt werden soll:
   - **Wetter** — eine Wettervorschau für einen Ort (Postleitzahl + Layout). Details: [Wetter-Bildgenerator](../bildgeneratoren/wetter.md).
   - **Markt (Kurse)** — ein Kurs einer Kryptowährung oder Aktie. Details: [Markt-Bildgenerator](../bildgeneratoren/markt.md).
3. Fülle die Felder aus. Unter **Vorschau** siehst du die erzeugte Adresse.
4. Klicke auf **URL übernehmen** — die Adresse wird in das Feld **Bild-URL** eingetragen.
5. **Konfiguration speichern**.

> **Tipp:** Du kannst auch jede andere Adresse eintragen, die ein Bild im **PNG**-Format (ein gängiges Bildformat) in der Größe deines Displays liefert. Die Adresse beginnt mit `http://` oder `https://`.

> **Hinweis:** Probiere eine Adresse im Zweifel zuerst im Browser aus. Erscheint dort das richtige Bild, funktioniert sie auch auf dem Display.

---

## Eigenes Bild hochladen

Ein **Eigenes Bild** ist ein Foto oder Logo, das du selbst hochlädst.

1. Klicke beim Eintrag auf **Bearbeiten** und dann auf **Bild hochladen/bearbeiten**.
2. Wähle eine Bilddatei von deinem Gerät.
3. Im Zuschnitt-Fenster kannst du das Bild **verschieben**, **vergrößern/verkleinern** und so passend ins Hochformat des Displays bringen.
4. Bestätige den Zuschnitt — das Bild wird auf den Controller hochgeladen und als Mini-Vorschau in der Liste angezeigt.
5. **Konfiguration speichern**.

> **Hinweis:** Die Bilder liegen auf dem Controller. Mit [Backup & Wiederherstellung](backup-restore.md) werden sie zusammen mit der übrigen Konfiguration gesichert.

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Änderungen erscheinen nicht auf dem Display | Hast du **Konfiguration speichern** geklickt? Erst dann werden sie übernommen. |
| Ein Web-Bild bleibt schwarz / wird nicht angezeigt | Prüfe die Adresse zuerst im Browser. Sie muss ein **PNG** in der passenden Display-Größe liefern und mit `http://` oder `https://` beginnen. |
| Statt des Bildes erscheint eine Fehlermeldung | Die Wetter-/Markt-Generatoren liefern bei falschen Eingaben ein gestaltetes Fehlerbild. Prüfe die Eingaben im Assistenten (siehe [Wetter](../bildgeneratoren/wetter.md) / [Markt](../bildgeneratoren/markt.md)). |
| Eigenes Bild wird nicht angezeigt | Lade es über **Bild hochladen/bearbeiten** (neu) hoch und speichere die Konfiguration. |
| Eine von mehreren Tankstellen zeigt keine aktuellen Preise | Prüfe, ob bei **diesem** Eintrag unter **Bearbeiten** eine Tankstelle ausgewählt ist — jede Tankstelle hat ihre eigene ID. |

> **Tipp:** Wie du die fertigen Adressen für Wetter und Börsenkurse zusammenstellst, steht ausführlich im Bereich [Bildgeneratoren](../bildgeneratoren/).
