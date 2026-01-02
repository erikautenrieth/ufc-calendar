
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event


class CalendarHandler:
    """Handles Google Calendar operations."""
    
    def __init__(self, credentials_path='credentials.json'):
        """Initialize Google Calendar connection."""
        self.calendar = GoogleCalendar(credentials_path=credentials_path)
    
    def get_existing_events(self):
        """Get set of existing event titles."""
        return {str(event).split('\n')[0] for event in self.calendar}
    
    def sync_fights_to_calendar(self, fights):
        """Add UFC fights to calendar if not already present."""
        existing_events = self.get_existing_events()
        added_count = 0
        
        for fight in fights:
            fighters = fight["fighters"]
            
            if fighters not in str(existing_events):
                event = Event(
                    f'UFC {fighters}',
                    start=fight['date'],
                )
                self.calendar.add_event(event)
                print(f"✅ Added: {fighters}")
                added_count += 1
            else:
                print(f"⏭️ Already exists: {fighters}")
        
        print(f"\n✅ Done! Added {added_count} new events")
        return added_count
