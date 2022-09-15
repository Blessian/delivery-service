import datetime
from datetime import date


def validate_date(data: str):
    try:
        datetime.datetime.strptime(data, '%Y-%m-%d')
        return True
    except ValueError:
        return False
