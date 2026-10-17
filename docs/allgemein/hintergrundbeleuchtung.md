---
title: Hintergrundbeleuchtung
layout: anleitung
parent: Allgemein
nav_order: 6
---

# Hintergrundbeleuchtung

Die Displays gibt es mit zwei verschiedenen Schaltungen für die Hintergrundbeleuchtung, die genau entgegengesetzt angesteuert werden. Was bei der einen Schaltung „Licht an“ bedeutet, ist bei der anderen „Licht aus“. Der Controller muss deshalb wissen, welche Variante angeschlossen ist. Diese Seite beschreibt, wie er das herausfindet und wie du es korrigierst, falls etwas schiefgegangen ist.

> **Hinweis:** Welche der hier beschriebenen Wege dein Display kennt, hängt von der Version seiner Betriebssoftware (Firmware) ab. Ab welcher Version was geht, steht in der Anleitung zu deinem Display.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Die Taster am Controller

An der Seite des Controllers sitzen drei Taster. Der mittlere ist der **Reset**-Taster; er liegt etwas nach innen versetzt, damit man ihn nicht versehentlich drückt. Daneben sitzen **BTN 0** und **BTN 3** — beide sind auf der Platine beschriftet. Für die Beleuchtung brauchst du nur **BTN 0** und **BTN 3**.

---

## Beim allerersten Start: Beleuchtung bestätigen

Beim **allerersten** Einschalten findet der Controller selbst heraus, welche Schaltung angeschlossen ist — dazu braucht er einmal deine Hilfe.

Auf dem Display steht dann **Jetzt BTN0 druecken**, und die Beleuchtung wechselt im Zwei-Sekunden-Takt zwischen hell und dunkel. Drücke die Taste **BTN 0** am Controller in dem Moment, in dem das Display **hell** ist.

Zur Bestätigung blinkt die Beleuchtung dreimal kurz. Das Ergebnis wird dauerhaft gespeichert, die Abfrage kommt nicht wieder — auch nicht nach einem Firmware-Update.

> **Hinweis:** Startet dein Display gleich mit dem normalen Bild, ist die Erkennung bereits erledigt — sie läuft nur ein einziges Mal.

---

## Danebengedrückt? Beleuchtung umschalten

Hast du im falschen Moment gedrückt — also während das Display dunkel war — merkt sich der Controller die verkehrte Variante. Die Beleuchtung verhält sich dann genau umgekehrt: Das Display bleibt im Betrieb dunkel, obwohl es läuft.

Am schnellsten korrigierst du das im laufenden Betrieb mit einem langen Tastendruck. Welche Taste das ist, hängt von der Firmware ab: ab 3.2 ist es **BTN 0**, davor **BTN 3**. Weißt du nicht, welche Version dein Display hat, probiere zuerst den Weg für 3.2 und danach den für 3.1 — die jeweils andere Taste richtet dabei keinen Schaden an.

### Ab Firmware 3.2: BTN 0 lange drücken

1. Warte, bis das Display vollständig hochgefahren ist. Ist die Beleuchtung dunkel, siehst du das Bild nicht — gib ihm nach dem Einschalten einfach ein paar Sekunden.
2. Halte **BTN 0** etwa **zwei Sekunden** gedrückt.
3. Die Beleuchtung schaltet auf die andere Variante um, das Display wird hell. Lass **BTN 0** jetzt los.

Die neue Einstellung wird sofort gespeichert und gilt auch nach dem nächsten Einschalten. Die Helligkeit wird dabei auf 100 % gestellt — falls sie versehentlich ganz heruntergedreht war, ist auch das damit erledigt.

> **Tipp:** Hast du aus Versehen umgeschaltet und das Display ist jetzt dunkel, halte **BTN 0** einfach noch einmal zwei Sekunden gedrückt — dann ist wieder die vorherige Variante aktiv.

