# DF95 V110 – Fieldrec Beat Audio Render (Slices → Beat)

V110 ergänzt das DF95-Beat-System um eine RS5k-/Audio-nahe Ebene, indem
es aus einem von V107 erzeugten MIDI-Beatpattern direkt Audio-Items aus
deinen Fieldrec-Slices erzeugt.

## Script

- `Scripts/IFLS/DF95/ReampSuite/DF95_V110_FieldrecBeat_RenderAudioFromSlices.lua`

## Idee

Bisher:

- V95/V95.2: Fieldrec aufnehmen, schneiden, klassifizieren, einfärben.
- V105: Adaptive Sample Engine – identifiziert, welche Slices zu
  KICK / SNARE / HAT / PERC / OTHER gehören, und speichert GUID-Listen
  in `DF95_ADAPTIVE/*`.
- V107: BeatEngine – erzeugt ein MIDI-Pattern (Kick=36, Snare=38, Hat=42,
  Perc=39, Extra=40) basierend auf Artist, Style, Tempo, Taktart, Euclid
  und Adaptive/Permission-Infos.

V110:

- nimmt dieses MIDI-Pattern,
- nutzt die GUID-Listen aus V105,
- findet die Original-Items im Projekt,
- dupliziert sie auf neue Spuren und setzt sie an die Positionen der
  jeweiligen MIDI-Noten.

Das Ergebnis ist ein Audio-Beat, der wirklich aus deinem Fieldrec-Material
besteht – kein abstraktes MIDI-Skelett.

## Annahmen

- `DF95_ADAPTIVE/KICK_GUIDS`, `SNARE_GUIDS`, `HAT_GUIDS`, `PERC_GUIDS`,
  `OTHER_GUIDS` existieren und enthalten GUID-Listen als Strings
  (Trennzeichen: Komma, Semikolon oder Whitespace).
- Es existiert mindestens ein selektiertes Item mit MIDI-Take,
  idealerweise das von V107 erzeugte Beat-Item.
- V107 verwendet das Standard-Noten-Mapping:
  - Kick  → Note 36
  - Snare → Note 38
  - Hat   → Note 42
  - Perc  → Note 39
  - Extra → Note 40

## Funktionsweise

1. **Adaptive-Pools laden**

   V110 liest:

   - `DF95_ADAPTIVE/KICK_GUIDS`
   - `DF95_ADAPTIVE/SNARE_GUIDS`
   - `DF95_ADAPTIVE/HAT_GUIDS`
   - `DF95_ADAPTIVE/PERC_GUIDS`
   - `DF95_ADAPTIVE/OTHER_GUIDS`

   und wandelt die String-Listen in Lua-Tabellen um.

2. **Item-GUID-Map aufbauen**

   Das Script läuft über alle Spuren & Items des Projekts:

   - liest pro Item die GUID (`GetSetMediaItemInfo_String(it, "GUID", ...)`),
   - baut eine Map: GUID → Item.

   So können wir später für jede GUID aus dem Adaptive-Pool das
   zugehörige Quell-Item finden.

3. **Beat-MIDI-Item finden**

   V110 erwartet, dass du ein MIDI-Item selektiert hast:

   - es nimmt das **erste selektierte Item, das einen MIDI-Take hat**,
   - typischerweise das V107-Beat-Item.

4. **MIDI-Events auslesen**

   - `MIDI_GetAllEvts` / `MIDI_GetEvt` werden verwendet,
   - für jedes Note-On (`status 0x90`, `vel > 0`) wird:
     - die Note gelesen (36/38/42/39/40),
     - der PPQ-Offset akkumuliert,
     - über `MIDI_GetProjQNFromPPQPos` + `TimeMap2_QNToTime` die
       Projektzeit berechnet.

5. **Kategorie bestimmen**

   - Note → Kategorie:

     - 36 → `"KICK"`
     - 38 → `"SNARE"`
     - 42 → `"HAT"`
     - 39 → `"PERC"`
     - 40 → `"EXTRA"` (wird intern dem PERC-Pool zugeordnet)

6. **Slice wählen (Round-Robin)**

   - Für jede Kategorie gibt es einen Pool aus GUIDs.
   - Pro Hit wird round-robin durch den Pool iteriert:
     - KICK: guid[1], guid[2], ..., guid[n], wieder von vorne
     - SNARE: analog
     - usw.

   So werden vorhandene Slices gleichmäßig verteilt.

7. **Quell-Item duplizieren**

   Für jede Note/HIT:

   - GUID im Pool wählen,
   - dazugehöriges Quell-Item über die GUID-Map finden,
   - neue Spur bestimmen:

     - `DF95_V110_KICK`
     - `DF95_V110_SNARE`
     - `DF95_V110_HAT`
     - `DF95_V110_PERC_EXTRA`
     - `DF95_V110_OTHER` (Fallback)

   - auf dieser Spur ein neues Item erzeugen:
     - Position = Note-Zeit
     - Länge = Länge des Quell-Items
     - aktiven Take anlegen und dessen Source auf die des Quell-Takes setzen
     - Fades (In/Out) & Startoffset übernehmen

8. **Beschränkung auf Beat-Länge**

   - Es werden nur Noten gerendert, deren Zeit innerhalb der
     Grenzen des Beat-Items liegt (`D_POSITION` bis `D_POSITION + D_LENGTH`).

## Ergebnis

Nach Ausführung von V110:

- bekommst du zusätzliche Spuren:

  - `DF95_V110_KICK`
  - `DF95_V110_SNARE`
  - `DF95_V110_HAT`
  - `DF95_V110_PERC_EXTRA`

- auf denen Audio-Items liegen, die:

  - direkt aus deinen Fieldrec-Slices stammen,
  - in ihrer Originallänge gespielt werden,
  - an den Stellen platziert sind, wo V107 MIDI-Noten gesetzt hat.

Du kannst die MIDI-Spur dann:

- stummschalten oder zum Layering verwenden,
- die Audio-Spuren normal mischen, bearbeiten, freezen etc.

## Workflow-Empfehlung

1. Fieldrec aufnehmen, schneiden, klassifizieren (V95/V95.2).
2. Slices selektieren, V105 (Adaptive Sample Engine) ausführen.
3. Permissions/Mode mit V106 setzen.
4. V108 (Artist+Tempo) und V109 (Taktart/Meter) konfigurieren.
5. V107 (BeatEngine) ausführen → MIDI-Beat-Item erzeugen.
6. MIDI-Beat-Item selektieren.
7. `DF95_V110_FieldrecBeat_RenderAudioFromSlices.lua` ausführen:
   - Audio-Beat-Spuren werden erzeugt.

## Status

V110 ist ein prototypischer, aber gut abgegrenzter Schritt in Richtung
„echter Audio-Beat“ aus Fieldrec:

- Es nutzt GUID-Listen aus V105 und das Notenlayout von V107.
- Der Fokus liegt auf Nachvollziehbarkeit & Transparenz
  (kein Pitch-Warpen, keine komplizierten Variationen).
- Zukünftige Versionen (V111+) könnten:
  - Microvarianten (Pitch/Offset),
  - Layering (z.B. 2–3 Slices pro Hit),
  - direkte RS5k-Zonensteuerung hinzufügen.

