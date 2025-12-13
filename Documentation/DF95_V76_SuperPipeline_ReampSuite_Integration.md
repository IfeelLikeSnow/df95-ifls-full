
# DF95 V76 – SuperPipeline ⇄ ReampSuite Integration

Dieses Paket ergänzt dein bestehendes DF95-Setup (V70–V75) um eine neue Integrations-Schicht:

- verbindet **DF95_V72_SuperPipeline.lua** (Fieldrec / AutoMic / Export)
- mit der **DF95 ReampSuite** (Profile, V71 ReampRouter, PedalChains)

Es werden **keine bestehenden Dateien überschrieben**.

---

## Dateien in diesem Paket

- `Scripts/IFLS/DF95/DF95_V76_SuperPipeline.lua`  
  Hauptscript für die Integration zwischen Fieldrec-Flow und ReampSuite.

- `Documentation/DF95_V76_SuperPipeline_ReampSuite_Integration.md`  
  Diese Datei.

---

## Funktionsweise (Kurzfassung)

1. Du selektierst beliebige Tracks (Fieldrec, Dialog, FX, Reamp/DI/Pedals).
2. `DF95_V76_SuperPipeline.lua` teilt die Auswahl in zwei Gruppen:
   - **Fieldrec-Tracks** → gehen wie gehabt an `DF95_V72_SuperPipeline.lua`  
     (über den Namespace `DF95_SUPERPIPELINE/*`)
   - **Reamp-/DI-/Pedal-Tracks** → werden an `DF95_ReampSuite_Router.lua` übergeben  
     (über den Namespace `DF95_REAMP/*`)

### Erkennung von Reamp-Kandidaten

Ein Track gilt als Reamp-Kandidat, wenn der Name (Case-insensitive) eines der folgenden Muster enthält:

- `REAMP`
- `RE-AMP`
- ` DI `
- `_DI`
- `DI_`
- `PEDAL`

Alles andere wird als Fieldrec/Dialog/FX behandelt und an die V72-SuperPipeline weitergereicht.

### Kommunikation mit ReampSuite

Für Reamp-Tracks setzt V76:

- `DF95_REAMP/TRACK_IDS` → CSV-Liste der Tracknummern
- optional `DF95_REAMP/PEDAL_CHAIN_KEY` → heuristisch ermittelter Key (z. B. `IDM_GlitchPerc`)

Anschließend wird `ReampSuite/DF95_ReampSuite_Router.lua` direkt per `dofile(...)` ausgeführt.
Dieser Script:

- lädt `DF95_ReampSuite_Profiles.lua`
- wählt ein Reamp-Profil (UR22 / PreSonus / Zoom F6 / Generic)
- setzt `DF95_REAMP/OUT_CH` und `DF95_REAMP/IN_CH`
- ruft den klassischen `DF95_V71_ReampRouter.lua` auf

Die **PedalChains-GUI** (IDM-Presets) arbeitet weiterhin wie gewohnt im Namespace `DF95_REAMP`
und kann den aktiven PedalChain-Key jederzeit ändern, ohne dass V76 angepasst werden muss.

---

## Installation

1. Dieses Paket **NICHT** einfach über dein gesamtes DF95-Repo entpacken,
   sondern gezielt in deinen REAPER-ResourcePath kopieren:

   - `Scripts/IFLS/DF95/DF95_V76_SuperPipeline.lua`
   - `Documentation/DF95_V76_SuperPipeline_ReampSuite_Integration.md` (optional)

   Dein REAPER-ResourcePath lässt sich über `Options → Show REAPER resource path` öffnen.

2. In REAPER:

   - `Actions → Show action list…`
   - Button `New Action… → Load ReaScript…`
   - `DF95_V76_SuperPipeline.lua` auswählen
   - Script registrieren

3. Optional in Toolbar einbinden:

   - Deine **DF95_V72_SuperPipeline_Reamp_Toolbar** öffnen
   - `Right-Click → Customize toolbar…`
   - `Add…` klicken
   - `DF95_V76_SuperPipeline` auswählen
   - Label z. B. `V76 SuperPipeline (Fieldrec+ReampSuite)` vergeben

Du hast jetzt in derselben Toolbar:

- den alten V72-Entry-Point (falls du ihn weiter nutzen willst)
- den neuen V76-Entry-Point für kombinierte Fieldrec+Reamp-Flows
- die direkten ReampSuite/Latency-Tools aus V71/V75

---

## Anpassbare Stellen

### 1. PedalChain-Heuristik

In `DF95_V76_SuperPipeline.lua` findest du:

```lua
local function guess_pedal_chain_key_for_tracks(tracks)
  local has_idm = false
  for _, tr in ipairs(tracks) do
    local name = get_track_name(tr):lower()
    if name:find("idm") then
      has_idm = true
      break
    end
  end

  if has_idm then
    return "IDM_GlitchPerc"  -- Beispiel-Chain-Key
  end

  return nil
end
```

Passe den Rückgabewert (`"IDM_GlitchPerc"`) an die Keys an,
die du in `DF95_ReampSuite_PedalChains.lua` in `M.chains = { ... }` definiert hast.

Wenn `nil` zurückgegeben wird, wird **kein** PedalChain-Key gesetzt – dann
kannst du per PedalChain-GUI oder MainGUI aktiv auswählen.

### 2. Zukünftige Erweiterungen (optional)

- Du kannst einen zusätzlichen ExtState wie `DF95_REAMP/PROFILE_KEY` einführen
  und im `DF95_ReampSuite_Router.lua` auswerten, um die Profilwahl zu
  automatisieren (kein Popup, wenn das Profil bereits bekannt ist).
- Du kannst einen separaten Script bauen, der nach erfolgreichem Reamping
  die Items auf den ReampReturn-Tracks automatisch basierend auf den
  OFFSETS aus `DF95_V71_LatencyAnalyzer.lua` verschiebt.

Beides ist vollständig kompatibel mit V76 und kann später ergänzt werden,
ohne das hier vorliegende Script zu verändern.

---

## Sicherheit / Kompatibilität

- V76 **überschreibt keine Dateien** – es kommt nur als neues Script dazu.
- Es nutzt ausschließlich die vorhandene DF95-Logik (V70–V75)
  über `dofile(...)` und ExtStates.
- Falls eines der benötigten Basisscripts fehlt oder fehlerhaft ist,
  zeigt V76 eine klare Fehlermeldung mit Pfadangabe an.

---

Viel Spaß beim ersten „echten“ SuperPipeline ⇄ ReampSuite Workflow mit V76 🚀
