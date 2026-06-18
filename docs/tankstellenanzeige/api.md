---
title: Eigene API-URL
layout: anleitung
parent: Tankstellenanzeige
nav_order: 4
---

# Tankstellenanzeige — Eigene API-URL

Diese Anleitung richtet sich an Nutzer, die eine eigene Datenquelle für die Preisanzeige verwenden möchten, anstatt die voreingestellte Live-Preisabfrage zu nutzen.

> **Hinweis:** Diese Seite ist nur relevant, wenn du die Preise über einen eigenen Server steuern möchtest. Für den normalen Betrieb mit Live-Preisen brauchst du das nicht.

## Inhalt
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Überblick

Die Tankstellenanzeige ruft in regelmäßigen Abständen Preisdaten von einem Server ab. Standardmäßig wird der integrierte Preisservice verwendet. Du kannst aber auch eine eigene URL hinterlegen — zum Beispiel ein PHP-Script auf deinem eigenen Webserver.

---

## URL im Webinterface eintragen

1. Öffne das Webinterface der Tankstellenanzeige (siehe [Einrichtung & Bedienung](anleitung.md)).
2. Gehe auf **Konfiguration**.
3. Trage deine URL im Feld **API-URL** ein (z.B. `http://meinserver.de/preise.php`).
4. Trage eine **Tankstellen-ID** ein — diese wird bei jedem Abruf als Parameter übergeben. Auch wenn dein Script die ID nicht auswertet, muss das Feld gefüllt sein, damit der Abruf stattfindet.
5. Klicke auf **Konfiguration speichern**.

---

## Wie der Abruf funktioniert

Die Tankstellenanzeige unterstützt sowohl **HTTP** als auch **HTTPS**. Wenn dein Server ein gültiges SSL-Zertifikat hat (z.B. Let's Encrypt), kannst du `https://` verwenden. Bei selbstsignierten Zertifikaten oder im lokalen Netzwerk nutze `http://` — beides funktioniert.

Die Tankstellenanzeige ruft deine URL per HTTP-GET auf und hängt die Tankstellen-ID als Parameter `t` an:

```
http://meinserver.de/preise.php?t=meine-id-123
```

Falls deine URL bereits Parameter enthält (z.B. `http://meinserver.de/preise.php?format=json`), wird die ID mit `&` angehängt:

```
http://meinserver.de/preise.php?format=json&t=meine-id-123
```

---

## Erwartetes JSON-Format

Dein Server muss ein JSON-Objekt (ein standardisiertes Textformat für Daten) mit den Kraftstoffpreisen zurückgeben. Die drei Schlüssel `e5`, `e10` und `diesel` werden erwartet:

```json
{"e5": 2.15, "e10": 2.09, "diesel": 1.89}
```

### Regeln

- **Content-Type** sollte `application/json` sein
- Die Preise sind Dezimalzahlen mit **Punkt als Dezimaltrennzeichen** (kein Komma)
- Alle drei Schlüssel `e5`, `e10` und `diesel` sollten vorhanden sein. Fehlt `e5`, wird das Update komplett übersprungen (die bisherigen Preise bleiben erhalten). Fehlen nur `e10` oder `diesel`, werden diese als 0 übernommen — gib daher immer alle drei Werte aus
- Zusätzliche Schlüssel werden ignoriert
- Bei einem Fehler sollte der Server einen HTTP-Statuscode ungleich 200 zurückgeben (z.B. 400 oder 500) — die Tankstellenanzeige überspringt dann das Update

---

## Beispiel: random.php

Dieses PHP-Script gibt bei jedem Aufruf zufällige Preise zurück. Praktisch zum Testen, ob die Tankstellenanzeige korrekt mit einer eigenen URL funktioniert.

```php
<?php
header("Content-Type: application/json; charset=utf-8");
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Pragma: no-cache");

// Komma zu Punkt normalisieren
$minRaw = isset($_GET['min']) ? str_replace(',', '.', $_GET['min']) : '1.50';
$maxRaw = isset($_GET['max']) ? str_replace(',', '.', $_GET['max']) : '2.50';

$min = floatval($minRaw);
$max = floatval($maxRaw);

if ($min <= 0 || $max <= 0 || $min >= $max) {
    http_response_code(400);
    exit(json_encode(["error" => "Invalid min/max range"]));
}

$minCent = (int)round($min * 100);
$maxCent = (int)round($max * 100);

$out = [
    "e5"     => rand($minCent, $maxCent) / 100,
    "e10"    => rand($minCent, $maxCent) / 100,
    "diesel" => rand($minCent, $maxCent) / 100,
];

print(json_encode($out));
?>
```

### Aufruf

```
http://meinserver.de/random.php?min=1.50&max=2.50&t=test-id
```

Der Parameter `t` wird vom Script nicht ausgewertet, muss aber in der Tankstellenanzeige eingetragen sein.

### Beispielausgabe

```json
{"e5": 1.87, "e10": 2.03, "diesel": 1.95}
```

---

## Eigenes Script schreiben

Als Vorlage für ein eigenes Script brauchst du nur drei Dinge:

1. Den **Content-Type Header** setzen (`application/json`)
2. Die drei Preise ermitteln (aus einer Datenbank, einer Datei, einer anderen API, ...)
3. Das Ergebnis als **JSON** ausgeben

### Minimalbeispiel (PHP)

```php
<?php
header("Content-Type: application/json");

$out = [
    "e5"     => 2.15,
    "e10"    => 2.09,
    "diesel" => 1.89,
];

print(json_encode($out));
?>
```

Das reicht bereits — die Tankstellenanzeige kann damit arbeiten.

### Einfachste Variante: Statische JSON-Datei

Du brauchst nicht einmal ein Script. Eine einfache Textdatei mit dem Namen `preise.json` auf einem Webserver reicht:

```json
{"e5": 2.15, "e10": 2.09, "diesel": 1.89}
```

Trage dann `http://meinserver.de/preise.json` als API-URL ein. Die Preise sind dann natürlich fest und ändern sich nur, wenn du die Datei manuell bearbeitest.