> **Wichtig:** Halte **BTN 0** nicht länger als nötig fest. Hast du vorher schon einmal kurz auf **BTN 0** gedrückt, ist die Info-Anzeige offen — bei dunklem Display siehst du sie nur nicht. Ein langer Druck startet dann statt der Umschaltung einen Countdown, der nach acht Sekunden die WLAN-Daten löscht. Lässt du nach zwei bis drei Sekunden los, passiert nichts. Wird das Display dabei nicht hell, warte eine Minute — dann schließt sich die Info-Anzeige von selbst — und versuche es noch einmal.

### Bis Firmware 3.1: BTN 3 lange drücken

1. Warte, bis das Display vollständig hochgefahren ist. Ist die Beleuchtung dunkel, siehst du das Bild nicht — gib ihm nach dem Einschalten einfach ein paar Sekunden.
2. Halte **BTN 3** etwa **zwei Sekunden** gedrückt.
3. Die Beleuchtung schaltet auf die andere Variante um, das Display wird hell. Du kannst **BTN 3** loslassen.

Die neue Einstellung wird sofort gespeichert und gilt auch nach dem nächsten Einschalten. Die eingestellte Helligkeit bleibt dabei unverändert.

> **Tipp:** Hast du aus Versehen umgeschaltet und das Display ist jetzt dunkel, halte **BTN 3** einfach noch einmal zwei Sekunden gedrückt — dann ist wieder die vorherige Variante aktiv.

> **Hinweis:** Ab Firmware 3.2 hat ein langer Druck auf **BTN 3** im laufenden Betrieb keine Funktion mehr.

### Beim Neustart: Erkennung wiederholen

Mit diesem Weg läuft die Erkennung vom ersten Start noch einmal ab. Er funktioniert vor und nach 3.2 gleich.

1. Halte **BTN 3** gedrückt.
2. Drücke währenddessen kurz die **Reset**-Taste (die mittlere) und halte **BTN 3** weiter gedrückt.
3. Sobald **Jetzt BTN0 druecken** auf dem Display steht und die Beleuchtung im Zwei-Sekunden-Takt wechselt, kannst du **BTN 3** loslassen.
4. Bestätige wie beim ersten Mal mit **BTN 0** in dem Moment, in dem das Display **hell** ist.

> **Hinweis:** Dabei wird auch die Helligkeit der Beleuchtung wieder auf 100 % gestellt. WLAN-Zugangsdaten und alle übrigen Einstellungen bleiben erhalten.

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Das Display bleibt dunkel, obwohl es läuft | Die Beleuchtung ist auf die falsche Variante eingestellt. Halte ab Firmware 3.2 **BTN 0**, davor **BTN 3** im laufenden Betrieb zwei Sekunden gedrückt, siehe [Danebengedrückt?](#danebengedrückt-beleuchtung-umschalten) |
| Langes Drücken auf **BTN 0** oder **BTN 3** bewirkt nichts | Die Firmware deines Displays kennt diese Funktion mit dieser Taste nicht. Probiere die andere Taste, oder schau in der Anleitung zu deinem Display nach, welcher Weg für deine Version gilt. |
| Ab 3.2: Langes Drücken auf **BTN 0** schaltet nicht um | Die Info-Anzeige war offen, siehe den Hinweis unter [Ab Firmware 3.2](#ab-firmware-32-btn-0-lange-drücken). Warte eine Minute und versuche es noch einmal. |
| **Jetzt BTN0 druecken** erscheint beim Start, obwohl du das nicht wolltest | **BTN 3** war beim Start gedrückt. Bestätige einfach mit **BTN 0**, wenn das Display hell ist. |
| Das Display blinkt nach dem Bestätigen, bleibt danach aber dunkel | Du hast bei dunklem Display gedrückt. Halte ab Firmware 3.2 **BTN 0**, davor **BTN 3** im laufenden Betrieb zwei Sekunden gedrückt. |
