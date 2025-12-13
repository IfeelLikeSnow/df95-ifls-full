# DF95 V109 – Time Signature Engine / Meter Panel

V109 ergänzt das DF95-System um eine explizite Time-Signature- und Meter-Ebene:

- Du kannst echte Taktarten definieren (z.B. 3/4, 5/4, 5/8, 7/8, 9/8, 12/8, 17/8, 19/8, ...),
- diese Taktarten als Grid-Länge für Artist-/Euclid-/Adaptive-Beats nutzen,
- die Euclid-Engine an diese Taktart koppeln,
- und festlegen, ob die BeatEngine Artist, Euclid oder eine Hybrid-Kombination
  verwenden soll.

## Neues Script

- `Scripts/IFLS/DF95/ReampSuite/DF95_V109_TimeSignatureEngine_MeterPanel.lua`

## ExtStates

V109 schreibt/liest u.a.:

- `DF95_TIME/NUMERATOR`   – Zähler (z.B. 3, 5, 7, 12, 17, 19, ...)
- `DF95_TIME/DENOMINATOR` – Nenner als String: "1/4", "1/8", "1/16"
- `DF95_TIME/BAR_STEPS`   – abgeleitete Grid-Länge (Steps pro Takt)
- `DF95_TIME/MODE`        – Meter Mode für die BeatEngine:
  - "Artist+Euclid (Hybrid)"
  - "Artist only"
  - "Euclid only"
- `DF95_TIME/LOCK_EUCLID_TO_METER` – "1" / "0", ob Euclid Steps automatisch
  an die Taktart gekoppelt werden sollen.

Außerdem kann V109, wenn gewünscht, `DF95_EUCLID_MULTI/STEPS` und
`DF95_EUCLID_MULTI/DIVISION` passend zur Taktart setzen.

## Taktart & BAR_STEPS

Die Taktart besteht aus:

- Zähler (Numerator) – z.B. 3, 5, 7, 12, 17, 19, ...
- Nenner (Denominator) – 1/4, 1/8, 1/16

V109 berechnet daraus eine interne Grid-Länge `BAR_STEPS`:

- Für 1/4 (Viertel):
  - Faktor = 4
  - Beispiel: 5/4 → BAR_STEPS = 5 * (16/4) = 20 Steps

- Für 1/8 (Achtel):
  - Faktor = 2
  - Beispiel: 7/8 → BAR_STEPS = 7 * (16/2) = 56/2 = 28 Steps
  - Beispiel: 12/8 → BAR_STEPS = 12 * (16/2) = 96/2 = 48 Steps
  - Beispiel: 17/8 → BAR_STEPS = 17 * 8 = 136 → 136/?? (im Script auf ganzzahlige Steps gerundet)

- Für 1/16 (Sechzehntel):
  - Faktor = 1
  - Beispiel: 5/16 → BAR_STEPS = 5 * (16/1) = 80 Steps

In der Praxis bedeutet das:

- ungewöhnliche Takte wie 5/8, 7/8, 9/8, 12/8, 17/8, 19/8 etc. sind möglich,
- V107 kann dieses Grid nutzen, um Artist-/Euclid-Patterns darauf abzubilden.

(Hinweis: Die exakte Mapping-Logik von Artist-Patterns auf BAR_STEPS liegt
in V107 und zukunftigen Versionen, V109 definiert das Raster.)

## Meter Mode

Über den Meter Mode kannst du festlegen, wie zukünftige BeatEngines mit
dem definierten Raster umgehen sollen:

- "Artist+Euclid (Hybrid)":
  - Artist-Pattern + Euclid-Pattern werden logisch kombiniert.
- "Artist only":
  - Nur Artist-Pattern nutzen das definierte Raster.
- "Euclid only":
  - Nur Euclid-Pattern nutzen das Raster, Artist-Layer bleibt außen vor
    (oder minimal).

