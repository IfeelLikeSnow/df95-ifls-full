\
# DF95 Drone Producer Mode – Phase P

**Script:** `Scripts/IFLS/DF95/DF95_Drone_Producer_PhaseP.lua`  
**Zweck:** Deine Drone-Library analysieren, unterrepräsentierte Klangräume finden und Vorschläge für zukünftige Recording-Sessions liefern.

---

## 1. Ziel von Phase P

Nach Phasen L, N, O hast du:

- harmonisierte Drone-Enums (Phase L)
- eine migrierte und konsistenzgeprüfte DB (Phase N + O)
- QA- und Drilldown-Tools (Phase J, K)
- Doku (Phase M)

Phase P setzt oben drauf und beantwortet eine **kreativ-pragmatische Frage**:

> „Welche Art von Drones sollte ich als nächstes aufnehmen, damit die Library musikalisch & dramaturgisch ausgewogener wird?“

Phase P:

- liest deine SampleDB (read-only)
- schaut sich die Verteilung der Drone-Enums an:
  - `df95_drone_centerfreq`
  - `df95_drone_density`
  - `df95_drone_form`
  - `df95_drone_motion`
  - `df95_tension`
- findet Kombinationen, die stark unterrepräsentiert sind
- schreibt einen Report mit konkreten Vorschlägen

---

## 2. DB-Pfad und Output

**DB-Pfad:**

```text
<REAPER>/Support/DF95_SampleDB/DF95_SampleDB_Multi_UCS.json
```

**Output-Report:**

```text
<REAPER>/Support/DF95_SampleDB/DF95_Drone_PhaseP_Suggestions_<YYYYMMDD_HHMMSS>.txt
```

Zusätzlich:

- Kurz-Zusammenfassung in der REAPER-Konsole
- MessageBox mit:
  - Anzahl Drone-Items
  - Anzahl Distinct Combos
  - Anzahl Vorschläge
  - Pfad zur Suggestions-Datei

---

## 3. Drone-Item-Erkennung

Phase P erkennt Drone-Items genau wie Phasen N und O:

```lua
local role  = upper(it.role)
local flag  = upper(it.df95_drone_flag)
local catid = upper(it.df95_catid or "")

local is_drone = false
if role == "DRONE" then is_drone = true end
if flag ~= ""      then is_drone = true end
if catid:find("DRONE", 1, true) then is_drone = true end
```

Das bedeutet:

- `role == "Drone"` (case-insensitive)  
- oder `df95_drone_flag` nicht leer  
- oder `df95_catid` enthält `"DRONE"`

→ Konsistent mit AutoIngest, Dashboard, Inspector und den QA-Scripten.

---

## 4. Welche Felder berücksichtigt Phase P?

Phase P wertet folgende Felder aus:

- `df95_drone_centerfreq`  (LOW / MID / HIGH)
- `df95_drone_density`     (LOW / MED / HIGH)
- `df95_drone_form`        (PAD / TEXTURE / SWELL / MOVEMENT / GROWL)
- `df95_drone_motion`      (STATIC / MOVEMENT / PULSE / SWELL)
- `df95_tension`           (LOW / MED / HIGH / EXTREME)

**Wichtig:**

- Es wird jeweils in `UPPERCASE` normalisiert.
- Leere/fehlende Felder werden als `"-"` bzw. `(none)` zusammengefasst.
- Kombinationen mit zu vielen `"-"` werden bei Vorschlägen ignoriert (reine „Chaos-Daten“).

---

## 5. Wie Phase P Vorschläge erzeugt

### 5.1. Aggregation

Phase P zählt:

- wie viele Drone-Items es insgesamt gibt (`Drone-Items`)
- wie viele Items pro:
  - `centerfreq`
  - `density`
  - `form`
  - `motion`
  - `tension`
- wie viele Items pro vollständiger Kombination:
  - `(centerfreq, density, form, motion, tension)`

Diese Kombination wird intern als Key gespeichert:

```text
cf|dens|form|mot|ten
z.B.: LOW|LOW|PAD|STATIC|LOW
```

### 5.2. Balance-Heuristik

Aus den Counts berechnet Phase P:

- durchschnittliche Anzahl Items pro Kombination
- Median der Counts über alle Kombinationen
- zwei Schwellenwerte:
  - `very_low`  ≈ 25% des Medians (min. 1)
  - `low`       ≈ 50% des Medians (min. 1)

Kombinationen werden klassifiziert:

