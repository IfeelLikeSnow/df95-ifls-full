# DF95 UI Styleguide – Toolbars & Color Philosophy (No DF95 Labels)

Dieses Dokument beschreibt die Gestaltung der DF95-Toolbars und die zugrunde liegende Farb- und Struktur-Logik,
nachdem alle Button-Beschriftungen von Präfixen wie „DF95 –“ befreit wurden. Ziel ist eine klarere, fokusierte
Arbeitsoberfläche, die Kreativität und Produktivität unterstützt.

## 1. Benennungs-Konzept

- Button-Labels verwenden **nur noch Funktionsnamen**, z. B.:
  - `Export (UCS)`
  - `META Helper GUI`
  - `Mic FX`
  - `Explode AutoBus`
  - `Toolbar Switcher`
- Kein „DF95 –“ mehr in den sichtbaren Labels:
  - kürzere Namen
  - bessere Lesbarkeit
  - geringere kognitive Last

Die technischen Skript-Namen (z. B. `DF95_Export_UCS_ImGui.lua`) bleiben unverändert, damit interne Abhängigkeiten
stabil bleiben.

## 2. Struktur der wichtigsten Toolbars

Zu jeder Toolbar existiert eine PNG-Übersicht im Repo:

- `DF95_MainToolbar_FlowErgo_Pro_Buttons.png`
- `DF95_ExportDesk_MainToolbar_Buttons.png`
- `DF95_MainToolbar_FlowErgo_Hub_Buttons.png`
- `DF95_EditToolbar_Arrange_Buttons.png`
- (weitere je nach Repo-Version)

Jede PNG zeigt die Buttons in der Reihenfolge, in der sie in REAPER angezeigt werden.

### 2.1 Main Toolbar FlowErgo Pro

Fokus: **Routing, Busses, Bias & Export**

Typische Buttons:

- Explode AutoBus
- FX Bus
- Coloring
- Master Bus
- Toolbar Switcher (DF95 Toolbars)
- Mic FX
- FX Seed
- Coloring Bus
- Coloring A/B (GainMatch)
- Bias Neutral / IDM / Glitch / BoC Warm
- Slicing (Weighted)
- Rearrange / Align
- Loop / Rhythm Builder
- MissingPlugin Reporter / AutoPatch
- META Bulk Wizard / META Helper GUI
- Export (UCS)

### 2.2 Export Desk Toolbar

Fokus: **UCS & Export-Pipeline**

Typische Buttons:

- UCS From Filename
- Mic/Recorder Tags
- Export (UCS)
- Export Metadata CSV
- UCS README
- Export Pipeline README
- UCS Browser
- UCS ImGui Frontend

### 2.3 Hub Toolbar

Fokus: **Schneller Zugriff auf Hubs**

- Input & LUFS Hub
- Bus & Routing Hub
- FX / Creative Hub
- Export Desk
- QA / Tools
- Toolbar Switcher

### 2.4 Edit / Arrange Toolbar

Fokus: **Slicing, Rearranging, Clip-Editing**

- Slicing & Edit Hub
- Rearrange
- Align / Nudge
- Humanize
- Take-Motion / Stretching

(Details siehe entsprechende `*_Buttons.png` im Repo.)

## 3. Farb- und Zonen-Logik (Empfehlung für Themes)

Die Toolbars folgen einer Zone-basierten Denkweise:

- **Input / Recording Zone (Blau)**
  - Ruhe, technische Kontrolle
- **Creative / FX Zone (Orange & Lila)**
  - Energie, Experimente, Sound-Design
- **Final / Master Zone (Grün)**
  - Erfolg, Sicherheit, Freigabe
- **Export Zone (Gelb / Türkis)**
  - Aufmerksamkeit, Präzision, Finale Kontrolle
- **Neutral / Utility (Anthrazit)**
  - Hilfs- und QA-Tools

Tracking dieser Farbideen kann in Reaper-Themes, Track-Farben und Toolbar-Icons weitergeführt werden.

## 4. Bedienphilosophie: Weniger ist mehr

- Die Main Toolbar zeigt primär **Workflow-Schalter** (AutoBus, Busses, Export, Tool-Switcher).
- Detailfunktionen hängen an:
  - Hubs (Input & LUFS, Bus-Routing, Creative, QA)
  - Export Desk
  - Toolbar Switcher (für selten benutzte Toolbars)

Ziel:

- im **Alltag** hauptsächlich Main Toolbar + eine spezialisierte Toolbar sichtbar
- alle anderen Toolbars bei Bedarf via **Toolbar Switcher** öffnen/schließen

Dadurch:

- weniger visuelle Überladung
- leichterer Einstieg in Flow-Zustände
- schnellere Orientierung in großen Projekten

## 5. Weitere Anpassungen

Wenn neue Toolbars/Scripts hinzukommen:

1. Button-Namen ohne Präfix halten (z. B. „Android AutoTag“ statt „DF95 – Android AutoTag“).
2. Buttons logisch gruppieren:
   - Routing / Busses
   - Sound-Design
   - QA / Tools
   - Export & Metadata
3. In der README und PNG-Visualisierung ergänzen.

Dieses Styleguide-Dokument kann bei Bedarf erweitert werden, z. B. mit konkreten Farbcodes, Icon-Sets oder
Empfehlungen für bestimmte Reaper-Themes, die gut mit DF95 harmonieren.


## 6. AutoColor-Script

Im Ordner `Scripts/IFLS/DF95` befindet sich das Script:

- `DF95_AutoColor_Tracks_ByRole.lua`

Es färbt Tracks und Busse anhand ihrer Namen und Rollen ein (Input / Creative / Master / Export / QA).
Damit kann die im Colors-Styleguide beschriebene Farb-Logik schnell auf bestehende Projekte angewendet werden.

Empfohlener Einsatz:

- nach dem Anlegen oder Umbennen von Bussen
- nach dem Aufbau der Recorder-Input-Struktur (Zoom F6 / Zoom H5 / Android)
- bevor lange Editing- oder Sound-Design-Sessions starten, um die visuelle Orientierung zu verbessern.


## 7. Farb-Tools in der Main Toolbar

In der Main Toolbar (FlowErgo Pro) sind zwei Buttons für das Farb-Management vorgesehen:

- `AutoColor Tracks` ruft `DF95_AutoColor_Tracks_ByRole.lua` auf und färbt alle Tracks/Busses anhand ihrer Rolle.
- `Reset Track Colors` ruft `DF95_Reset_TrackColors_All.lua` auf und setzt alle Trackfarben auf die Reaper-Standardfarbe zurück.

Empfohlene Nutzung:

1. Neue Session oder bestehendes Projekt laden.
2. Ggf. manuell sinnvolle Track-/Bus-Namen vergeben (z. B. `IN_ZF6_...`, `FX_GLITCH_...`, `MASTER Bus`, etc.).
3. `Reset Track Colors` ausführen, um alte Farbreste zu entfernen.
4. `AutoColor Tracks` ausführen, um die Farb-Logik flächendeckend anzuwenden.
