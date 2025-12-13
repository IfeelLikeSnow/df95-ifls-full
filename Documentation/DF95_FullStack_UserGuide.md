# DF95 Full Template Stack – User Guide (Option 6)

Dieses Dokument beschreibt den Einsatz des vollständigen Template-Stacks:

- Project Templates
- Track Templates
- FX-Chains
- Render Presets
- Theme-Mod-Snippet

mit Fokus auf Produktivität und Kreativität (Flow-Zustand) auf Basis aktueller
Erkenntnisse zu UI-Design und DAW-Workflows.

## 1. Installation

1. Entpacke das ZIP in einen Ordner deiner Wahl.
2. Starte REAPER und gehe zu:
   - Options → Show REAPER resource path...
3. Öffne das Script:
   - Scripts/IFLS/DF95/DF95_Install_FullTemplateStack_Helper.lua
4. Führe das Script aus:
   - Es öffnet eine Konsole mit genauen Pfadangaben, wohin du
     - Projects/Templates → ProjectTemplates
     - TrackTemplates → TrackTemplates
     - FXChains → FXChains
   kopieren solltest.

Damit sind alle Bestandteile in REAPER sichtbar.

## 2. Project Templates – Workflow-Typen

Empfohlen:

- Fieldrec Template
- Creative Template
- Dialog Template
- ExportPrep Template

Strategie:
- Pro Projekt-Typ ein Template, um Kontextwechsel zu minimieren.
- Lieber mehrere spezialisierte Templates als ein überladenes „Universal“-Template.

## 3. Track Templates – Recorder & Busses

Empfohlene Konventionen:

- Zoom F6:
  - IN_ZF6_*  (z. B. IN_ZF6_LAV, IN_ZF6_SHOTGUN)
- Zoom H5:
  - IN_H5_*   (z. B. IN_H5_XY, IN_H5_LAV)
- Android Fieldrec:
  - IN_ANDR_* (z. B. IN_ANDR_MONO, IN_ANDR_STEREO)

- FX- und Creative-Busse:
  - FX_GLITCH_BUS
  - FX_FILTERMOTION_BUS

Diese Namen sind kompatibel zur AutoColor-Logik und machen Rollen pre-attentiv erkennbar.

## 4. FX-Chains – Safety & Coloring

Im Ordner FXChains:

- Safety_Highpass.RfxChain
- Coloring_Standard.RfxChain

Sie dienen als Startpunkt für:
- Rausch-Reserven
- generelle Tonformung
- kreative Varianten

## 5. Render Presets – UCS & Circuit Rhythm

Im Ordner RenderPresets:

- UCS_24bit.rpp-render
- CircuitRhythm.rpp-render

Sie bilden Beispiel-Render-Settings, die im Render-Dialog als Basis geladen
und angepasst werden können.

## 6. Theme-Mod – Psychologisch sinnvolle Anpassungen

Im Ordner ThemeMod:

- rtconfig_mod_snippet.txt

Empfehlung:

- Erzeuge eine Kopie deines aktiven Themes.
- Ergänze/justiere UI-Bereiche, z. B.:
  - Hintergrund etwas dunkler, weniger Kontrast-Sprünge.
  - Text gut lesbar, kein zu dünner Font.
  - Metering-Farben abgestimmt auf AutoColor-Zonen.

Aktuelle Ressourcen und Best Practices:
- Reapertips Theme (hohe Lesbarkeit, Kontrast, reduziert Eye-Strain).
- Community-Feedback zeigt: zu hoher Kontrast und „grelles“ Grün ermüden schneller. [Siehe Reaper-Theme-Diskussionen und Artikel zu DAW-Themes.]

## 7. Psychologischer Hintergrund (Kurzfassung)

- **Farblogik nach Zonen**:
  - Input = Blau → signalisiert „Quelle“ und Ruhe.
  - Creative = Orange / Magenta → signalisiert Energie, Experimente.
  - Master = Grün → signalisiert Abschluss, Sicherheit.
  - Export/Meta = Gelb / Türkis → signalisiert finale Aufmerksamkeit, Präzision.
  - QA = Anthrazit → signalisiert nüchterne Kontrolle ohne Ablenkung.

- **Weniger UI-Überladung**:
  - Nur die wichtigsten Toolbars standardmäßig sichtbar.
  - Spezial-Toolbars bei Bedarf via Toolbar-Switcher öffnen.

- **Flow-Förderung**:
  - Klar erkennbare Phasen: Aufnahme → Design → Feinschliff → Export.
  - Jede Phase hat eigene Template-Presets und Farben.

Diese Kombination aus Templates, Farben und Toolbars ist darauf ausgelegt,
dich schneller in stabilen, kreativen Flow zu bringen und mühselige
„Wo ist was?“-Suche zu vermeiden.


## 8. DF95 v41 – Template-Übersicht

In dieser Version sind vier Project Templates vorgesehen:

- `DF95_Fieldrec_Template.RPP`
  - Zoom F6 / H5 / Android Input-Zone
  - FX-Busse (Glitch, FilterMotion, Perc)
  - Coloring / Master / QA Tracks

- `DF95_Creative_Template.RPP`
  - IN_DESIGN-Folder für fertige Clips
  - FX-Busse für kreatives Sound-Design
  - Coloring / Master / QA

- `DF95_Dialog_Template.RPP`
  - Dialog- und Voice-Editing-Umgebung
  - FX- und Coloring-Bus
  - Master / QA

- `DF95_ExportPrep_Template.RPP`
  - Print-Master- und Alt-Master-Tracks
  - META/UCS-Kontrolltrack
  - QA-Track

Alle Templates sind kompatibel zur AutoColor-Logik und können mit den bestehenden
DF95-Toolbars, AutoBus-Scripts und dem ExportDesk kombiniert werden.


