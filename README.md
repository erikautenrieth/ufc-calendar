# UFC Calendar

Automatisches Tool zum Scrapen von UFC-Events und deren Eintrag in Google Calendar.


## Dependencies

**Web Scraping:**
- beautifulsoup4
- requests

**Google Calendar:**
- gcsa ([github.com/kuzmoyev/google-calendar-simple-api](https://github.com/kuzmoyev/google-calendar-simple-api))
- google-api-python-client
- google-auth
- google-auth-oauthlib


## Installation

```bash
pip install -r requirements.txt
```


## Setup

### Google Credentials erstellen

Folge dieser [Anleitung](https://google-calendar-simple-api.readthedocs.io/en/latest/getting_started.html#credentials) um `credentials.json` zu generieren.


## Verwendung

```bash
python main.py
```

Browser öffnet sich → anmelden → `token.pickle` wird erstellt

## Automatisierung (GitHub Actions)

Der Workflow läuft automatisch am 1. des Monats oder kann manuell getriggert werden.

### Setup

1. **Lokal authentifizieren** (einmalig):
   ```bash
   python main.py
   ```
   Browser öffnet sich → anmelden → `token.pickle` wird erstellt

2. **Token in base64 konvertieren** (PowerShell/Windows):
   ```powershell
   [Convert]::ToBase64String([IO.File]::ReadAllBytes('token.pickle')) | Set-Clipboard
   ```
   
   Oder (bash/macOS/Linux):
   ```bash
   base64 token.pickle | pbcopy
   ```

3. **GitHub Secret erstellen**:
   - Gehe zu **Settings → Secrets and variables → Actions**
   - Click **New repository secret**
   - Name: `GOOGLE_TOKEN_PICKLE_BASE64`
   - Value: Das base64-encodierte Token einfügen
   - **Save**

4. **Testen**: Im **Actions** Tab → **Sync UFC Calendar** → **Run workflow**