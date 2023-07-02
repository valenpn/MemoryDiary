from typing import List
import pandas as pd

from errors import DateBeforeDataDates


def validate_range(dates:List, df: pd.DataFrame):
    # smallest_date = df['Date'].min()
    # if not all(date_str > str(smallest_date) for date_str in dates):
    #     raise DateBeforeDataDates
    pass