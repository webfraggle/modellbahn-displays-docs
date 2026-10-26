---
title: Zugdaten sichern und wiederherstellen
layout: anleitung
parent: Zugzielanzeiger
nav_order: 10
---

# Zugdaten sichern und wiederherstellen

Das Backuptool sichert die Zugliste eines Gleises in eine Datei auf deinem Computer und spielt sie bei Bedarf wieder ein.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Was gesichert wird — und was nicht

Gesichert wird die **Zugliste** eines Gleises — also alle Züge mit Zeit, Zugnummer, Ziel, Via, Hinweis, Wagenreihung und DCC-Adresse.

**Nicht** gesichert werden:

- deine **Bilder**
- die **Einstellungen** des Gleises (Anzeigeart, Gleisnummer, Intervall-Zeit, MQTT und so weiter)
- die **WLAN-Zugangsdaten**

Die Einstellungen sind schnell wieder eingetragen — die Zugliste nicht. Deshalb sichert das Tool genau die. Wie du die übrigen Sachen von Hand sicherst, steht unter [Konfiguration und Bilder sichern](#konfiguration-und-bilder-sichern).

> **Wichtig:** Sichere deine Zugliste **bevor** du ein Update des Dateisystems einspielst. Ein solches Update überschreibt Zugdateien und Bilder.

---

## Das Backuptool öffnen

Klicke unten links auf das **Menü-Symbol** (drei Striche) und wähle **Züge Backuptool**.

Das Backuptool verbindet sich von selbst mit dem Anzeiger, von dem die Seite kommt: Oben bei **Controller IP** steht schon seine Adresse, der Punkt neben **Backup & Restore** leuchtet grün und unten steht **Verbunden mit …**.

![Die Seite Backup & Restore direkt nach dem Öffnen: oben ist die IP-Adresse des Controllers eingetragen, der Punkt neben der Überschrift ist grün, links der Bereich Backup mit Gleis A, Gleis B und Von Controller lesen, rechts der Bereich Restore mit Dateiauswahl, Textfeld und dem noch ausgegrauten Knopf Wiederherstellen](backup-restore.png){: style="max-width: 80%;" }

> **Hinweis:** Bis Version 3.2.12 musst du die **IP-Adresse** zuerst von Hand eintragen: Gib sie oben bei **Controller IP** ein und klicke auf **Verbinden**. Erst danach lassen sich die Knöpfe darunter benutzen.

Bei der Ausführung für **ein Gleis** gibt es nur **Gleis A**. Wählst du dort **Gleis B**, meldet das Backuptool **Controller nicht erreichbar** — schalte dann zurück auf **Gleis A**.

---

## Eine Sicherung erstellen

1. Wähle im Bereich **BACKUP** aus, welches Gleis du sichern willst — **Gleis A** oder **Gleis B**
2. Klicke auf **Von Controller lesen**. Das Backuptool liest jetzt jeden Zug einzeln — bei vielen Zügen dauert das einige Sekunden. Am Ende steht unten zum Beispiel **18 Züge geladen**
3. Erst jetzt erscheinen neben dem Knopf die Knöpfe **⇩ Als Datei speichern** und **Alle Züge löschen**. Im Feld darunter stehen deine Zugdaten, ganz unten die Liste **Züge auf Controller**
4. Klicke auf **⇩ Als Datei speichern**

![Das Backuptool nach Von Controller lesen: neben dem Knopf sind jetzt die Knöpfe Als Datei speichern und Alle Züge löschen erschienen, im Feld darunter stehen die Zugdaten, unten die Liste Züge auf Controller mit einem roten Kreuz hinter jedem Zug](backup-gelesen.png){: style="max-width: 80%;" }

Die Datei landet im Download-Ordner deines Browsers — je nach Einstellung fragt der Browser vorher, wo du sie speichern willst. Ihr Name verrät, woher sie stammt: `backup_`, die IP-Adresse des Anzeigers, das Gleis und das Datum, zum Beispiel `backup_192-168-178-41_GleisA_2026-10-26.json`.

> **Tipp:** Du kannst die Datei danach umbenennen, zum Beispiel in `bahnhof-nord-gleisA-2026-10.json`. Das Backuptool liest beim Zurückspielen nur den Inhalt, der Name ist egal.

> **Hinweis:** Hast du zwei Gleise, brauchst du **zwei** Sicherungen — eine je Gleis.

---

## Eine Sicherung zurückspielen

1. Klicke im Bereich **RESTORE** auf **Datei auswählen** (je nach Browser auch **Choose file**) und wähle deine Sicherungsdatei. Ihr Inhalt erscheint im Textfeld darunter
2. Wähle darunter das Gleis aus, auf das die Züge sollen
3. Klicke auf **Wiederherstellen**. Das Backuptool zählt mit, welcher Zug gerade dran ist, und meldet am Ende zum Beispiel **Fertig: 52 gespeichert**

![Das Backuptool nach dem Wiederherstellen: rechts unter Restore ist die Sicherungsdatei von Gleis A geladen, darunter steht Fertig: 52 gespeichert](../allgemein/backuptool-wiederhergestellt.png){: style="max-width: 80%;" }

Alternativ kannst du den Inhalt einer Sicherung auch direkt in das Textfeld einfügen, wenn du ihn zum Beispiel per Mail bekommen hast.

**Wiederherstellen** lässt sich erst anklicken, wenn das Backuptool verbunden ist und im Textfeld etwas steht.

> **Wichtig:** Achte darauf, das richtige Gleis auszuwählen. Spielst du eine Sicherung von Gleis A auf Gleis B ein, landen die Züge dort.

Das Zurückspielen **ergänzt** die Zugliste: Züge aus der Sicherung, die es auf dem Gleis schon gibt, werden überschrieben — alle anderen Züge auf dem Gleis bleiben stehen. Willst du genau den Stand aus der Sicherung, lösche vorher alle Züge des Gleises (siehe [Alle Züge löschen](#alle-züge-löschen)).

> **Hinweis:** Ein Gleis fasst höchstens **100 Züge**. Würden es mit der Sicherung mehr, nimmt der Anzeiger die übrigen nicht an und das Backuptool meldet am Ende **Fehler**.

---

## Alle Züge löschen

Der Knopf **Alle Züge löschen** räumt die komplette Zugliste des gewählten Gleises ab — praktisch, wenn du von vorn anfangen willst oder eine Sicherung ohne alte Reste zurückspielen möchtest.

Du findest den Knopf nicht sofort: Er erscheint im Bereich **BACKUP** erst, **nachdem du auf Von Controller lesen geklickt hast**. Gelöscht werden genau die Züge, die das Backuptool dabei gelesen hat.

1. Wähle das Gleis aus und klicke auf **Von Controller lesen**
2. Klicke auf **⇩ Als Datei speichern**, damit du eine Sicherung hast
3. Klicke auf **Alle Züge löschen** und bestätige die Rückfrage. Das Backuptool zählt mit und meldet am Ende **Alle Züge gelöscht**

Einzelne Züge löschst du in der Liste **Züge auf Controller** mit dem roten **✕** hinter dem Zug.

> **Wichtig:** Erst sichern, dann löschen. Rückgängig machen lässt sich das nicht.

---

## Züge auf einen anderen Anzeiger übertragen

Hast du mehrere Zugzielanzeiger und willst dieselben Züge auf allen haben:

1. Sichere die Zugliste des ersten Anzeigers wie oben beschrieben
2. Öffne das Backuptool des zweiten Anzeigers — oder trage oben einfach dessen **IP-Adresse** ein und klicke auf **Verbinden**
3. Spiele die Datei dort ein

Die Sicherung lässt sich auch auf ein anderes Gleis zurückspielen: Wähle unter **RESTORE** einfach das Ziel-Gleis.

So kannst du auch einen Bahnsteig mit zwei Gleisen schnell gleich bestücken und danach nur noch die Abweichungen von Hand ändern.

---

## Konfiguration und Bilder sichern

In zwei Fällen ist alles weg, was nicht in der Zugsicherung steckt:

- Beim **Update des Dateisystems** über die Upgrade-Seite werden Zugdateien und Bilder überschrieben.
- Ist das Dateisystem nach einem Stromausfall beschädigt, **formatiert sich der Controller selbst** und startet sauber. Er läuft danach wieder, ist aber leer.

Beides passiert selten, aber es lohnt sich, vorbereitet zu sein.

### Die Einstellungen sichern

Ruf im Browser die Adresse deines Anzeigers auf, ergänzt um `/GleisA/config.json` — also zum Beispiel `192.168.178.41/GleisA/config.json`. Du siehst dann die Einstellungen dieses Gleises als Text. Speichere die Seite über das Menü deines Browsers als Datei ab. Hat dein Anzeiger zwei Gleise, machst du dasselbe noch einmal mit `/GleisB/config.json`.

> **Hinweis:** Diese Datei lässt sich nicht zurückspielen. Sie dient zum Nachschlagen — die Werte trägst du im Bedarfsfall von Hand wieder in das Konfigurationsfenster ein.

**Einfacher geht es so:** Öffne das Konfigurationsfenster mit dem Zahnrad **⚙** und mach ein Bildschirmfoto davon. Bei zwei Gleisen je eines. Das reicht für den Notfall völlig und du musst dich mit keiner Datei befassen.

### Die Bilder sichern

Schalte in der Kachel auf **Bilder** um. Klicke dann mit der rechten Maustaste auf ein Vorschaubild und wähle **Bild speichern unter** — die Vorschau ist die Originaldatei. Das wiederholst du für jedes Bild, das du behalten willst.

> **Tipp:** Am einfachsten ist es, die Bilder ohnehin dort aufzubewahren, wo du sie erstellt hast. Dann brauchst du sie gar nicht erst herunterzuladen.

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Die Knöpfe sind ausgegraut | Prüfe, ob der Punkt neben **Backup & Restore** grün ist. Wenn nicht: Trage oben die **Controller IP** ein und klicke auf **Verbinden** |
| **Wiederherstellen** ist ausgegraut, obwohl die Datei geladen ist | Das Backuptool ist nicht verbunden. Klicke oben auf **Verbinden** |
| Der Knopf **Alle Züge löschen** fehlt | Er erscheint erst, nachdem du **Von Controller lesen** geklickt hast |
| Unten steht **Controller nicht erreichbar**, obwohl die IP stimmt | Beim Anzeiger für ein Gleis ist **Gleis B** gewählt. Schalte auf **Gleis A** |
| Nach dem Wiederherstellen sind noch alte Züge da | Das Zurückspielen ergänzt nur. Lösche vorher alle Züge des Gleises, siehe [Alle Züge löschen](#alle-züge-löschen) |
| **Von Controller lesen** bringt nichts | Prüfe, ob die IP-Adresse stimmt und der Anzeiger eingeschaltet ist |
| Nach dem Wiederherstellen fehlen Züge | Prüfe, ob das richtige Gleis ausgewählt war |
| Meine Bilder sind nach dem Wiederherstellen weg | Bilder sind nicht Teil der Sicherung. Lade sie neu hoch — siehe [Bilder statt Züge anzeigen](bilder-anzeigen.md) |
| Die Einstellungen stimmen nicht mehr | Auch die sind nicht Teil der Sicherung. Trage sie über das Zahnrad **⚙** neu ein |
| Nach einem Firmware-Update sind alle Züge weg | Das passiert beim Update des Dateisystems. Spiele deine Sicherung wieder ein |
