from src.ufc_scraper import UfcScraper
from src.calendar_handler import CalendarHandler


def main():
    """Main function - Sync UFC fights to Google Calendar."""
    # Get upcoming fights
    scraper = UfcScraper()
    fights = scraper.get_upcoming_fights()
    print(f"Found {len(fights)} upcoming fights\n")
    
    if not fights:
        print("No upcoming UFC fights found.")
        return
    
    # Sync to calendar
    handler = CalendarHandler(credentials_path='credentials.json')
    handler.sync_fights_to_calendar(fights)


if __name__ == "__main__":
    main()
