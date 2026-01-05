from typing import List

import requests
from bs4 import BeautifulSoup
from datetime import datetime

from src.utils import convert_date_string_to_datetime
from src.models import UfcEvent


UFC_EVENTS_URL = "https://www.ufc.com/events"

VS_KEYWORD = "vs"
MAIN_CARD_KEYWORD = "Main Card"
TBD_KEYWORD = "TBD"
ATHLETE_TOTAL_CLASS = "althelete-total"


class UfcScraper:
    """Scraper for upcoming UFC events."""

    def __init__(self, events_url: str = UFC_EVENTS_URL) -> None:
        self.events_url = events_url

    def fetch_upcoming_events_html(self) -> BeautifulSoup:
        page = requests.get(self.events_url, headers={"User-Agent": "Mozilla/5.0"})
        return BeautifulSoup(page.content, "html.parser")

    def extract_fights_from_html(self, soup: BeautifulSoup) -> List[UfcEvent]:
        all_anchor_tags = soup.find_all(name="a")

        athlete_total = soup.find(class_=ATHLETE_TOTAL_CLASS)
        count_matches = int(athlete_total.text[0]) if athlete_total else len(all_anchor_tags)

        fight_list: List[dict] = []
        fight_dict = {"fighters": None, "date": None}

        for tag in all_anchor_tags:
            if VS_KEYWORD in tag.text:
                fight_dict["fighters"] = tag.text
            if MAIN_CARD_KEYWORD in tag.text:
                fight_dict["date"] = tag.text
                fight_list.append(fight_dict.copy())
                fight_dict = {"fighters": None, "date": None}

        # Filter TBD and parse dates
        raw_fights = [f for f in fight_list[:count_matches] if f["fighters"] and TBD_KEYWORD not in f["fighters"]]
        events: List[UfcEvent] = []
        for fight in raw_fights:
            dt = convert_date_string_to_datetime(fight["date"]) if fight.get("date") else None
            if dt:
                events.append(UfcEvent(fighters=fight["fighters"], date=dt))

        return events

    def get_upcoming_fights(self) -> List[UfcEvent]:
        soup = self.fetch_upcoming_events_html()
        fight_list = self.extract_fights_from_html(soup)

        now = datetime.now()
        return [fight for fight in fight_list if now < fight.date]
