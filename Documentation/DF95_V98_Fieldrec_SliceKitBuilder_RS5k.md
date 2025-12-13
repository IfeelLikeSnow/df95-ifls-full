# DF95 V98 – Fieldrec SliceKit Builder (RS5k)

V98 baut auf dem V95/V95.1-Fieldrec-System auf und erzeugt daraus automatisch ein kleines
Drumkit mit ReaSamplomatic5000 (RS5k).

## Voraussetzungen

- Du hast dein Fieldrec-/PolyWAV-Material bereits mit V95/V95.1 bearbeitet, z.B. über:
  - `DF95_V95_2_Fieldrec_OneClick_SplitEngine`
- Dadurch existieren im Projekt Tracks und Items mit Namen der Form:
  - `V95_LOW_PERC*`   → Kick-/Tom-Rolle
  - `V95_SNARE_PERC*` → Snare-Rolle
  - `V95_HAT_CYMBAL*` → HiHat-/Cymbal-Rolle

## Script: DF95_V98_Fieldrec_SliceKitBuilder_RS5k.lua

### Aufgabe

- Sucht im Projekt nach V95-Klassentracks.
- Sammelt pro Rolle alle Slices (Items).
- Wählt pro Rolle den „besten“ Slice (lautester RMS).
- Erzeugt einen neuen Track `V98_SliceKit_RS5k`.
- Fügt für jede Rolle eine ReaSamplomatic5000-Instanz hinzu:
  - LOW_PERC   → Kick-Slot (Note 36)
  - SNARE_PERC → Snare-Slot (Note 38)
  - HAT_CYMBAL → Hat-Slot   (Note 42)
- Jede RS5k-Instanz:
  - lädt die zugrundeliegende Audio-Datei,
  - setzt Start/End im File auf den Bereich des Slices,
  - beschränkt Note Range auf eine GM-Note,
  - setzt moderate Attack/Release und Velocity-Empfindlichkeit.

### Verwendung

1. Fieldrec-Items vorbereiten:
   - PolyWAV ggf. in Monotracks explodieren,
   - `DF95_V95_2_Fieldrec_OneClick_SplitEngine` ausführen
     (oder direkt V95/V95.1 nutzen).
2. `DF95_V98_Fieldrec_SliceKitBuilder_RS5k` ausführen.
3. Ergebnis:
   - Neuer Track `V98_SliceKit_RS5k` mit bis zu 3 RS5k-Instanzen (Kick, Snare, Hat).
4. Zum Ansteuern:
   - `DF95_V97_Fieldrec_BeatEngine_MIDI.lua` verwenden
     (erzeugt ein MIDI-Pattern mit Kick=36, Snare=38, Hat=42),
   - oder manuell MIDI auf den Kit-Track routen/einzeichnen.

### Erweiterungsideen

- Mehrere Slices pro Rolle (Round-Robin / Velocity-Layer).
- Preset-System für Kits (Speichern/Wiederladen als Datei).
- Zusätzliche Rollen (FX/NOISE, DRONE/TEXTURE) mit eigenen Noten.