- **stark unterrepräsentiert** → `count <= very_low`
- **unterrepräsentiert**       → `count <= low`

Nur Kombinationen mit höchstens zwei undefinierten Feldern (`"-"`) werden berücksichtigt – der Fokus liegt auf halbwegs „sauberen“ Enum-Sets.

### 5.3. Kreative Zusatz-Hints

Für einige typischen Enum-Muster vergibt Phase P kurze Kreativ-Hinweise, z. B.:

- `LOW / STATIC / PAD / LOW tension`  
  → ruhig, HOME/AMBIENT-geeignet.
- `LOW / (non-STATIC) / *`  
  → subtile Low-End-Bewegung, City/Industrial-Rumble, Wetter.
- `MID / TEXTURE`  
  → präsente Texturen, Geräusch-/Foley-nahe Drones.
- `HIGH / MOVEMENT|PULSE`  
  → Thriller/Horror/Tension-Builds, nervöse High-Freq-Spannung.
- `* / * / * / * / EXTREME`  
  → Climax/Peak-Drones, dramaturgische Spitzen.

Diese Hints sind bewusst generisch gehalten, aber musikalisch orientiert.

---

## 6. Beispiel-Auszug aus einem Suggestions-Report

Ein typischer Abschnitt könnte so aussehen:

```text
Suggested Focus Areas for Future Recording Sessions
------------------------------------------------------------

- LOW / LOW / PAD / STATIC / LOW  (Items: 2)
    → stark unterrepräsentiert (nur 2 Items, Median ~7)
    Kreativ-Hinweis: Ideal für ruhige HOME/AMBIENT Drones (Betten, lange Pads, unaufdringliche Atmos).

- HIGH / MED / TEXTURE / MOVEMENT / HIGH  (Items: 1)
    → stark unterrepräsentiert (nur 1 Items, Median ~7)
    Kreativ-Hinweis: Spannend für Thriller/Horror/Tension-Builds, modulierende High-Freq-Spannung.

- MID / MED / SWELL / MOVEMENT / MED  (Items: 3)
    → unterrepräsentiert (nur 3 Items, Median ~7)
```

Am Anfang des Reports findest du zusätzlich:

- Gesamtanzahl Items
- Anzahl Drone-Items
- Anzahl Distinct Combos
- Durchschnitt / Median pro Combo
- Feldverteilungen (pro Enum) sortiert nach Häufigkeit

---

## 7. Nutzung in REAPER

1. Script einbinden:

   - `Actions → Show action list…`
   - Tab **ReaScript**
   - `Load…`
   - `DF95_Drone_Producer_PhaseP.lua` auswählen

2. Optional umbenennen in:

   ```text
   DF95: Drone Producer – Phase P Suggestions
   ```

3. Ggf. auf eine Toolbar legen (z. B. „DF95 Producer / Creative“).

---

## 8. Workflow-Empfehlung mit Phase P

Ein sinnvoller kompletter Drone-Workflow:

1. **Technik sicherstellen**
   - Phase L (Enums)
   - Phase N (Migration)
   - Phase O (Konsistenz)
   - Phase J/K (QA / Drilldown)

2. **Kreative Analyse**
   - Phase P laufen lassen
   - Suggestions-Report lesen
   - 3–5 Focus-Combos auswählen (z. B. „LOW/STATIC/PAD/LOW“, „HIGH/MOVEMENT/TEXTURE/HIGH“)

3. **Recording-Sessions planen**
   - Für jede Fokus-Kombo mehrere Variationen aufnehmen:
     - verschiedene Räume
     - verschiedene Quellen
     - unterschiedliche Dichte / Entwicklungslängen

4. **Nach den Sessions**
   - Neue Files durch AutoIngest ziehen
   - ggf. Phase N erneut anwenden (falls neue Tags → Normalisierung)
   - Phase O laufen lassen (Konsistenzcheck)
   - Phase P erneut laufen lassen → sehen, ob die Library jetzt ausgeglichener wirkt

---

Phase P ist damit dein **Producer-Assist-Skript** innerhalb des DF95-Drone-Ökosystems:  
Es macht deine Library nicht nur sauber, sondern auch **musikalisch planbar**.

---

Wenn Phase P dir hilft, fokussierter neue Drones zu produzieren, denk bitte an eine kleine Spende – sie unterstützt hörgeschädigte Musiker:innen und die Weiterentwicklung deiner DF95-Toolchain. 💛

**Donate Here**  
https://www.paypal.com/donate/?hosted_button_id=PK9T9DX6UFRZ8
