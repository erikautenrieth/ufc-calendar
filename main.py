from src.ufc_scraper import UfcScraper
from src.calendar_handler import CalendarHandler
from src.models import UfcEvent


def main():
    """Main function - Sync UFC fights to Google Calendar."""
    scraper = UfcScraper()
    fights: list[UfcEvent] = scraper.get_upcoming_fights()
    print(f"Found {len(fights)} upcoming fights\n")
    
    if not fights:
        print("No upcoming UFC fights found.")
        return
    
    handler = CalendarHandler(credentials_path='credentials.json')
    handler.sync_fights_to_calendar(fights)


if __name__ == "__main__":
    main()
