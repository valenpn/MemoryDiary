from typing import List
import pandas as pd
from datetime import datetime
from errors import DateBeforeDataDates


def validate_range(dates:List, df: pd.DataFrame):
    smallest_date = df['Date'].min()
    if not all(datetime.strptime(date, '%Y/%m/%d').date() > smallest_date for date in dates):
        raise DateBeforeDataDates