## 9. Standardisierte FX-Chain-Dateinamen (v42)

In dieser Version wurden zusätzliche, standardisierte Dateinamen für FX-Chains angelegt.
Die Chains liegen im Ordner `FXChains` und folgen u. a. diesen Präfixen:

- `MIC_...`         → MicFX- und Mikrofon-Korrektur-Chains
- `FX_GLITCH_...`   → Glitch / IDM / Stutter / Slice / Granular
- `FX_PERC_...`     → Percussion / DrumGhost / transientbetonte Chains
- `FX_FILTER_...`   → Filter / Motion / Sweeps / Movement
- `COLOR_...`       → Coloring / Tape / Saturation / Tone-Shaping
- `MASTER_...`      → Mastering / Safety / Limiter / LUFS

Die ImGui-Chain-Browser (MicFX / FXBus / Coloring / Master) verwenden diese Präfixe und
die Dateinamen-Analyse, um Chains automatisch nach Kategorien in Dropdown-Menüs zu sortieren.

Vorhandene, ältere Chain-Dateinamen bleiben unverändert erhalten und werden weiterhin
unter "Other" einsortiert, sodass es zu keiner Inkompatibilität kommt.


## 9. BalancedStudio Theme Installer (v48)

Das Script

- `Scripts/IFLS/DF95/DF95_Install_BalancedStudio_Theme.lua`

kopiert die Datei `DF95_BalancedStudio.ReaperThemeZip` automatisch in den
`ColorThemes`-Ordner deines REAPER-ResourcePath. Danach kann das Theme direkt
unter `Options > Themes` ausgewählt werden.

Empfohlen: Nach dem ersten Einrichten einmal ausführen und anschließend das
DF95_BalancedStudio-Theme als Standard wählen.


## 11. Erste Reamp Session (Palmer DACCAPO + Effektpedale)

**WICHTIG: Nie denselben physikalischen Kanal für Out und In verwenden (Out 3 ≠ In 3 etc.)!**

### 11.1 Reamp Hub öffnen

- Lade ein Projekt (z.B. DF95_Fieldrec_Template.RPP).
- Stelle sicher, dass die Main Toolbar "DF95_MainToolbar_FlowErgo_Pro" aktiv ist.
- Klicke oben auf den Button **Reamp Hub**.

Im Fenster:

- Wähle dein Interface:
  - *PreSonus Studio 1824c* (mehrere Out-Paare)
  - *Steinberg UR22mkII* (nur Out 1/2)
  - *Generic / Manuell* (für andere Interfaces)
- Wähle den Modus:
  - *Single Track* → ein Dry-Track wird direkt re-ampt
  - *Summe aus selektierten Tracks* → mehrere Dry-Tracks werden auf einen Reamp-Bus summiert

### 11.2 Routing-Optionen einstellen

- **Hardware-Out Paar:** wähle das Out-Paar, das physisch auf deine DACCAPO-Reamp-Box geht (z.B. Out 3/4).
- **Return-Input:** gib die Mono-Input-Nummer an, an der deine DI-Box / der Pedal-Return anliegt (z.B. 1 = Mono Input 1).
- **Send-Modus:**
  - *Post-Fader* → Reamp-Pegel folgt dem Mix-Fader.
  - *Pre-Fader* → Reamp-Pegel bleibt stabil, unabhängig vom Mix-Fader.
- **Master-Send auf Reamp-Summenbus deaktivieren:** verhindert, dass der Summenbus direkt auf den Master geht (sauberere Trennung von Mix und Reamp-Send).

### 11.3 Routing anlegen

1. Markiere einen oder mehrere Dry-Tracks (Gitarre, Synth, Fieldrec etc.).
2. Klicke im Reamp Hub auf **„Reamp-Routing für Auswahl erstellen“**.
3. Es werden angelegt/konfiguriert:
   - ein Send-Track (entweder einer der selektierten Tracks oder ein neuer REAMP_SUM_* Bus)
   - ein Return-Track (z.B. REAMP_RETURN_1824C_DACCAPO) mit:
     - Record-Arm an
     - Input-Monitoring an
     - gewähltem Mono-Input

### 11.4 Physikalische Verkabelung

- Interface-Out (gewähltes Out-Paar, z.B. Out 3/4) → **Palmer DACCAPO**
- DACCAPO Out → **Pedalboard**
- Pedalboard Out → **DI-Box**
- DI-Box Out → Interface-Mono-Input (entspricht deiner Return-Input-Einstellung)

**Nie:** denselben physikalischen Ausgang und Eingang für denselben Loop benutzen (z.B. Out 3 UND In 3 – das kann Feedback erzeugen).

### 11.5 Safety & Latenz

- **Safety Check:** im Reamp Hub auf „Safety Check“ klicken → öffnet DF95_Reamp_SafetyCheck_ImGui.
- **Testimpuls:**
  - Dry-Track selektieren
  - im Hub oder in der Action List: `DF95_Reamp_TestImpulse_Generate.lua` starten
- **Latenz messen:**
  - Reamp-Return aufnehmen
  - `DF95_Reamp_Latency_Analyze_And_Align.lua` verwenden oder
  - den **„Test & Align Wizard“** im Reamp Hub nutzen (`DF95_Reamp_TestAndAlign_Wizard.lua`):
    - Script findet Dry-/Wet-Impuls automatisch
    - bietet Optionen:
      - A: Wet-Item verschieben
      - B: Track-Delay am Return-Track setzen
      - C: Nur Latenz anzeigen

Damit lassen sich Kammfilter-/Phasenprobleme bei parallelem Dry+Wet-Betrieb minimieren.
