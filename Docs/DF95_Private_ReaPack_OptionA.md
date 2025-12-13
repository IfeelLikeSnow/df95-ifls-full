# DF95 – ReaPack Option A (privates Repo) – Setup Guide

Dieses Setup ist **für ein privates “nur ich” Repo** gedacht: du behältst *alle* DF95‑Funktionen/Skripte, bekommst aber Updates über ReaPack statt ZIP‑Copy.

## Zielbild

- Dein DF95 Git‑Repo ist **privat** (GitHub/GitLab o.ä.).
- ReaPack lädt **dein** `index.xml` über eine **Raw-URL** (oder über deinen Git‑Host).
- Updates = `git tag` + `index.xml` Version bump + ReaPack “Synchronize packages”.

ReaPack-Workflow (Import/Synchronize) ist der Standardweg.  
Siehe ReaPack User Guide: “Synchronize packages”.  

## Schritt 1 — Privates Git-Repo vorbereiten

1. Repo privat erstellen (z.B. GitHub **Private Repository**).
2. Deinen DF95-Repo-Root enthält `index.xml` (Modell B: Core + Packs).
3. Commit + Push.

## Schritt 2 — Raw `index.xml` URL ermitteln

Beispiel (GitHub Raw Pattern):

`https://github.com/<USER>/<REPO>/raw/<BRANCH>/index.xml`

oder (gleichwertig je nach GitHub UI):

`https://raw.githubusercontent.com/<USER>/<REPO>/<BRANCH>/index.xml`

Ein reales Beispiel (öffentlicher Blogpost; nur als Pattern):  
`https://github.com/schapps/ReaperScripts/raw/master/index.xml`

## Schritt 3 — In REAPER/ReaPack importieren

In REAPER:

1. **Extensions → ReaPack → Import repositories…**
2. Deine Raw `index.xml` URL einfügen.
3. **Extensions → ReaPack → Synchronize packages**
4. Dann in “Browse packages” die DF95 Packs installieren (Core + Tools + Catalogs + Legacy + Resources).

## Schritt 4 — DF95 Config setzen (für Install Doctor)

In `Support/DF95_Config.json`:

```json
"reapack": {
  "df95_repo_index_url": "https://raw.githubusercontent.com/<USER>/<REPO>/<BRANCH>/index.xml"
}
```

Dann zeigt der Install Doctor die URL prominent an und bietet Copy-to-Clipboard (via SWS) an.

## Schritt 5 — Updates (Release Routine)

Kurzablauf:

1. `bump_reapack_version.py X.Y.Z` (oder manuell im `index.xml`)
2. Commit
3. `git tag -a vX.Y.Z -m "DF95 vX.Y.Z"`
4. Push (inkl. Tags)
5. In REAPER: ReaPack → **Synchronize packages**

## Troubleshooting (typisch)

- **ReaPack fehlt**: Install Doctor zeigt *nur* “ReaPack installieren”.
- **URL nicht gesetzt**: Smoke Test warnt (kein Error).
- **Private Repo Zugriff**: Wenn dein Git‑Host Auth braucht, stelle sicher, dass der Raw-Link ohne Login abrufbar ist (oder nutze GitLab Token/Basic Auth-URL – falls dein Host das zulässt).