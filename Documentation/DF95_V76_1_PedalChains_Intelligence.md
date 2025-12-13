
# DF95 V76.1 – PedalChains Intelligence Layer

Dieses Add-on erweitert dein bestehendes DF95-/ReampSuite-Setup um eine
intelligente Auswahllogik für die IDM-PedalChains aus
`DF95_ReampSuite_PedalChains.lua`.

---

## Inhalt

- `Scripts/IFLS/DF95/DF95_V76_SuperPipeline.lua`
  - aktualisierte Version (1.1)
  - nutzt optional die PedalChains-Intelligenz

- `Scripts/IFLS/DF95/ReampSuite/DF95_ReampSuite_PedalChains_Intelligence.lua`
  - Modul, das:
    - Tracknamen analysiert (Kick/Snare/Lead/FX/etc.)
    - versucht, eine passende Chain aus `M.chains` zu wählen
    - ExtStates in `DF95_REAMP/*` setzt
    - optional Tracknamen mit `[PC:<Key>]` taggt

---

## Wie es funktioniert

### 1. V76 SuperPipeline (Version 1.1)

`DF95_V76_SuperPipeline.lua` arbeitet wie bisher:

- Fieldrec/Dialog/FX-Tracks → `DF95_V72_SuperPipeline.lua`
- Reamp-/DI-/Pedal-Tracks → `DF95_ReampSuite_Router.lua`

Neu in V76.1:

- Vor dem Aufruf des ReampSuite-Routers versucht das Script,
  `DF95_ReampSuite_PedalChains_Intelligence.lua` zu laden.
- Wenn das Modul vorhanden ist, wird `auto_assign_for_tracks(...)`
  aufgerufen, um **automatisch eine PedalChain zu wählen** und
  in `DF95_REAMP/PEDAL_CHAIN_KEY` zu hinterlegen.
- Wenn kein Modul vorhanden ist oder keine geeignete Chain gefunden
  wird, fällt V76 auf die alte, einfache Heuristik zurück
  (Trackname enthält `idm` → `IDM_GlitchPerc`).

### 2. PedalChains Intelligence Modul

`DF95_ReampSuite_PedalChains_Intelligence.lua`:

- lädt `DF95_ReampSuite_PedalChains.lua` und liest `M.chains`
- baut eine interne Liste mit Key, Name, Use-Case
- analysiert Tracknamen:

  - `kick`, `snare`, `clap`, `hat`, `perc`, `drum`
  - `lead`, `pad`, `bass`, `vocal`
  - `fx`, `impact`, `hit`, `noise`, `whoosh`, `sweep`, `rise`
  - `idm`, `glitch`, `chip`, `8bit`, `pitch`, `warp`
  - vorhandene `[PC:<KEY>]`-Tags werden respektiert und direkt übernommen

- bewertet jede Chain anhand der Textbeschreibung:

  - Treffer auf `glitch`, `perc`, `drums`, `lead`, `pitch`, `formant`,
    `noise`, `chip`, `8-bit` etc. erhöhen den Score.
  - die Chain mit dem höchsten Score wird ausgewählt.

- setzt optional:

  - `DF95_REAMP/PEDAL_CHAIN_KEY`
  - `DF95_REAMP/PEDAL_CHAIN_NAME`
  - `DF95_REAMP/PEDAL_CHAIN_DESC`

- kann optional Tracknamen um `[PC:<Key>]` ergänzen.

---

## Verwendung

### A) Vollautomatisch über V76 SuperPipeline

1. Dieses Add-on ins DF95-Repo kopieren:
   - `Scripts/IFLS/DF95/DF95_V76_SuperPipeline.lua` **(überschreibt die frühere V76-Version)**.
   - `Scripts/IFLS/DF95/ReampSuite/DF95_ReampSuite_PedalChains_Intelligence.lua`

2. REAPER starten, Scripts neu scannen (oder Projektscripts re-laden).

3. In deiner V72/V76-Reamp-Toolbar:
   - Button `DF95_V76_SuperPipeline` beibehalten.

4. Workflow:
   - Reamp-Kandidaten-Tracks auswählen (z. B. `Snare_Glitch`, `Lead_IDM`, `FX_ChipNoise`)
   - `V76 SuperPipeline` starten
   - SuperPipeline:
     - erkennt Reamp-Tracks
     - ruft PedalChains-Intelligence auf → Chain wird vorgeschlagen
     - übergibt an ReampSuite-Router → Routing + Profil

### B) Optional als eigenständige Action

Du kannst zusätzlich ein kleines Wrapper-Script bauen, z. B.:

```lua
-- DF95_ReampSuite_PedalChains_AutoAssign_Selected.lua
local r = reaper

local function df95_root()
  local sep = package.config:sub(1,1)
  local res = r.GetResourcePath()
  return (res .. sep .. "Scripts" .. sep .. "IfeelLikeSnow" .. sep .. "DF95" .. sep):gsub("\\","/")
end

local ok, intel = pcall(dofile, df95_root() .. "ReampSuite/DF95_ReampSuite_PedalChains_Intelligence.lua")
if not ok or type(intel) ~= "table" then
  r.ShowMessageBox("Konnte PedalChains_Intelligence nicht laden.", "DF95", 0)
  return
end

local tracks = {}
local cnt = r.CountSelectedTracks(0)
for i = 0, cnt-1 do
  tracks[#tracks+1] = r.GetSelectedTrack(0, i)
end

if #tracks == 0 then
  r.ShowMessageBox("Keine Tracks selektiert.", "DF95", 0)
  return
end

intel.auto_assign_for_tracks(tracks, {
  tag_tracks   = true,
  set_extstate = true,
  verbose      = true,
})
```

Dann kannst du:

- beliebige Tracks selektieren
- die Action ausführen
- automatisch passende `[PC:<Key>]`-Tags + ExtStates setzen.

---

## Kompatibilität

- Überschreibt nur `DF95_V76_SuperPipeline.lua` – der Rest deines DF95-Repos bleibt unverändert.
- Nutzt ausschließlich öffentliche Strukturen aus `DF95_ReampSuite_PedalChains.lua` (`M.chains`).
- Wenn das Modul nicht geladen werden kann, bleibt das Verhalten wie in V76 (ohne .1).

---

Viel Spaß mit der ersten „intelligenten“ IDM-PedalChain-Automatik im DF95-Ökosystem 🚀
