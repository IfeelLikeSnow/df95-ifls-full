# DF95 V101 – Artist+Style Layer BeatEngine (MIDI)

V101 führt eine Trennung von "Artist" und "Style" in der BeatEngine ein und
baut auf V100 (Artist BeatEngine) auf.

## Grundidee

- **Artist** = konkrete Künstlerpersönlichkeit:
  - Aphex Twin
  - Autechre
  - Boards of Canada
  - Squarepusher

- **Style** = musikalischer Stil / Textur-Bias:
  - IDM_Style
  - Glitch_Style
  - WarmTape_Style
  - HarshDigital_Style
  - Neutral

Der Artist bestimmt in V101 das grundsätzliche Beatverhalten (Komplexität,
Breakbeat-Bias, Ghost-Notes, Hat-Dichte), der Style wirkt als Layer oben drauf
und moduliert diese Parameter (z.B. mehr/weniger Swing, Dichte, Jitter, Lautstärken).

## Script: DF95_V101_Fieldrec_ArtistStyleBeatEngine_MIDI.lua

### Ablauf

1. Artist wählen:
   - Das Script liest `DF95_ARTIST/NAME` aus den Project-ExtStates.
   - Wenn nichts gesetzt ist:
     - Es öffnet ein kleines Popup-Menü mit 4 Artists:
       - Aphex Twin
       - Autechre
       - Boards of Canada
       - Squarepusher
     - Die Wahl wird in `DF95_ARTIST/NAME` gespeichert.

2. Style wählen:
   - Das Script liest `DF95_STYLE/NAME`.
   - Wenn nichts gesetzt ist:
     - Es öffnet ein Popup-Menü mit Styles:
       - Neutral
       - IDM_Style
       - Glitch_Style
       - WarmTape_Style
       - HarshDigital_Style
     - Die Wahl wird in `DF95_STYLE/NAME` gespeichert.

3. Profile berechnen:
   - Artist-Profil:
     - definiert Basiswerte für:
       - Komplexität (Anzahl Zusatzkicks/-snares),
       - Breakbeat-Bias (Offbeats 0.75/1.75/...),
       - Ghost-Note-Wahrscheinlichkeit,
       - Hat-Dichte,
       - Swing (16tel-Feel),
       - Timing-Jitter,
       - Velocities (Main/Ghost).
   - Style-Profil:
     - skaliert/offsettet diese Basiswerte:
       - IDM_Style -> alles etwas dichter, etwas mehr Swing/Jitter.
       - Glitch_Style -> deutlich mehr Dichte, mehr Jitter.
       - WarmTape_Style -> weniger Dichte, mehr Swing, etwas softere Velocities.
       - HarshDigital_Style -> aggressiver, härter, mehr Offbeats.

4. Beat erzeugen:
   - Das Script fragt nach `Bars` (Anzahl Takte).
   - Es erzeugt einen Track `V101_ArtistStyleBeat_MIDI` mit einem MIDI-Item über diese Takte.
   - Es schreibt ein Drumpattern mit General-MIDI-Noten:
     - Kick  = 36
     - Snare = 38
     - Hat   = 42
   - Muster:
     - Grund-Backbeat (4/4) + 8tel-Hats (Basis),
     - plus artist-/style-abhängige Zusatzkicks, Offbeat-Snares, Ghost-Notes und Hats.

5. Verwendung mit SliceKit:
   - Den Track `V101_ArtistStyleBeat_MIDI` auf dein Kit routen (z.B. `V98_SliceKit_RS5k`).
   - Kick/Snare/Hat in RS5k entsprechen den Noten 36/38/42 (wie in V98/V97).

## Unterschiede zu V100

- V100 benutzt primär den Artist als Einflußgröße und behandelt IDM/Glitch
  quasi als "Pseudo-Artists".
- V101 trennt Artist und Style explizit:
  - Artist = Aphex/Autechre/BoC/Squarepusher.
  - Style  = IDM/Glitch/WarmTape/HarshDigital/Neutral.
- Das Profil für den Beat entsteht aus der Kombination beider Ebenen,
  was ein klareres mentales Modell und flexiblere Kombinationen ermöglicht.

## Empfehlungen

- Nutze V101, wenn du bewusst zwischen "wer" (Artist) und "wie" (Style)
  unterscheiden möchtest.
- Nutze V100, wenn du schnell einen Artist-bezogenen Beat ohne separate
  Style-Ebene erzeugen möchtest.
