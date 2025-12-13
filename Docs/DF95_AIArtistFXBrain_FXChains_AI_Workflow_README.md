# DF95 AI ArtistFXBrain – FXChains AI Workflow

Dieses Dokument beschreibt das komplette **AI-FXChains-System** rund um:

- `DF95_AI_ArtistFXBrain_ImGui.lua`
- `DF95_FXChains_Index_Builder.lua`
- `DF95_FXChains_Index_Enricher.lua`
- `DF95_AI_FXChain_From_AIResult.lua`
- `DF95_AI_FXChain_FullAuto_From_AIResult.lua`
- `DF95_AI_FXChain_FullAuto_TrackSelect.lua`
- `DF95_AI_FXChain_BatchRequest_FromSelection.lua`
- `DF95_AI_FXMacro_Apply_From_AIResult.lua`

und die dazugehörigen JSON-Dateien unter `Data/DF95/`.

---

## 1. Überblick: Architektur

### 1.1 Ziel

Das System verbindet **Reaper FXChains** mit einer externen **AI-Engine**:

1. FXChains unter `FXChains/DF95/**` werden indexiert → `fxchains_index.json`
2. Der Index wird mit Profil-Daten angereichert (Style, Intensity, UCS-Tags, CPU, …)
3. Reaper/DF95 erzeugt aus der aktuellen Selektion **AI-Requests** (`ai_fxchains_batch_request.json`)
4. Ein externer AIWorker liest diese Requests und erzeugt:
   - `ai_fxchains_result.json` (FXChain-Empfehlungen)
   - optional `ai_fxmacros_result.json` (Macro-/Shaping-Werte)
5. Reaper/DF95 lädt die empfohlenen FXChains und setzt Macro-Parameter.
6. Das alles wird über das **DF95 AI ArtistFXBrain (ImGui)** zentral bedient.

### 1.2 Haupt-JSON-Dateien

Alle AI-bezogenen JSON-Dateien liegen unter:

- `<REAPER_RESOURCE_PATH>/Data/DF95/`

Relevante Dateien:

- `fxchains_index.json`  
  → Index aller `FXChains/DF95/*.rfxchain`
- `fxchains_index_raw.json`  
  → Backup des ursprünglichen Index (vor Enrichment)
- `ai_fxchains_batch_request.json`  
  → von Reaper erzeugte AI-Requests (Option 6)
- `ai_fxchains_result.json`  
  → AI-Ergebnis: Welche FXChain für welche Situation? (Option 1/3)
- `ai_fxmacros_result.json`  
  → AI-Ergebnis: Macro-Werte für vorhandene FX (Option 7)

---

## 2. FXChain Index: Builder & Enricher

### 2.1 `DF95_FXChains_Index_Builder.lua`

**Pfad:**

- `Scripts/IFLS/DF95/DF95_FXChains_Index_Builder.lua`

**Aufgabe:**

- Scannt rekursiv:

  - `<REAPER_RESOURCE_PATH>/FXChains/DF95/`

- Sucht alle `.rfxchain`-Dateien
- Erzeugt:

  - `<REAPER_RESOURCE_PATH>/Data/DF95/fxchains_index.json`

**Struktur von `fxchains_index.json`:**

```jsonc
{
  "version": "1.0",
  "generated_at": "2025-12-01T12:34:56Z",
  "base_path": "FXChains/DF95",
  "count": 123,
  "fxchains": [
    {
      "id": "SFX_Whoosh_Wide_01",
      "path": "FXChains/DF95/SFX/Whoosh/SFX_Whoosh_Wide_01.rfxchain",
      "filename": "SFX_Whoosh_Wide_01.rfxchain",
      "category": "SFX/Whoosh",
      "tags": ["sfx","whoosh"],
      "roles": ["item"],
      "meta": {
        "created_by": "DF95_FXChains_Index_Builder",
        "version": "1.1"
      }
    }
  ]
}
```

- `id` ist eine Ketten-ID (aus Pfad ohne Extension, Slashes → `_`)
- `path` ist relativ zu `<REAPER_RESOURCE_PATH>`
- `category` ist der Unterordner relativ zu `FXChains/DF95`

### 2.2 `DF95_FXChains_Index_Enricher.lua`

