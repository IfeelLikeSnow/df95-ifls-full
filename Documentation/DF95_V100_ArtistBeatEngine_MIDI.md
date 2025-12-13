# DF95 V100 – Artist BeatEngine (MIDI)

V100 erweitert die V97-BeatEngine um eine Artist-Logik, die auf dem bestehenden
DF95-Artist-System (Coloring_ArtistBias_v1.json, DF95_COLORING/ARTIST) basiert.

## Idee

- Du wählst einen Artist im Coloring-Artist-Dropdown:
  - `DF95_Menu_Coloring_Artist_Dropdown.lua`
- Dieser Artist wird in `DF95_COLORING/ARTIST` gespeichert.
- V100 liest diesen Artist und erzeugt ein Drum-Pattern (Kick/Snare/Hat)
  mit artist-typischer Dichte, Ghost-Notes, Breakbeat-Bias, Humanize/Swing.

Aktuell unterstützt (u.a.):

- Autechre
- AphexTwin
- BoardsOfCanada
- Squarepusher_JazzBass
- IDM
- Glitch
- diverse weitere Artists aus `Coloring_ArtistBias_v1.json` (fallen auf einen
  moderaten IDM-Style zurück, falls kein spezielles Profil hinterlegt ist).

## Script: DF95_V100_Fieldrec_ArtistBeatEngine_MIDI.lua

### Workflow

1. Fieldrec vorbereiten:
   - PolyWAV ggf. in Monotracks explodieren.
   - V95/V95.2 auf das Material anwenden (Slices + Klassen).
   - V98 SliceKit (RS5k) bauen:
     - `V98_SliceKit_RS5k` (Kick=36, Snare=38, Hat=42).

2. Artist wählen:
   - `DF95_Menu_Coloring_Artist_Dropdown.lua` aufrufen.
   - Einen Artist auswählen (z.B. AphexTwin, Autechre, BoardsOfCanada, Squarepusher_JazzBass).
   - Der Artist wird in `DF95_COLORING/ARTIST` gespeichert.

3. V100 ausführen:
   - `DF95_V100_Fieldrec_ArtistBeatEngine_MIDI.lua` starten.
   - Das Script:
     - liest den Artist (oder zeigt eine Liste, wenn keiner gesetzt ist),
     - fragt nach Anzahl der Takte (Bars),
     - erzeugt Track `V100_ArtistBeat_MIDI`,
     - schreibt ein Drum-Pattern mit:
       - Kick (Note 36),
       - Snare (Note 38),
       - Hat (Note 42),
       - artist-spezifischer Komplexität,
       - Swing/Humanize,
       - Ghost-Notes und Breakbeat-Offbeats (je nach Profil).

4. Routing:
   - Den MIDI-Track `V100_ArtistBeat_MIDI` auf dein SliceKit routen
     (z.B. `V98_SliceKit_RS5k`) oder auf ein anderes Drum-Instrument.

## Artist-Profile (intern, V100)

V100 nutzt eine interne Zuordnung von Artist-Namen zu Profilen:

- `Autechre`:
  - hohe Komplexität, viele Offbeats,
  - starke Hats, Breakbeat-Bias,
  - mittlerer Swing, mehr Timing-Jitter.

- `AphexTwin`:
  - komplex, aber etwas strukturierter als Autechre,
  - Kicks/Snares mit zusätzlichen Offbeats,
  - Ghost-Snares, moderate Hats.

- `BoardsOfCanada`:
  - reduzierter, laid-back Beat,
  - weniger Hats, mehr Swing,
  - geringere Velocities, weicher Gesamteindruck.

- `Squarepusher_JazzBass`:
  - sehr hohe Dichte,
  - viele Hats (auch 16tel/32tel-Anteil),
  - starke Offbeat-Snares, Ghost-Notes,
  - hohe Velocities, aggressiver Charakter.

- `IDM`:
  - balancierte Komplexität,
  - moderate Offbeats, moderate Ghosts, etwas Swing.

- `Glitch`:
  - mehr Offbeats, mehr Zufall,
  - viel Hats, starke Variation.

Alle anderen Artists aus der Coloring-Artist-Liste werden als
"Neutral/IDM" interpretiert, mit moderaten Werten für Komplexität,
Swing und Humanize.

## Kombination mit V99

In Kombination mit V99 kannst du zwei Wege fahren:

- Klassisch (V99):
  - V99 OneClick (Fieldrec -> Kit -> Beat) nutzen,
  - danach den V97-Beat bearbeiten oder ersetzen.

- Artist-Driven (V100):
  - V99 nur für Fieldrec+Kit nutzen (BeatEngine dort optional),
  - V100 Artist BeatEngine verwenden, um ein Artist-Pattern zu erzeugen.
