from typing import List
from datetime import datetime

from errors import DateBeforeDataDates


def validate_range(dates: List, smallest_date: datetime.date):
    if not all(date > smallest_date for date in dates):
        raise DateBeforeDataDates