**Pfad:**

- `Scripts/IFLS/DF95/DF95_FXChains_Index_Enricher.lua`

**Aufgabe:**

- Liest `fxchains_index.json`
- Erweitert jeden Eintrag um:

```jsonc
"profile": {
  "artist_id": "SomeArtist",
  "style": "SFX",
  "intensity": 0.8,
  "ucs_tags": ["WHOOSH","SWEETENER"],
  "cpu_cost": 0.6,
  "role_primary": "item"
}
```

- Legt vorher ein Backup an:

  - `fxchains_index_raw.json`

**Empfohlene Reihenfolge:**

1. `DF95_FXChains_Index_Builder.lua`
2. `DF95_FXChains_Index_Enricher.lua`

Beide Actions können direkt aus dem **FXBrain-ImGui** gestartet werden.

---

## 3. FXBrain UI (`DF95_AI_ArtistFXBrain_ImGui.lua`)

**Pfad:**

- `Scripts/IFLS/DF95/DF95_AI_ArtistFXBrain_ImGui.lua`

**Funktionen:**

- Lädt und visualisiert `fxchains_index.json`
- Zeigt Chains nach Artist/Style/Kategorien
- Schreibt den absoluten `.rfxchain`-Pfad in eine ExtState:

  - Section: `DF95`
  - Key: `ApplyFXChain_Path`

- Stellt Buttons bereit für:

  - `Build FXChain Index` (Index-Builder Action)
  - `Enrich FXChain Index` (Enricher Action)
  - `Build AI BatchRequest (Selection)` (Option 6)
  - `Apply AI FXMacros` (Option 7)
  - `FullAuto: AI FXChain Apply` (Option 3)
  - `Selftest: DF95 AI FX Pipeline`

### 3.1 Action-ID-Konfiguration im ImGui

Im Script gibt es mehrere Konfig-Blöcke:

```lua
-- FullAuto-Action (Option 3)
local FULLAUTO_ACTION_COMMAND_ID = ""  -- Command-ID von DF95_AI_FXChain_FullAuto_From_AIResult.lua

-- Index/Enricher
local INDEX_BUILDER_ACTION_COMMAND_ID  = ""  -- Command-ID von DF95_FXChains_Index_Builder.lua
local INDEX_ENRICHER_ACTION_COMMAND_ID = ""  -- Command-ID von DF95_FXChains_Index_Enricher.lua

-- BatchRequest / FXMacros
local BATCHREQUEST_ACTION_COMMAND_ID = ""  -- Command-ID von DF95_AI_FXChain_BatchRequest_FromSelection.lua
local FXMACROS_ACTION_COMMAND_ID    = ""  -- Command-ID von DF95_AI_FXMacro_Apply_From_AIResult.lua
```

**So füllst du sie:**

1. Reaper → `Actions`
2. Script suchen → Rechtsklick → `Copy selected action command ID`
3. Command-ID im ImGui-Script einsetzen
4. Script speichern, in Reaper neu laden

---

## 4. AI-FXChain Recommendation (Option 1 & 3)

### 4.1 `DF95_AI_FXChain_From_AIResult.lua` (Option 1)

**Pfad:**

- `Scripts/IFLS/DF95/DF95_AI_FXChain_From_AIResult.lua`

**Aufgabe:**

- Liest:

  - `Data/DF95/fxchains_index.json`
  - `Data/DF95/ai_fxchains_result.json`

- Erwartetes Format von `ai_fxchains_result.json`:

```jsonc
{
  "mode": "fxchain_recommendation",
  "recommendations": [
    {
      "fxchain_id": "SFX_Whoosh_Wide_01",
      "confidence": 0.94
    }
  ]
}
```

- Wählt die Empfehlung mit der höchsten `confidence`
- Sucht `fxchain_id` im Index
- Resolvt zu einem absoluten Pfad und schreibt:

  - ExtState: `DF95 / ApplyFXChain_Path = <absoluter rfxchain Pfad>`

### 4.2 `DF95_AI_ApplyFXChain_FromExtState.lua`

**Pfad:**

- `Scripts/IFLS/DF95/DF95_AI_ApplyFXChain_FromExtState.lua`

