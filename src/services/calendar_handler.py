from typing import Iterable

from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event as GcsaEvent

from src.models import UfcEvent


class CalendarHandler:
    """Handles Google Calendar operations."""

    def __init__(self, credentials_path: str = "credentials.json") -> None:
        """Initialize Google Calendar connection."""
        self.calendar = GoogleCalendar(credentials_path=credentials_path)

    def get_existing_events(self) -> set:
        """Get set of existing event titles."""
        return {str(event).split("\n")[0] for event in self.calendar}

    def sync_fights_to_calendar(self, fights: Iterable[UfcEvent]) -> int:
        """Add UFC fights to calendar if not already present."""
        existing_events = self.get_existing_events()
        added_count = 0

        for fight in fights:
            title = f"UFC {fight.fighters}"

            if title not in existing_events:
                event = GcsaEvent(title, start=fight.date)
                self.calendar.add_event(event)
                print(f"✅ Added: {fight.fighters}")
                added_count += 1
            else:
                print(f"⏭️ Already exists: {fight.fighters}")

        print(f"\n✅ Done! Added {added_count} new events")
        return added_count
