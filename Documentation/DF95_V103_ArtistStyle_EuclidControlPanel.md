# DF95 V103 – Artist+Style ImGui Panel + Euclid Rhythm Engine

V103 erweitert das DF95-Artist/Beat-System um ein ImGui-Controlpanel und eine
integrierte Euclid-Rhythmus-Engine.

## Neues Script

- `Scripts/IFLS/DF95/ReampSuite/DF95_V103_ArtistStyle_EuclidControlPanel.lua`

## Funktionen

### 1. Artist + Style Verwaltung (ImGui-Panel)

- Zeigt zwei Combo-Boxen:
  - **Artist (Person):**
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

  - **Style (Textur / Verhalten):**
    - Neutral
    - IDM_Style
    - Glitch_Style
    - WarmTape_Style
    - HarshDigital_Style

- Die Auswahl wird in Project-ExtStates gespeichert:
  - `DF95_ARTIST/NAME`
  - `DF95_STYLE/NAME`

- Button: **"V102 Artist+Style BeatEngine starten"**
  - Ruft das Script
    `DF95_V102_Fieldrec_ArtistStyleBeatEngine_MIDI_MultiArtist.lua`
    via `dofile()` auf.
  - Damit kannst du Artist/Style im Panel wählen und dann direkt einen
    Artist+Style-Beat erzeugen.

### 2. Euclid Rhythm Generator (ImGui)

- Bereich "Euclid Rhythm Generator" im Panel.

Einstellbare Parameter:

- **Schritte (Steps)**: 1–32
  - z.B. 8 → 8tel-Gitter, 16 → 16tel-Gitter etc.

- **Pulses (Hits)**: 0–Steps
  - z.B. 3 in 8 (klassisch 3/8-Feeling),
         5 in 8,
         7 in 8,
         3 in 4 (bei 4 Schritten).

- **Rotation**: 0–Steps-1
  - rotiert das Euclid-Muster (z.B. für unterschiedliche Offbeat-Platzierungen).

- **Note-Division** (Combo):
  - 1/4
  - 1/8
  - 1/16
  - 1/32
  - Die Division bestimmt die zeitliche Länge jedes Steps (in Beats).

- **MIDI-Note**:
  - direkte Eingabe einer Note-Nummer (0–127), z.B.:
    - 36 = Kick
    - 38 = Snare
    - 42 = Hat

Button:

- **"Euclid-Muster auf selektiertem Track erzeugen"**:
  - Erwartet einen selektierten Track.
  - Erzeugt ein neues MIDI-Item ab Cursor-Position.
  - Länge = `Steps * Division` in Beats.
  - Trägt für jeden Step mit "Hit" ein Note-On/Off-Event ein
    (mit leicht verkürzter Notenlänge, ca. 80 % des Step-Abstands).

### 3. Algorithmus (Euclid)

- Implementiert eine Bjorklund-basierte Euclid-Verteilung:
  - verteilt `Pulses` möglichst gleichmäßig auf `Steps`.
  - das Ergebnis wird in ein boolean-Pattern umgewandelt.
  - Rotation verschiebt das Pattern zyklisch.

Beispiele:

- Steps=8, Pulses=3, Div=1/8
  - → 3 Hits auf einem 8tel-Raster → 3/8-artiges Pattern.
- Steps=8, Pulses=5
  - → dichtes 5-in-8-Pattern.
- Steps=7, Pulses=3, Div=1/8
  - → ungerade 7-Step-Pattern (7/8-Grooves).
- Steps=12, Pulses=5, Div=1/16
  - → halbdichte 5-in-12 Pattern mit 16tel-Grid.

## Use Cases

- Nutze das Panel als zentrale Steuerzentrale für:
  - Artist/Style Auswahl (MultiArtist-System),
  - Start der V102 BeatEngine,
  - Erzeugung von Euclid-Hats, -Kicks oder -Snares auf einem freien Track.

- Typischer Workflow:
  1. Fieldrec -> V95/V95.2 -> V98 SliceKit (RS5k).
  2. Panel öffnen: `DF95_V103_ArtistStyle_EuclidControlPanel`.
  3. Artist/Style wählen.
  4. Optional: V102 Artist+Style BeatEngine starten.
  5. Zusätzlich: Euclid-Patterns für einzelne Stimmen (z.B. Hats) erzeugen.