**Aufgabe:**

- Liest `ApplyFXChain_Path` aus ExtState (`DF95`/`ApplyFXChain_Path`)
- Lädt die `.rfxchain` auf alle selektierten Tracks
- Nutzt Reaper-Track-State-Chunks (kein direkter File-Parse nötig)

### 4.3 `DF95_AI_FXChain_FullAuto_From_AIResult.lua` (Option 3)

**Pfad:**

- `Scripts/IFLS/DF95/DF95_AI_FXChain_FullAuto_From_AIResult.lua`

**Aufgabe:**

- Kombiniert Resolver + Apply in einer Action:
  - liest Index und `ai_fxchains_result.json`
  - resolved Chain
  - setzt ExtState
  - ruft `DF95_AI_ApplyFXChain_FromExtState` auf

**Konfiguration:**

```lua
local APPLY_ACTION_COMMAND_ID = ""  -- Command-ID von DF95_AI_ApplyFXChain_FromExtState.lua
```

- Ohne korrekt gesetzte ID kann FullAuto seine Apply-Action nicht starten.

---

## 5. Track-Selection Watcher (Option 5)

### 5.1 `DF95_AI_FXChain_FullAuto_TrackSelect.lua`

**Pfad:**

- `Scripts/IFLS/DF95/DF95_AI_FXChain_FullAuto_TrackSelect.lua`

**Aufgabe:**

- Defer-Loop, der die Track-Selektion beobachtet
- Wenn sich die Selektion ändert, wird die FullAuto-Action gestartet (Option 3)

**Konfiguration:**

```lua
local FULLAUTO_ACTION_COMMAND_ID = ""  -- Command-ID von DF95_AI_FXChain_FullAuto_From_AIResult.lua
local MIN_TRIGGER_INTERVAL = 0.5       -- Sekunden
local ONLY_SINGLE_TRACK    = false     -- true => nur bei genau einer Spur
local REQUIRE_NAME_MARKER  = ""        -- z.B. "[AI]" für markierte Tracks
```

**Typische Nutzung:**

- Script einmal starten (z.B. Toolbar-Button „AI Follow Selection“)
- AI-Worker hat `ai_fxchains_result.json` aktualisiert
- Bei Auswahl neuer Tracks → FullAuto wird automatisch aufgerufen

---

## 6. BatchRequest (Option 6)

### 6.1 `DF95_AI_FXChain_BatchRequest_FromSelection.lua`

**Pfad:**

- `Scripts/IFLS/DF95/DF95_AI_FXChain_BatchRequest_FromSelection.lua`

**Aufgabe:**

- Baut einen AI-Request aus aktueller Auswahl:

  - Wenn **Items selektiert** → über Items
  - Sonst, wenn **Tracks selektiert** → über Tracks

- Erzeugt:

  - `Data/DF95/ai_fxchains_batch_request.json`

**Beispiel-Struktur:**

```jsonc
{
  "version": "1.0",
  "generated_at": "2025-12-01T12:34:56Z",
  "project_name": "MyProject.RPP",
  "project_path": "C:/Projects/MyProject",
  "selection_mode": "items",
  "entry_count": 2,
  "entries": [
    {
      "id": 1,
      "entry_type": "item",
      "track_name": "SFX Whoosh",
      "track_guid": "{...}",
      "item_guid": "{...}",
      "item_position": 12.34,
      "item_length": 1.23,
      "take_name": "whoosh_fast_01",
      "role": "SFX",
      "ucs_tags": ["WHOOSH","SWEETENER"]
    }
  ]
}
```

**Zweck:**

- Diese Datei ist das Input-Format für deinen externen AIWorker:
  - Eintrag pro Item/Track
  - AI entscheidet pro Entry passende `fxchain_id` und/oder Macro-Werte

---

## 7. FXMacros (Option 7)

### 7.1 `DF95_AI_FXMacro_Apply_From_AIResult.lua`

**Pfad:**

- `Scripts/IFLS/DF95/DF95_AI_FXMacro_Apply_From_AIResult.lua`

**Aufgabe:**

- Liest:

  - `Data/DF95/ai_fxmacros_result.json`

- Erwartete Struktur:

```jsonc
{
  "version": "1.0",
  "targets": [
    {
      "track_guid": "{...}",
      "fx_name": "ReaComp",
      "macros": {
        "Punch": 0.8,
        "Glue": 0.4
      }
    }
  ]
}
```

- Für jedes `target`:
  - Spur via `track_guid` finden
  - FX via Name-/Substring-Match (`fx_name`) finden
  - Macro-Werte (`0.0`–`1.0`) über `FX_MACRO_MAP` in konkrete Parameterwerte übersetzen
  - Parameter mit `TrackFX_SetParam` setzen

**Macro-Mapping:**

Im Script findet sich z.B.:

```lua
FX_MACRO_MAP["ReaComp"] = {
  Punch = {
    { param = 1, min = 1.5,  max = 6.0  },   -- Ratio
    { param = 2, min = 0.0005, max = 0.02 }, -- Attack
  },
  Glue = {
    { param = 3, min = -30.0, max = -6.0 },  -- Threshold
    { param = 4, min = 0.1,   max = 0.5  },  -- Release
  },
}

FX_MACRO_MAP["Saturation"] = {
  Color = {
    { param = 0, min = 0.0, max = 1.0 },      -- Drive / Color
  },
}
```

- **Wichtig:** `FX_MACRO_MAP` ist bewusst minimal und soll projekt-/chain-spezifisch erweitert werden.

---

## 8. Typische End-to-End Pipelines

### 8.1 Manuelle FXChain-Empfehlung

1. `Build FXChain Index` im FXBrain-UI
2. `Enrich FXChain Index`
3. Externer AIWorker erzeugt `ai_fxchains_result.json`
4. In Reaper:
   - Tracks selektieren
   - `FullAuto: AI FXChain Apply` im FXBrain-UI klicken
   - (oder `DF95_AI_FXChain_From_AIResult.lua` + `DF95_AI_ApplyFXChain_FromExtState.lua` getrennt nutzen)

### 8.2 Auto-Follow mit Track-Selection

1. Wie oben Index + Enricher aufbauen
2. `DF95_AI_FXChain_FullAuto_From_AIResult.lua` als Action konfigurieren
3. `DF95_AI_FXChain_FullAuto_TrackSelect.lua` starten
4. AIWorker aktualisiert regelmäßig `ai_fxchains_result.json`
5. Du klickst dich durch Tracks → AI-FXChains werden automatisch angewendet

### 8.3 Batch-basiertes AI-Mastering / Scene-Processing

1. Items/Tracks selektieren
2. Im FXBrain-UI: `Build AI BatchRequest (Selection)`
3. AIWorker verarbeitet `ai_fxchains_batch_request.json` und erzeugt:
   - `ai_fxchains_result.json` (oder mehrere Result-Dateien)
   - optional `ai_fxmacros_result.json`
4. In Reaper:
   - `FullAuto` ausführen (für Chains)
   - `Apply AI FXMacros` ausführen (für finetuning)

---

## 9. Externer AIWorker: Pfade & Verantwortung

- Alle AI-Input/Output-Dateien liegen unter: `Data/DF95/`
- Reaper/DF95 schreibt:

  - `fxchains_index.json`, `fxchains_index_raw.json`
  - `ai_fxchains_batch_request.json`

- Externer AIWorker ist dafür verantwortlich:

  - `ai_fxchains_result.json` zu erzeugen
  - optional `ai_fxmacros_result.json` zu erzeugen
  - sich an die hier dokumentierten JSON-Schemata zu halten

---

## 10. TODO / Erweiterungsideen

- Erweiterte Artist-/Style-Profile im Index (z.B. mehrere Artist-IDs, Versioning)
- Mehr vordefinierte `FX_MACRO_MAP`-Einträge für häufige Plugin-Ketten
- Zusätzliche Buttons im FXBrain:

  - TrackSelect-Watcher (Start/Stop)
  - Logging-Panel für AI-Events

- Erweiterte Security/Validation für AI-Outputs (Bounds-Clamping, Sanity-Checks etc.)

Dieses Dokument soll als Referenz dienen, um AIWorker, DF95-Tools und Reaper-Scripts
sauber miteinander zu verdrahten und langfristig kompatibel zu halten.
