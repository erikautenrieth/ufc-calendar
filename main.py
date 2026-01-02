from src.scraper import get_upcoming_ufc_fights
from src.calendar_handler import CalendarHandler


def main():
    """Main function - Sync UFC fights to Google Calendar."""
    # Get upcoming fights
    fights = get_upcoming_ufc_fights()
    print(f"Found {len(fights)} upcoming fights\n")
    
    if not fights:
        print("No upcoming UFC fights found.")
        return
    
    # Sync to calendar
    handler = CalendarHandler(credentials_path='credentials.json')
    handler.sync_fights_to_calendar(fights)


if __name__ == "__main__":
    main()
