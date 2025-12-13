# DF95 V106 – Adaptive Beat Permission Panel

V106 erweitert das DF95-System um eine explizite "Permission-Layer" für
Artist-Beats und Euclid-Patterns auf Basis der Adaptive Sample Engine (V105).

Ziel:
- Keine automatische Vollautomatik.
- Du entscheidest explizit, ob:
  - fehlende Samples rekonstruiert werden dürfen,
  - virtuelle Duplikate erlaubt sind,
  - ein vollständiger Artist-Beat versucht werden darf,
  - oder nur ein Minimal-Beat aus dem vorhandenen Material erzeugt werden soll.

## Neues Script

- `Scripts/IFLS/DF95/ReampSuite/DF95_V106_AdaptiveBeat_PermissionPanel.lua`

## Funktionsweise

### 1. Adaptive Sample Info anzeigen (V105)

- V106 liest die von V105 erzeugten ExtStates:

  - `DF95_ADAPTIVE/KICK_REAL_COUNT`
  - `DF95_ADAPTIVE/SNARE_REAL_COUNT`
  - `DF95_ADAPTIVE/HAT_REAL_COUNT`
  - `DF95_ADAPTIVE/PERC_REAL_COUNT`
  - `DF95_ADAPTIVE/OTHER_COUNT`

  - `DF95_ADAPTIVE/KICK_FALLBACK`
  - `DF95_ADAPTIVE/SNARE_FALLBACK`
  - `DF95_ADAPTIVE/HAT_FALLBACK`
  - `DF95_ADAPTIVE/PERC_FALLBACK`

  - `DF95_ADAPTIVE/KICK_VIRTUAL_COUNT`
  - `DF95_ADAPTIVE/SNARE_VIRTUAL_COUNT`
  - `DF95_ADAPTIVE/HAT_VIRTUAL_COUNT`
  - `DF95_ADAPTIVE/PERC_VIRTUAL_COUNT`

- Im Panel wird eine Tabelle angezeigt, aus der du ablesen kannst:
  - wie viele reale Slices es pro Kategorie gibt,
  - welche Fallbacks V105 vorgeschlagen hat,
  - wie viele "virtuelle Duplikate" vorgesehen sind.

- Wenn noch keine V105-Daten vorhanden sind:
  - zeigt V106 einen Hinweis, zuerst
    `DF95_V105_AdaptiveSampleEngine_FieldrecKit.lua`
    auszuführen.

### 2. Permission / Policy Layer

Im Panel kannst du einstellen:

- **Kick rekonstruieren** (wenn keine / zu wenige Kicks vorhanden sind)
- **Snare rekonstruieren** (aus Perc/Hat/FX)
- **Hat rekonstruieren** (aus Perc/Noise etc.)
- **Virtuelle Duplikate verwenden**
  - z.B. aus 1 Kick rechnerisch 4 Varianten machen (Mikrovariationen).

Außerdem:

- **Bevorzugter Beat-Typ:**
  - *Minimal Beat*:
    - arbeitet möglichst nur mit vorhandenem Material,
    - Rekonstruktion & Duplikate optional deaktiviert.
  - *Voller Beat*:
    - darf Rekonstruktion & Duplikate nutzen,
    - Ziel: möglichst "kompletter" Artist-Beat, selbst bei Lücken.

Diese Einstellungen werden gespeichert in:

- Section: `DF95_ADAPTIVE_CONFIG`
  - `ALLOW_RECONSTRUCT_KICK`
  - `ALLOW_RECONSTRUCT_SNARE`
  - `ALLOW_RECONSTRUCT_HAT`
  - `ALLOW_VIRTUAL_DUPES`
  - `PREFER_MINIMAL_BEAT`
  - `PREFER_FULL_BEAT`

### 3. Aktionen – nichts passiert ohne deinen Klick

Unter "Aktionen" hast du Buttons:

- **"Policy speichern (ohne Beat erzeugen)"**
  - schreibt nur `DF95_ADAPTIVE_CONFIG/*`,
  - erzeugt kein MIDI, kein Audio.

- **"Minimalen Artist-Beat (V102) erzeugen"**
  - setzt `PREFER_MINIMAL_BEAT = 1`, `PREFER_FULL_BEAT = 0`,
  - speichert aktuelle Rekonstruktions-Flags,
  - ruft `DF95_V102_Fieldrec_ArtistStyleBeatEngine_MIDI_MultiArtist.lua` auf.

- **"Vollständigen Artist-Beat (V102) zulassen & erzeugen"**
  - setzt `PREFER_FULL_BEAT = 1`, `PREFER_MINIMAL_BEAT = 0`,
  - aktiviert alle Rekonstruktions-Flags (Kick/Snare/Hat + Duplikate),
  - speichert diese Policy,
  - ruft `DF95_V102_Fieldrec_ArtistStyleBeatEngine_MIDI_MultiArtist.lua` auf.

- **"Nur Euclid Multi-Lane Pattern (V104) öffnen"**
  - ruft `DF95_V104_ArtistStyle_EuclidControlPanel_MultiLane.lua` auf,
  - ändert die Policy nicht.

### 4. Wichtig: Was V106 NOCH NICHT tut

- V106 erzeugt selbst noch keine Audio-Duplikate, keine RS5k-Instanzen,
  keine direkten Sample-Zuweisungen.
- Es baut die **Policy-Ebene** und den **Workflow**:
  - du siehst, was V105 erkannt hat,
  - du definierst, was die Engine tun darf,
  - du triggerst bewusst V102/V104.

Ziel ist, spätere Versionen (V107+) darauf aufzubauen:

- z.B. eine BeatEngine, die:
  - `DF95_ADAPTIVE/*` und `DF95_ADAPTIVE_CONFIG/*` liest,
  - echte Item-Duplikate / Microvarianten anlegt,
  - Kick/Snare/Hat/FX-Layer audioseitig im Arrange aufbaut.

## Typischer Workflow

1. Fieldrec aufnehmen, slicen & klassifizieren (V95/V95.2).
2. Alle relevanten Slices selektieren.
3. `DF95_V105_AdaptiveSampleEngine_FieldrecKit.lua` ausführen.
4. `DF95_V106_AdaptiveBeat_PermissionPanel.lua` starten:
   - Adaptive-Übersicht ansehen.
   - Erlauben / verbieten, was die Engine tun darf.
   - Entscheidung treffen: Minimaler Beat, Voller Beat oder nur Euclid.
5. V102/V104 wie gewohnt nutzen, wobei künftige Versionen
   dein Policy-Layer berücksichtigen können.