Diese Information wird in `DF95_TIME/MODE` gespeichert und kann von
V107+ zukünftigen Engine-Versionen ausgewertet werden.

## Euclid-Bindung

Checkbox: "Euclid Steps an Taktart koppeln"

- Wenn aktiviert (`LOCK_EUCLID_TO_METER = 1`):
  - setzt `DF95_EUCLID_MULTI/STEPS = BAR_STEPS`,
  - legt bei Bedarf auch `DF95_EUCLID_MULTI/DIVISION` passend zum Denominator.
- Wenn deaktiviert:
  - bleiben Euclid-Parameter unabhängig (z.B. für polyrhythmische Layer).

## Aktionen

Es gibt zwei Hauptaktionen:

1. **"Taktart + Euclid anwenden (Projekt-Takt setzen)"**
   - Aktualisiert:
     - `DF95_TIME/NUMERATOR`
     - `DF95_TIME/DENOMINATOR`
     - `DF95_TIME/BAR_STEPS`
     - `DF95_TIME/MODE`
     - ggf. `DF95_EUCLID_MULTI/STEPS` & `DIVISION`
   - Ruft `SetProjectTimeSignature2()` auf, um die Projekt-Taktart in REAPER
     zu setzen.

2. **"Nur ExtStates setzen (Projekt-Takt unverändert)"**
   - Aktualisiert nur die ExtStates, ohne die REAPER-Taktart zu ändern.
   - Sinnvoll, wenn du Taktarten logisch für die Engine definieren,
     aber das visuelle Projekt-Meter unangetastet lassen willst.

## Zusammenarbeit mit V107/V108

- **V108 (Artist Tempo Profiles / Euclid Panel):**
  - definiert Artist-spezifische BPM (Slow/Medium/Fast), sowie
    Euclid-Parameter (STEPS / DIVISION).
  - V109 kann diese Euclid-Einstellungen überschreiben oder ergänzen,
    wenn LOCK_EUCLID_TO_METER aktiv ist.

- **V107 (Fieldrec Adaptive BeatEngine MIDI):**
  - nutzt:
    - Projekt-Tempo,
    - `DF95_EUCLID_MULTI/STEPS` (als steps_per_bar),
    - Artist-Profile und Style,
  - um Beats auf dem vorgegebenen Grid zu erzeugen.
  - V109 stellt sicher, dass dieses Grid mit der gewählten Taktart
    konsistent ist.

## Typischer Workflow mit V109

1. Artist & Style setzen (z.B. mit deinem Artist/Style-Panel).
2. `DF95_V108_ArtistTempoProfiles_TempoAndEuclidPanel.lua` starten:
   - Tempo-Mode (Slow/Medium/Fast) und BPM wählen.
3. `DF95_V109_TimeSignatureEngine_MeterPanel.lua` starten:
   - Taktart wählen (z.B. 5/8, 7/8, 12/8, 17/8, 19/8, 3/4, 5/4).
   - ggf. Euclid-Bindung aktivieren.
   - Projekt-Taktart setzen oder nur ExtStates aktualisieren.
4. Adaptive & Permissions:
   - V105 (Adaptive Sample Engine),
   - V106 (Permission/Policy).
5. `DF95_V107_Fieldrec_AdaptiveBeatEngine_MIDI.lua` ausführen:
   - erzeugt Artist-/Euclid-/Adaptive-Beats auf dem durch V109
     definierten Grid.

## Status

V109 bildet die logische Meter-Ebene:

- Es erzeugt selbst keine Beats,
- definiert aber das zeitliche Raster, auf dem alle Modulschichten
  (Artist, Euclid, AdaptiveEngine) arbeiten können.
- Zukünftige DF95-Versionen (V110+) können `DF95_TIME/*` noch stärker
  auswerten, um z.B. metrisch modulierte Pattern (Taktwechsel, Odd-Meter-
  Sequenzen über mehrere Takte) aufzubauen.

