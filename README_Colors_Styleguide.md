# DF95 Colors & Track/Bus Styleguide

Dieses Dokument ergänzt den UI Styleguide und legt eine empfohlene Farb- und Rollenlogik
für Tracks und Busse in DF95-Projekten fest. Ziel ist eine konsistente visuelle Sprache,
die Orientierung, Kreativität und Produktivität unterstützt.

## 1. Zonenbasierte Farb-Logik

Die Session wird in funktionale Zonen unterteilt, jede mit einer eigenen Farb-Familie:

- **Input / Aufnahme (Blau-Töne)**
  - Zoom F6 Input-Tracks
  - Zoom H5 Input-Tracks
  - Android Fieldrec
  - weitere Recorder-Inputs

- **Creative / FX / Motion (Orange & Lila)**
  - Glitch / IDM / Rearrange Bus
  - FilterMotion Bus
  - DrumGhost / Percussion Bus
  - spezielle FX- oder Design-Busse

- **Coloring / Tone-Shaping (Neutral-Grau)**
  - Coloring Bus(e)
  - Pre-Master Sättigungs- oder Tonalitäts-Busse

- **Master / Final (Grün)**
  - Master Bus
  - Liefer-/Print-Busse (z. B. „Print Master“, „Alt Master“)

- **Export / Admin (Gelb & Türkis)**
  - Export-spezifische Utility-Tracks (z. B. Render Checker)
  - ggf. Tracker für Loudness / QC

- **Utility / QA (Anthrazit)**
  - Analyse-Tracks
  - Referenz/Null-/Sicherheits-Tracks

## 2. Konkrete Farbempfehlungen (Hex)

Diese Farben sind Vorschläge und können an das verwendete Reaper-Theme angepasst werden:

### 2.1 Input / Recorder

- Zoom F6:
  - **Farbe:** `#1F4FA8` (kräftiges Blau)
  - **Rolle:** „Multichannel Fieldrec / hochpräzise Aufnahme“

- Zoom H5:
  - **Farbe:** `#3366CC` (etwas helleres Blau)
  - **Rolle:** „Flexibler Stereo/Quad-Recorder“

- Android Fieldrec:
  - **Farbe:** `#345678` (gedämpftes, leicht graues Blau)
  - **Rolle:** „Mobile / spontane Aufnahmen“

### 2.2 Creative / FX

- Glitch / IDM / Rearrange Bus:
  - **Farbe:** `#FF8E3C` (kräftiges Orange)

- FilterMotion Bus:
  - **Farbe:** `#C255FF` (helles Lila / Magenta)

- DrumGhost / Percussion Design:
  - **Farbe:** `#D948D4` (sattes Magenta)

### 2.3 Coloring / Tone

- Coloring Bus / Tonal Bus:
  - **Farbe:** `#9E9E9E` (Neutral-Grau)
  - **Rolle:** „Ton-Formung ohne Fokus auf Spektakel“

### 2.4 Master / Final

- Master Bus:
  - **Farbe:** `#00B86C` (kräftiges Grün)
  - **Rolle:** „Finale Freigabe, Erfolg, Safety-Gain & Limiter“

### 2.5 Export / Admin

- Export / Render Utility-Tracks:
  - **Farbe:** `#FFEB3B` (helles Gelb)
  - **Rolle:** „Aufmerksamkeit beim finalen Schritt“

- UCS/Metadata Controller (optional):
  - **Farbe:** `#2DC9B4` (Türkis)
  - **Rolle:** „Präzise, nüchterne Verwaltung“

### 2.6 Utility / QA

- QA / Safety / Referenz-Tracks:
  - **Farbe:** `#424242` (dunkles Anthrazit)
  - **Rolle:** „sachlich, zurückhaltend“

## 3. Track- und Bus-Namen

Empfehlung für Namenspräfixe:

- Input-Tracks:
  - `IN_ZF6_`, `IN_H5_`, `IN_ANDR_`
- Creative-Busse:
  - `FX_GLITCH_`, `FX_IDM_`, `FX_PERC_`
- Coloring:
  - `COL_` oder `COLOR_`
- Master / Print:
  - `MASTER_`, `PRINT_`, `ALT_MASTER_`
- QA / Utility:
  - `QA_`, `UTIL_`, `ANALYZE_`

So bleiben sämtliche Rollen auch in großen Projekten klar lesbar.

## 4. Anwendung in Reaper

- Track-Farben können über:
  - Kontextmenü -> Set track color,
  - SWS-ColorSets
  - oder Scripts automatisiert gesetzt werden.

- DF95-Scripts können diese Farblogik optional aufgreifen:
  - z. B. Input-Autobusse automatisch in Blau,
  - Creative/FX-Busse in Orange/Magenta,
  - Master in Grün färben.

## 5. Erweiterbarkeit

- Für neue Recorder (z. B. Zoom H6, MixPre-Serie, iOS Apps) können weitere Input-Farben ergänzt werden.
- Für neue Creative-Busse (z. B. Doppler, Granular, Atmos Beds) können eigene Farb-Familien definiert werden.
- Wichtig ist, dass die Kernidee beibehalten wird:
  - Input = Blau
  - Creative = warm / intensiv
  - Master = Grün
  - Export/QA = klare Utility-Farben
