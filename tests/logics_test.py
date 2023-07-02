import pytest
import pandas as pd
from datetime import datetime
from logics.validators import validate_range
from errors import DateBeforeDataDates
def test_valid_dates():
    df = pd.DataFrame({'Date': ['2023/07/02', '2023/07/03', '2023/07/04']})
    dates = ['2023/07/05', '2023/07/06', '2023/07/07']
    # No exception should be raised if all dates are after the smallest_date in the DataFrame
    assert validate_range(dates, df) is None

def test_invalid_dates():
    df = pd.DataFrame({'Date': ['2023/07/02', '2023/07/03', '2023/07/04']})
    dates = ['2023/06/30', '2023/07/01', '2023/07/02']
    # DateBeforeDataDates exception should be raised if any date is before or equal to the smallest_date
    with pytest.raises(DateBeforeDataDates):
        validate_range(dates, df)

def test_empty_dates():
    df = pd.DataFrame({'Date': ['2023/07/02', '2023/07/03', '2023/07/04']})
    dates = []
    # No exception should be raised if dates list is empty
    assert validate_range(dates, df) is None
