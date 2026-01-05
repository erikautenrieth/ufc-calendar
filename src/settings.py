from __future__ import annotations

from pathlib import Path
from typing import Optional

# TODO: use BaseSettings and pyproject.toml for settings management
#from pydantic_settings import BaseSettings
# BaseSettings

class Settings():
    credentials_path: Path = Path("credentials.json")
    token_pickle: Path = Path("token.pickle")
    calendar_id: Optional[str] = None




settings = Settings()
