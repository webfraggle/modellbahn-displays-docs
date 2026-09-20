---
title: Fernsteuerung über MQTT
layout: anleitung
parent: Zugzielanzeiger
nav_order: 9
---

# Fernsteuerung über MQTT

Betreibst du zu Hause eine Hausautomation wie Home Assistant, ioBroker oder Node-RED, kannst du deine Zugzielanzeiger von dort aus schalten. Auch Steuerungsprogramme wie Win-Digipet beherrschen MQTT. Diese Seite richtet sich an Fortgeschrittene mit einem eigenen MQTT-Broker im Netzwerk.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

> **Wichtig:** Die MQTT-Steuerung ist **neu und noch in Erprobung**. Sie funktioniert, ist aber bisher wenig im Einsatz. Die Topics und die Nachrichtenformate auf dieser Seite können sich in einer späteren Firmware deshalb noch ändern. Für den Alltagsbetrieb sind die Weboberfläche, [DCC](dcc-steuern.md) und die [Steuerungsprogramme](steuerungsprogramme.md) der erprobte Weg.

---

## Was MQTT ist

**MQTT** ist eine einfache Sprache, mit der Geräte im Heimnetz Nachrichten austauschen. In der Mitte steht ein Vermittler, der **Broker** — jedes Gerät meldet sich dort an und hört auf bestimmte Kanäle, die **Topics** heißen. Schickt jemand eine Nachricht an ein Topic, bekommen alle Geräte sie, die darauf hören.

Dein Zugzielanzeiger hört auf ein paar solcher Topics und führt aus, was dort ankommt.

> **Hinweis:** Du brauchst dafür einen laufenden MQTT-Broker in deinem Netzwerk. Betreibst du keinen, ist diese Seite für dich nicht relevant — nutze stattdessen die Weboberfläche, [DCC](dcc-steuern.md) oder ein [Steuerungsprogramm](steuerungsprogramme.md).

---

## MQTT einrichten

1. Öffne mit dem Zahnrad **⚙** die Einstellungen des Gleises
2. Trage unter **Gerät und MQTT** ein:
   - **Geräte-ID** — der Name deines Anzeigers. Voreingestellt ist `ESP_` und eine Kennung des Chips, zum Beispiel `ESP_73D100`. Du kannst einen eigenen Namen vergeben, etwa `bahnhof-nord`
   - **MQTT-Broker** — die Adresse deines Brokers, zum Beispiel `192.168.178.20`
   - **MQTT-Benutzer** und **MQTT-Passwort** — nur, wenn dein Broker eine Anmeldung verlangt
3. **Speichern**

Bleibt das Feld **MQTT-Broker** leer, ist MQTT ausgeschaltet.

> **Hinweis:** Der Anzeiger verbindet sich auf dem üblichen MQTT-Port **1883** ohne Verschlüsselung. Das ist für ein Heimnetz gedacht.

> **Wichtig:** Die Geräte-ID gilt für den ganzen Controller, nicht pro Gleis. Hast du zwei Gleise, teilen sie sich dieselbe ID und werden über den Gleisbuchstaben im Topic unterschieden.

---

## Die Topics

`<id>` steht überall für deine **Geräte-ID**.

| Topic | Nachricht | Wirkung |
|---|---|---|
| `zugzielanzeiger/<id>/A/cmd` | `next` oder `prev` | Gleis A einen Zug weiter oder zurück |
| `zugzielanzeiger/<id>/A/time` | `HH:MM` | Gleis A auf den Zug zu dieser Uhrzeit setzen |
| `zugzielanzeiger/<id>/A/zuege` | Zugdaten als JSON | Alle drei angezeigten Züge auf einmal setzen |
| `zugzielanzeiger/<id>/B/…` | wie oben | Dasselbe für Gleis B |
| `zugzielanzeiger/all/cmd` | `next` oder `prev` | **Alle** Anzeiger im Netz, beide Gleise |
| `zugzielanzeiger/all/time` | `HH:MM` | **Alle** Anzeiger im Netz, beide Gleise |

Die beiden `all`-Topics sind praktisch, wenn du mehrere Anzeiger auf der Anlage hast und alle gleichzeitig auf eine neue Modellzeit setzen willst.

> **Wichtig:** Züge, die du über das Topic `zuege` überträgst, werden **nicht gespeichert**. Sie stehen auf der Tafel, bis der nächste Zugwechsel kommt oder der Controller neu startet. Für dauerhafte Züge nutzt du die Weboberfläche — siehe [Züge anlegen und anzeigen](zuege-verwalten.md).

---

## Ausprobieren ohne Hausautomation

Der Controller bringt eine Testseite mit. Du erreichst sie über das **Menü** unten links, Eintrag **MQTT Test**. Dort kannst du dich mit deinem Broker verbinden und Nachrichten von Hand abschicken, um zu sehen, ob alles ankommt.

---

## Win-Digipet

Die MQTT-Steuerung ist vor allem deshalb entstanden, weil **Win-Digipet** MQTT unterstützt. Damit könnte das Steuerungsprogramm die Anzeiger direkt schalten — ohne das Hilfsprogramm, das [TrainController, iTrain und Rocrail](steuerungsprogramme.md) brauchen.

Erprobt ist das bisher nicht. Offen ist unter anderem, ob Win-Digipet einen eigenen Broker mitbringt oder ob zusätzlich ein Broker im Netzwerk laufen muss, und wie die Anzeiger-Topics dort einzutragen sind. Sobald das geklärt ist, steht an dieser Stelle eine Schritt-für-Schritt-Anleitung.

---

## Problembehebung

| Problem | Lösung |
|---|---|
| Der Anzeiger reagiert auf keine Nachricht | Prüfe, ob im Feld **MQTT-Broker** eine Adresse steht und gespeichert ist |
| Verbindung zum Broker kommt nicht zustande | Prüfe Adresse, Benutzer und Passwort. Der Anzeiger nutzt Port `1883` ohne Verschlüsselung |
| Es reagiert der falsche Anzeiger | Prüfe die **Geräte-ID**. Zwei Anzeiger dürfen nicht dieselbe ID haben |
| Es reagieren alle Anzeiger gleichzeitig | Dann hast du ein `all`-Topic benutzt. Nimm das Topic mit der Geräte-ID |
| Übertragene Züge sind nach einem Neustart weg | Das ist so — über MQTT gesetzte Züge werden nicht gespeichert |
| Nur Gleis A reagiert | Gleis B gibt es nur beim Zugzielanzeiger für zwei Gleise (Mittelbahnsteig) |
