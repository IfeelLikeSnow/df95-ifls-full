# DF95 V102 – Artist+Style BeatEngine (Multi-Artist, MIDI)

V102 erweitert die V101-Artist+Style-Engine um eine größere Liste expliziter Artists,
orientiert an deinem IDM-/Elektronik-Kosmos.

## Artists (Personen)

Folgende Artists werden als **Artists** (nicht als Styles) unterstützt:

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

Jeder Artist wird intern auf ein Rhythmus-Profil gemappt (Komplexität, Breakbeat-Bias,
Ghost-Notes, Hat-Dichte, Swing/Jitter, Velocities). Die Profile sind stilisierte
Approximationen und orientieren sich am charakteristischen Groove/Drum-Verhalten,
nicht an exakten Reproduktionen.

## Styles (Textur-/Verhaltenslayer)

Styles sind **keine Artists**, sondern modulieren das Artist-Profil:

- Neutral
- IDM_Style
- Glitch_Style
- WarmTape_Style
- HarshDigital_Style

Beispiele:

- Artist = Aphex Twin, Style = IDM_Style
- Artist = Autechre,   Style = Glitch_Style
- Artist = BoC,        Style = WarmTape_Style
- Artist = Flying Lotus, Style = IDM_Style oder WarmTape_Style
- Artist = Bogdan Raczynski, Style = HarshDigital_Style

## Script: DF95_V102_Fieldrec_ArtistStyleBeatEngine_MIDI_MultiArtist.lua

### Ablauf

1. Artist wählen
   - Script liest `DF95_ARTIST/NAME` aus Project-ExtState.
   - Wenn leer oder unbekannt:
     - Popup-Menü mit allen Artists (siehe Liste oben).
   - Auswahl wird in `DF95_ARTIST/NAME` gespeichert.

2. Style wählen
   - Script liest `DF95_STYLE/NAME`.
   - Wenn leer oder unbekannt:
     - Popup-Menü mit Styles.
   - Auswahl wird in `DF95_STYLE/NAME` gespeichert.

3. Profile kombinieren
   - `get_artist_profile(Artist)` liefert ein Basisprofil je Artist.
   - `get_style_profile(Style)` liefert einen Style-Layer (Multiplikatoren/Offsets).
   - `merge_profiles` kombiniert beides zu einem finalen Profil:

     - complexity
     - breakbeat_bias
     - ghost_prob
     - hat_density
     - swing
     - jitter
     - vel_main / vel_ghost

4. Beat erzeugen
   - Abfrage: Anzahl Takte (Bars).
   - Track `V102_ArtistStyleBeat_MIDI` wird erstellt.
   - MIDI-Noten werden geschrieben für:
     - Kick  = 36
     - Snare = 38
     - Hat   = 42
   - Muster:
     - Basis: 4/4-Backbeat + 8tel-Hats.
     - plus Artist/Style-abhängige Offbeats, Ghosts, Dichte und Humanize.

5. Verwendung
   - MIDI-Track auf dein SliceKit (z.B. `V98_SliceKit_RS5k`) routen.
   - Kick/Snare/Hat im Kit müssen auf 36/38/42 liegen (kompatibel zu V95/V98/V97).

## Hinweise

- Viele der Artists (µ-ziq, Bogdan Raczynski, Photek, Flying Lotus, Burial usw.)
  werden in der Engine bewusst als Cluster-Abwandlungen der Kern-Artists
  (Aphex/Autechre/BoC/Squarepusher) modelliert.
- Ziel ist nicht 1:1 Reproduktion, sondern ein inspirierter Rhythmus-/Groove-Starter,
  der sich anfühlt wie "in der Ästhetik" des jeweiligen Artists.

