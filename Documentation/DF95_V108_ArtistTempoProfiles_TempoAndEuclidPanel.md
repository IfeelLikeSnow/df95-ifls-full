# DF95 V108 – Artist Tempo Profiles & Euclid Panel

V108 ergänzt das DF95-System um ein Artist-spezifisches Tempo-Profil
(Slow / Medium / Fast) sowie um ein zentrales Panel, in dem du Tempo und
Euclid-Grid bequem einstellen kannst.

## Neues Script

- `Scripts/IFLS/DF95/ReampSuite/DF95_V108_ArtistTempoProfiles_TempoAndEuclidPanel.lua`

## Funktionen

### 1. Artist-spezifische BPM-Zonen (Slow / Medium / Fast)

V108 kennt für jeden integrierten Artist drei typische BPM-Zonen:

- **Slow**   – langsamere, ruhigere Stücke
- **Medium** – typische Kern-Tempi
- **Fast**   – energetische / schnellere Stücke

Diese Zonen basieren auf:

- typischen Genre-Ranges (z.B. Drum&Bass 160–180 BPM, IDM/Glitch 90–150 BPM),
- veröffentlichten Album-BPM-Profilen und Song-BPM-Analysen,
- musikalisch sinnvollen Clustern (z.B. Durchschnittstempi bestimmter Alben).

In der Tabelle `tempo_profiles` sind u.a. hinterlegt:

- Aphex Twin
- Autechre
- Boards of Canada
- Squarepusher
- µ-ziq
- Apparat
- Arovane
- Björk
- Bochum Welt
- Bogdan Raczynski
- Burial
- Cylob
- DMX Krew
- Flying Lotus
- Four Tet
- The Future Sound Of London
- I am Robot and Proud
- Isan
- Jan Jelinek
- Jega
- Legowelt
- Matmos
- Moderat
- Photek
- Plaid
- Skylab
- Telefon Tel Aviv
- Thom Yorke
- Tim Hecker
- Proem

Für unbekannte Artists gibt es ein Default-Profil:

- Slow:   90 BPM
- Medium: 120 BPM
- Fast:   140 BPM

### 2. Lesen von Artist & Style

V108 liest:

- `DF95_ARTIST/NAME` – z.B. "Aphex Twin", "Autechre" usw.
- `DF95_STYLE/NAME`  – z.B. "IDM_Style", "Glitch_Style" (nur Anzeige)

Der aktuell gewählte Tempo-Mode kommt aus:

- `DF95_ARTIST/TEMPO_MODE` – "Slow" / "Medium" / "Fast" (Default: "Medium")

### 3. Auswahl des Tempo-Modes

Im Panel kannst du per Combo den Tempo-Mode wählen:

- "Slow"
- "Medium"
- "Fast"

V108 zeigt dir dann das für diesen Artist vorgeschlagene Tempo an, z.B.:

- "Aphex Twin" → Medium ≈ 130 BPM
- "Autechre"   → Fast   ≈ 160 BPM
- "Boards of Canada" → Slow ≈ 78 BPM

Der gewählte Mode wird nach:

- `DF95_ARTIST/TEMPO_MODE`

gespeichert und die BPM nach:

- `DF95_ARTIST/TEMPO_BPM`

### 4. Euclid Grid (STEPS & DIVISION)

Zusätzlich verwaltet V108 das Euclid-Grid, welches von V104/V107 genutzt wird:

- `DF95_EUCLID_MULTI/STEPS`
  - Anzahl der Schritte pro Takt (z.B. 3, 5, 7, 8, 12, 16, ...)
  - im Panel als Int-Slider (3–32).

- `DF95_EUCLID_MULTI/DIVISION`
  - Notenwert / zeitliche Auflösung:
    - `1/4`  – Viertel
    - `1/8`  – Achtel
    - `1/16` – Sechzehntel
    - `1/12` – Triolen-Bereich

