# DF95 V104 – Artist+Style Panel (Multi-Lane Euclid)

V104 erweitert V103 um eine Multi-Lane Euclid Engine im ImGui-Panel.

## Neues Script

- `Scripts/IFLS/DF95/ReampSuite/DF95_V104_ArtistStyle_EuclidControlPanel_MultiLane.lua`

## Features

### 1. Artist + Style Verwaltung (wie V103)

- Artist-Auswahl (Personen):
  - Aphex Twin, Autechre, Boards of Canada, Squarepusher,
    µ-ziq, Apparat, Arovane, Björk, Bochum Welt, Bogdan Raczynski,
    Burial, Cylob, DMX Krew, Flying Lotus, Four Tet, The Future Sound Of London,
    I am Robot and Proud, Isan, Jan Jelinek, Jega, Legowelt, Matmos,
    Moderat, Photek, Plaid, Skylab, Telefon Tel Aviv, Thom Yorke,
    Tim Hecker, Proem.

- Style-Auswahl (Verhaltens-/Textur-Layer):
  - Neutral, IDM_Style, Glitch_Style, WarmTape_Style, HarshDigital_Style.

- Speichert Auswahl in:
  - `DF95_ARTIST/NAME`
  - `DF95_STYLE/NAME`.

- Button:
  - **"V102 Artist+Style BeatEngine starten"**
    - ruft `DF95_V102_Fieldrec_ArtistStyleBeatEngine_MIDI_MultiArtist.lua` auf.

### 2. Euclid Multi-Lane Generator

- Ein globales Grid:
  - **Global Steps**: 1–32
    - z.B. 8 → 8tel-Feeling, 7 → 7/8, 16 → 16tel etc.
  - **Division** (Notenwert):
    - 1/4, 1/8, 1/16, 1/32
    - bestimmt die Dauer eines Steps in Beats.

- Vier Lanes (auf demselben Grid):
  - Kick Lane (KICK)
  - Snare Lane (SNARE)
  - Hat Lane (HAT)
  - Extra Lane (EXTRA)

Je Lane ein Block mit:

- **aktiv Checkbox**:
  - Lane kann ein-/ausgeschaltet werden.

- **Pulses** (Hits):
  - 0–Steps, z.B. 3 in 8, 5 in 8, 7 in 8 etc.

- **Rotation**:
  - 0–Steps-1, verschiebt das Pattern (z.B. Variation der Offbeats).

- **MIDI Note**:
  - 0–127, Standardvorschläge:
    - KICK: 36
    - SNARE: 38
    - HAT: 42
    - EXTRA: 39 (oder frei wählbar).

Button:
- **"Euclid Multi-Lane auf selektierten Track schreiben"**:

Ablauf beim Klick:

1. Erwartet einen selektierten Track in REAPER.
2. Liest die globalen Werte (Steps/Division) und pro Lane Pulses/Rotation/Note/aktiv.
3. Berechnet für jede aktive Lane ein Euclid-Muster:
   - Bjorklund-Verteilung (Pulses gleichmäßig auf Steps verteilt).
   - Rotation wird pro Lane angewandt.
4. Erzeugt ein einziges MIDI-Item auf dem selektierten Track:
   - Länge: `Steps * Division` in Beats.
   - Für jede Lane:
     - Schreibt Note-On/Off in die Lane-Note,
     - Note-Länge ~ 80 % des Step-Abstands.

### 3. Speichern der Einstellungen

- Alle Euclid-Multi-Parameter werden in Project-ExtStates gespeichert:
  - Section: `DF95_EUCLID_MULTI`
  - Keys z.B.:
    - `STEPS`, `DIVISION`
    - `KICK_PULSES`, `KICK_ROT`, `KICK_NOTE`, `KICK_EN`
    - `SNARE_PULSES`, ...
    - `HAT_*`, `EXTRA_*`.

So bleiben deine bevorzugten Euclid-Einstellungen projektbezogen erhalten.

## Nutzungsideen

- Typische Konfigurationen:
  - Steps=8, Division=1/8:
    - KICK: Pulses=3, ROT=0 (3/8-Beat)
    - SNARE: Pulses=2, ROT=4
    - HAT: Pulses=7, ROT=0 (nahezu durchgehend, mit Euclid-Feeling)
  - Steps=7, Division=1/8:
    - 7/8-Feeling, z.B. 3,4,5-Puls-Varianten auf verschiedenen Lanes.
  - Steps=16, Division=1/16:
    - feine 16tel-Euclid-Patterns für Hats + Glitch-Snare-Einsätze.

- Verwendung mit DF95 ReampSuite / Fieldrec:
  1. Fieldrec -> V95/V95.2 Slicing & Klassifizierung.
  2. V98 SliceKit (RS5k) bauen.
  3. `DF95_V104_ArtistStyle_EuclidControlPanel_MultiLane` öffnen.
  4. Artist + Style wählen.
  5. Entweder:
     - V102 BeatEngine laufen lassen UND Euclid-Lanes als zusätzliche Layer bauen,
     - oder nur Euclid-Lanes als rhythmische Basis erzeugen.
