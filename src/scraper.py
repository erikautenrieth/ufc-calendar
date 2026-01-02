import re
import requests

from bs4 import BeautifulSoup
from datetime import datetime

UFC_EVENTS_URL = "https://www.ufc.com/events"


VS_KEYWORD = "vs"
MAIN_CARD_KEYWORD = "Main Card"
TBD_KEYWORD = "TBD"
ATHLETE_TOTAL_CLASS = "althelete-total"

MONTH_MAPPING = {
    'jan': 'jan', 'feb': 'feb', 'mär': 'mar', 'apr': 'apr',
    'mai': 'may', 'jun': 'jun', 'jul': 'jul', 'aug': 'aug',
    'sep': 'sep', 'okt': 'oct', 'nov': 'nov', 'dez': 'dec'
}


def fetch_upcoming_events_html():
    """Fetch UFC events page and return BeautifulSoup object."""
    page = requests.get(UFC_EVENTS_URL, headers={'User-Agent': 'Mozilla/5.0'})
    return BeautifulSoup(page.content, "html.parser")


def extract_fights_from_html(soup):
    """Extract fight data from the HTML."""
    all_anchor_tags = soup.find_all(name="a")
    
    athlete_total = soup.find(class_=ATHLETE_TOTAL_CLASS)
    count_matches = int(athlete_total.text[0]) if athlete_total else len(all_anchor_tags)
    
    fight_list = []
    fight_dict = {"fighters": None, "date": None}
    
    for tag in all_anchor_tags:
        if VS_KEYWORD in tag.text:
            fight_dict["fighters"] = tag.text
        if MAIN_CARD_KEYWORD in tag.text:
            fight_dict["date"] = tag.text
            fight_list.append(fight_dict.copy())
            fight_dict = {"fighters": None, "date": None}
    
    # Filter TBD and parse dates
    fight_list = [f for f in fight_list[:count_matches] if TBD_KEYWORD not in f['fighters']]
    for fight in fight_list:
        fight["date"] = convert_date_string_to_datetime(fight["date"])
    
    return fight_list


def convert_date_string_to_datetime(date_string):
    """Convert date string to datetime object."""
    element_date = re.split(', |/', date_string)[1:3]
    date_parts = element_date[0].split(" ")
    month = date_parts[0].lower()[:3]
    day = date_parts[1]
    
    if month in MONTH_MAPPING:
        month = MONTH_MAPPING[month]
    
    hour = int(element_date[1].split(" ")[1].split(":")[0])
    return datetime(datetime.now().year, datetime.strptime(month, '%b').month, int(day), hour, 0)


def get_upcoming_ufc_fights():
    """Fetch all upcoming UFC fights."""
    soup = fetch_upcoming_events_html()
    fight_list = extract_fights_from_html(soup)
    
    # Filter for future fights only
    now = datetime.now()
    return [fight for fight in fight_list if now < fight["date"]]
