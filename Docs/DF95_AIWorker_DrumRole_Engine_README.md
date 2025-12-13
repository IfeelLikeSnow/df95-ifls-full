# DF95 AIWorker Drum-Role Engine (V1)

Dieses Modul beschreibt, wie DF95 AIWorker mit Drum-Rollen umgehen soll – speziell für
Fieldrec/Beat-Engines (z.B. V133 AIBeat Soundscape Generator).

## 1. Lua-Seite (REAPER / DF95)

### 1.1 Fieldrec → AIWorker Bridge

`DF95_Fieldrec_AIWorker_Bridge_FromProject.lua` erzeugt einen Job mit:

- `worker_mode = "material"`
- `requested_tasks` enthält nun zusätzlich:

  - `classify_drum_role`

Der Job liegt in:

- `<REAPER>/Support/DF95_AIWorker/Jobs/DF95_AIWorker_Job_Fieldrec_*.json`

### 1.2 ApplyToItems

`DF95_Fieldrec_AIWorker_ApplyToItems.lua` wertet ein Result-JSON aus und erwartet optional:

- `drum_role` (String)
- `drum_confidence` (Number, 0.0–1.0 optional)

Wenn `drum_role` vorhanden ist:

- wird dieser Wert direkt als Rolle genutzt (`KICK/SNARE/HIHAT/TOM/PERC/FX/AMBIENCE/...`)
- Items werden entsprechend eingefärbt
- Take-Namen werden angepasst
- AI-Block in den Item Notes enthält `role=...`

Wenn `drum_role` **nicht** vorhanden ist:

- greift eine lokale Heuristik auf Basis von:
  - `material`, `instrument`, `ai_tags`

### 1.3 Beat-Engine V133

`DF95_V133_AIBeat_Soundscape_Generator.lua` nutzt nun:

- `AI_BEAT_SELECTION_MODE`:

  - `CLASSIC`
  - `AI_FIRST`
  - `AI_WEIGHTED` (für spätere Erweiterung vorbereitet)

- Klassifizierer (Kick/Snare/Hat/Toms/Ride/Crash/Ambience) lesen:

  - `it.drum_role` / `it.df95_role`
  - `it.ai_tags`, `it.ai_labels`, `ai_primary`
  - UCS-Category/Subcategory
  - Dateiname

Damit können Beats deutlich gezielter passende Samples wählen.

## 2. Python-Seite (externer AIWorker)

Beispiel-Skript:

- `Support/DF95_AIWorker/df95_aiworker_drumrole_example.py`

Erwartet:

```bash
python df95_aiworker_drumrole_example.py <job.json> <result.json>
```

### 2.1 Job-Format (Input)

- `version`: `"DF95_AIWorker_UCS_V1"`
- `audio_root`: Basisordner für Audiofiles
- `files`: Liste von Dateien mit z.B.:

  - `rel_path`
  - `full_path` (optional)

- `requested_tasks` enthält `"classify_drum_role"`.

### 2.2 Result-Format (Output)

```jsonc
{
  "version": "DF95_AIWorker_DrumRole_V1",
  "source_job": "...",
  "results": [
    {
      "full_path": "D:/.../Snr_Metal_TightRoom_01.wav",
      "drum_role": "SNARE",
      "drum_confidence": 0.92
    }
  ]
}
```

Weitere Felder (material, instrument, tags, ucs_*) sind erlaubt und werden von
anderen DF95-Skripten genutzt.

## 3. Typischer Workflow

1. Fieldrec-Projekt vorbereiten (Slices etc.).
2. `DF95_Fieldrec_AIWorker_Bridge_FromProject.lua` ausführen → Job.
3. Python-Worker:

   ```bash
   python df95_aiworker_drumrole_example.py Job.json Result.json
   ```

   oder dein eigenes Modell-Skript.

4. `DF95_Fieldrec_AIWorker_ApplyToItems.lua` in REAPER ausführen:
   - Item Notes/Take-Namen/Colours werden gesetzt.
5. `DF95_V133_AIBeat_Soundscape_Generator.lua` nutzen:
   - AI Selection Mode auf `AI_FIRST` oder `AI_WEIGHTED` setzen.

Damit sind Fieldrecordings → AIWorker → Drum-Rolle → Beat-Engine sauber verbunden.


---

## 4. Full Model Mode (DrumRole Engine V2)

Für ernsthafte Einsätze gibt es eine eigene Engine:

- `Support/DF95_AIWorker/df95_aiworker_drumrole_engine.py`
- Optionale Config:
  - `Support/DF95_AIWorker/df95_aiworker_drumrole_config.json`

### 4.1 Backends

In der Config:

```jsonc
{
  "backend": "heuristic", // "heuristic" | "yamnet" | "clap" | "custom"
  "min_confidence": 0.25
}
```

Mögliche Werte:

- `heuristic` – eingebaut, leichtgewichtig (Dateiname-basiert, gut als Fallback)
- `yamnet`   – YAMNet/TFHub-Backend (du bindest dein Modell ein)
- `clap`     – CLAP/AudioCLAP-Embedding + Textprompts
- `custom`   – du gibst ein eigenes Modul/Funktion an, z.B.:

```jsonc
"custom": {
  "module": "my_drum_model",
  "function": "predict_role"
}
```

mit Python:

```python
def predict_role(path: str) -> tuple[str, float]:
    ...
    return "SNARE", 0.93
```

### 4.2 Aufruf

Typischer Call:

```bash
python df95_aiworker_drumrole_engine.py Job_Fieldrec.json Result_DrumRole.json
```

Optional mit eigener Config:

```bash
python df95_aiworker_drumrole_engine.py Job_Fieldrec.json Result_DrumRole.json my_drumrole_config.json
```

### 4.3 Result

Die Engine schreibt ein JSON mit:

```jsonc
{
  "version": "DF95_AIWorker_DrumRole_V2",
  "backend": "heuristic",
  "source_job": "...",
  "results": [
    {
      "full_path": "D:/.../Kick_DeepRoom_01.wav",
      "drum_role": "KICK",
      "drum_confidence": 0.81
    }
  ]
}
```

Das wird von `DF95_Fieldrec_AIWorker_ApplyToItems.lua` gelesen und
direkt an die BeatEngine (V133) weitergereicht.
