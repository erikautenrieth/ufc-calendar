import re
from datetime import datetime

MONTH_MAPPING = {
    'jan': 'jan', 'feb': 'feb', 'mär': 'mar', 'apr': 'apr',
    'mai': 'may', 'jun': 'jun', 'jul': 'jul', 'aug': 'aug',
    'sep': 'sep', 'okt': 'oct', 'nov': 'nov', 'dez': 'dec'
}


def convert_date_string_to_datetime(date_string: str) -> datetime:
    """Convert date string from UFC site to a datetime object.

    Expected input formats come from the site's event labels and look like
    "..., Month Day / HH:MM ...". This keeps the original parsing logic.
    """
    element_date = re.split(', |/', date_string)[1:3]
    date_parts = element_date[0].split(" ")
    month = date_parts[0].lower()[:3]
    day = date_parts[1]

    if month in MONTH_MAPPING:
        month = MONTH_MAPPING[month]

    hour = int(element_date[1].split(" ")[1].split(":")[0])
    return datetime(datetime.now().year, datetime.strptime(month, '%b').month, int(day), hour, 0)
