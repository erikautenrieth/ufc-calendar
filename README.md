# UFC Calendar

Automatisches Tool zum Scrapen von UFC-Events und deren Eintrag in Google Calendar.

## Installation

```bash
pip install -r requirements.txt
```

## Dependencies

- beautifulsoup4
- requests
- google-api-python-client
- gcsa ([github.com/kuzmoyev/google-calendar-simple-api](https://github.com/kuzmoyev/google-calendar-simple-api))
- google-auth
- google-auth-oauthlib
- lxml


## Setup

1. Downloade `credentials.json` von Google Cloud Platform
2. Lege `credentials.json` im Root-Verzeichnis ab
3. Beim ersten Run öffnet sich der Browser zur Authentifizierung

## Verwendung

```bash
python main.py
```

