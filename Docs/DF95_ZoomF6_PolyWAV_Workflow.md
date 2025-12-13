# DF95 Zoom F6 PolyWAV Workflow – PolyWAV Toolbox V2

Dieses Dokument beschreibt den empfohlenen Workflow für Zoom F6 / Multichannel-Aufnahmen
im DF95-System (V150+).

## 1. Aufnahme

- Nimm mit dem Zoom F6 in 6-Kanal-Konfiguration auf (z.B. Boom, zwei Lavs, Stereo Ambience, Spare).
- Übertrage die PolyWAV-Datei(en) auf deinen Rechner.

## 2. Import in REAPER

- Ziehe die PolyWAV-Datei(en) in ein REAPER-Projekt.
- Wähle die Items im Arrange-Fenster aus.

## 3. PolyWAV Toolbox V2 öffnen

- Öffne die DF95 SampleDB Toolbar.
- Klicke auf: **DF95 – SampleDB: PolyWAV Toolbox V2**.
- Das ImGui-Fenster zeigt alle selektierten Multichannel-Items an (inkl. Kanalanzahl).

## 4. Optionen

Im unteren Bereich der Toolbox gibt es zwei Schalter:

- **ZoomF6 Mapping (Name/Farbe/Pan)**  
  - Vergibt Rollen pro Kanal:
    - CH1 → Boom
    - CH2 → Lav1
    - CH3 → Lav2
    - CH4 → AmbL
    - CH5 → AmbR
    - CH6 → Spare
  - Setzt automatisch:
    - Tracknamen (`F6 CHx – Rolle`)
    - Track-Farben
    - Panning

- **SampleDB Bridge (Multi-UCS Eintrag)**  
  - Trägt die PolyWAV-Datei(en) in die DF95 SampleDB Multi-UCS ein:
    - `path` = Dateipfad
    - `ucs_category` = `FIELDREC`
    - `ucs_subcategory` = `ZoomF6`
    - `df95_catid` = `FIELDREC_ZoomF6`
    - `zoom_source` = `ZoomF6`
    - `zoom_role_map` = `"CH1=Boom;CH2=Lav1;CH3=Lav2;CH4=AmbL;CH5=AmbR;CH6=Spare"`
    - Längen- und Kanalinfo
    - `ai_status` = `pending` (bereit für spätere AI-Analyse)

Du kannst beide Optionen unabhängig voneinander aktivieren/deaktivieren.

## 5. Explode

- Klicke auf **„Explode Multichannel Items (REAPER Action)”**.
- REAPER führt die Standard-Explode-Action aus.
- Anschließend:
  - werden Tracks (sofern Option aktiv) benannt, gefärbt und gepannt.
  - werden (sofern Option aktiv) SampleDB-Einträge erzeugt/ergänzt.

## 6. Weiterverarbeitung im DF95-System

Sobald die PolyWAVs in der SampleDB stehen, können sie verwendet werden in:

- DF95 SampleDB Inspector
- Analyzer / Planner
- Texture Presets & AI Soundscape Generator
- Pack Exporter
- UCS-Renamer / UCS-Light-Workflows

So wird aus einer einzelnen Zoom-F6-Aufnahme ein vollständiger, integrierter Baustein
deiner Sound-Library.

