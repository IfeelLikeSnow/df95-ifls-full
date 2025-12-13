# DF95 – Toolbar Visual Setup Guide

Dieses Dokument erklärt, wie du die DF95-Toolbars in REAPER so einstellst,
dass Icons, Text und Tooltips optimal zusammenarbeiten.

---

## 1. Tooltips (Namen beim Hover anzeigen)

Damit beim Überfahren der Buttons mit der Maus der Button-Name als Tooltip erscheint:

1. Öffne REAPER.
2. Gehe zu **Options → Preferences…**.
3. Suche den Bereich **Appearance** / **General** (je nach REAPER-Version).
4. Aktiviere die Option sinngemäß:
   - **"Show tooltips for toolbar buttons"**
   - oder **"Display hints for toolbar buttons"**

Ab jetzt zeigt REAPER beim Hover über einen DF95-Button den Text an,
der im Toolbar-Editor hinter **Custom: ...** eingetragen ist.

Die DF95-Toolbars sind so angelegt, dass diese Namen schon sinnvoll und sprechend sind
(z. B. "Explode AutoBus", "FX Bus", "Coloring", "Reamp Hub / Toolbar" etc.).

---

## 2. Text unter Icons anzeigen (Text below icons)

REAPER speichert die Darstellung (Icons / Text) pro Toolbar in deiner lokalen Konfiguration.
Die DF95-MenuSet-Dateien liefern das Layout und die Actions, aber nicht den Darstellungsmodus.
Diesen stellst du einmalig pro Toolbar ein.

### Schritt-für-Schritt:

1. **Options → Customize menus/toolbars…**
2. Im Dropdown oben die gewünschte Toolbar auswählen, z. B.:
   - `Main toolbar`
   - `Main toolbar (DF95 Hub)`
   - `Toolbar 2` (falls als DF95 Reamp Toolbar genutzt)
3. Unten im Dialog findest du eine Auswahl für die Darstellung, z. B.:
   - *Icons only*
   - *Text only*
   - *Icons and text*
   - *Text below icons*
4. Wähle für DF95-Workflows z. B.:

   - **Main toolbar** (DF95_MainToolbar_FlowErgo_Pro):
     - *Text below icons* oder *Icons and text*, damit du die Namen der wichtigsten Buttons immer siehst.

   - **DF95 Hub Toolbar** (DF95_MainToolbar_FlowErgo_Hub):
     - *Icons and text* oder *Text below icons*, da jeder Hub eine eigene Funktionsebene aufmacht.

   - **Reamp Toolbar** (DF95_Reamp_Toolbar):
     - je nach Platz:
       - *Icons only* (wenn du den Platz sparen willst),
       - oder *Icons and text*, wenn du beim Lernen des Workflows die Labels sehen möchtest.

Sobald du diese Einstellung pro Toolbar einmal gesetzt hast, bleibt sie bestehen,
auch wenn du später die DF95-MenuSets erneut importierst oder aktualisierst.

---

## 3. Icons den Buttons zuweisen

Die DF95-Repo-Struktur liefert:

- alle Toolbar-Layouts in `Menus/*.ReaperMenuSet`
- alle Icon-Dateien in `Data/toolbar_icons/DF95/`
- sowie eine Mapping-Hilfe in `Documentation/DF95_Toolbar_Icon_Mapping.md`

### Empfohlener Ablauf:

1. Stelle sicher, dass das DF95-Repo im REAPER-ResourcePath entpackt ist.
2. Importiere die Toolbars:
   - **Main Toolbar**: `DF95_MainToolbar_FlowErgo_Pro.ReaperMenuSet`
   - **Hub Toolbar**: `DF95_MainToolbar_FlowErgo_Hub.ReaperMenuSet`
   - optional weitere DF95-Toolbars (Reamp, FXBus-Variants etc.).
3. Öffne erneut **Customize menus/toolbars…**, wähle die gewünschte Toolbar
   und markiere einen Button (z. B. "Reamp Hub").
4. Klicke auf **Icon…**:
   - wechsle im Icon-Dialog in den Ordner **DF95**,
   - wähle das empfohlene Icon laut Mapping-Doku:
     - z. B. `df95_reamp.png` für den Reamp Hub,
     - `df95_hub_bus_32.png` für den Bus & Routing Hub,
     - `df95_hub_color_32.png` für den Coloring Hub usw.

Das Mapping-Dokument `DF95_Toolbar_Icon_Mapping.md` listet alle DF95-Buttons und
die empfohlenen Icon-Dateien in Tabellenform auf.

---

## 4. Empfohlene Kombinationen für Produktivität & Klarheit

Basierend auf typischen DAW- und UI-Design-Ansätzen:

- **Main toolbar (FlowErgo Pro)**:
  - *Text below icons*  
  - Du siehst sowohl Funktion (Icon) als auch Label → ideal für Lernen & Alltag.

- **Hub toolbar (DF95 Hub)**:
  - *Icons and text*  
  - Hier sind die "Macro-Hubs" (Bus Routing, Coloring, Bias & Humanize, Slicing, Reamp, Export, QA).
    Eine klare Beschriftung unterstützt schnelle Orientierung.

- **Reamp Toolbar**:
  - Beim Einrichten: *Icons and text*
  - Später im Alltag: *Icons only*, wenn du den Platz brauchst.
  - Dank Tooltips kannst du mit der Maus über den Button gehen und dir den Namen dennoch anzeigen lassen.

- **Spezialisierte Toolbars (FX-Variants, QA-Toolbars etc.)**:
  - je nach Bildschirmplatz:
    - *Icons only* für maximalen Platz,
    - *Icons and text* während der Eingewöhnung.

---

## 5. Wichtig: Repo vs. persönliche REAPER-Einstellungen

Das DF95-Repo liefert:

- die Struktur der Toolbars,
- die Action-Zuordnungen,
- die Icons,
- und Dokumentation (Icon-Mapping, Visual-Setup).

Deine REAPER-Installation entscheidet:

- ob Tooltips angezeigt werden,
- ob Text unter Icons steht,
- ob eine Toolbar als Floating- oder Docked-Toolbar sichtbar ist.

Diese Einstellungen sind **absichtlich nicht** fest im Repo kodiert, damit du
den Look an deinen Bildschirm, dein Theme und deine Arbeitsweise anpassen kannst.

---
