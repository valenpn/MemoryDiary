import pytest
from datetime import datetime
from logics.validators import validate_range
from errors import DateBeforeDataDates

DATES = [datetime.strptime('2023/07/02', '%Y/%m/%d').date(), datetime.strptime('2023/07/03', '%Y/%m/%d').date()]


def test_valid_dates():
    smallest_date = datetime.strptime('2023/07/01', '%Y/%m/%d').date()
    assert validate_range(DATES, smallest_date) is None


def test_invalid_dates():
    smallest_date = datetime.strptime('2023/07/03', '%Y/%m/%d').date()
    with pytest.raises(DateBeforeDataDates):
        validate_range(DATES, smallest_date)