Damit kannst du z.B. ungerade und polyrhythmische Grids definieren:

- 3 Steps @ 1/8  → 3/8-artiger Puls
- 5 Steps @ 1/16 → "5er"-Figuren im 16tel-Raster
- 7 Steps @ 1/16 → klassischer "odd-meter"-Feel
- 12 Steps @ 1/12→ triplet-ähnliche Strukturen

V107 liest `DF95_EUCLID_MULTI/STEPS`, um `steps_per_bar` zu setzen, und kann so
direkt mit deinem Euclid-Grid arbeiten.

### 5. Aktionen

Im Panel gibt es zwei Haupt-Buttons:

1. **"Tempo & Euclid anwenden (Projekt BPM setzen)"**
   - Setzt:
     - `DF95_ARTIST/TEMPO_MODE`
     - `DF95_ARTIST/TEMPO_BPM`
     - `DF95_EUCLID_MULTI/STEPS`
     - `DF95_EUCLID_MULTI/DIVISION`
   - und ruft `reaper.SetCurrentBPM(0, target_bpm, true)` auf,
     um die Projekt-BPM anzupassen.
   - Zeigt eine Bestätigung mit Artist, Mode, BPM, Steps & Division.

2. **"Nur ExtStates setzen (Projekt BPM unverändert)"**
   - aktualisiert nur die genannten ExtStates,
   - das Projekt-Tempo bleibt unverändert.
   - sinnvoll, wenn du Tempo lieber manuell setzt, aber V107/V104 mit
     konsistenten Metadaten arbeiten sollen.

### 6. Zusammenarbeit mit anderen Versionen

- **V101 / V102 (Artist+Style Layer Engine)**:
  - setzen typischerweise `DF95_ARTIST/NAME` und `DF95_STYLE/NAME`.
  - V108 baut darauf auf und ergänzt Tempo-Informationen.

- **V104 (ArtistStyle Euclid Control Panel)**:
  - definiert ggf. ebenfalls Euclid-Parameter.
  - V108 bietet eine kompakte Übersicht / Steuerung, die direkt mit
    Artist-Tempo verknüpft werden kann.

- **V105 (Adaptive Sample Engine)**:
  - bleibt unverändert, aber V107 verwendet Tempo & Grid aus V108,
    um das Pattern sinnvoll zu quantisieren.

- **V106 (Permission Panel)**:
  - steuert Minimal vs. Full Mode / Rekonstruktion.
  - V108 ist davon unabhängig, ergänzt aber das Timing-/Tempo-Gefüge.

- **V107 (Fieldrec Adaptive BeatEngine MIDI)**:
  - nutzt:
    - das Projekt-Tempo (das du in V108 setzen kannst),
    - das Euclid-Grid (`DF95_EUCLID_MULTI/STEPS` & `DIVISION`),
    - sowie Artist & Style aus `DF95_ARTIST`/`DF95_STYLE`,
  - um daraus feldaufnahmebasierte Beats zu bauen.

## Typischer Workflow (mit V108)

1. Artist & Style wählen (z.B. über dein Artist/Style-Panel).
2. `DF95_V108_ArtistTempoProfiles_TempoAndEuclidPanel.lua` starten:
   - Tempo-Mode (Slow/Medium/Fast) wählen,
   - Euclid-Steps & Division einstellen,
   - optional Projekt-Tempo setzen.
3. V105 & V106 wie gewohnt für Adaptive/Permissions nutzen.
4. `DF95_V107_Fieldrec_AdaptiveBeatEngine_MIDI.lua` ausführen:
   - Beat wird im gewählten Tempo & Grid erzeugt.

## Status

V108 ist als Steuer-Panel gedacht:

- Es erzeugt selbst keine Beats,
- sondern sorgt dafür, dass Artist, Tempo-Mode, BPM und Euclid-Grid
  konsistent und explizit definiert sind,
- so dass V107 (und spätere Engines) darauf aufbauen können.

