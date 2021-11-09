from datetime import datetime, timedelta
from inspect import isclass
from typing import Any


def ask_number(prompt, class_, default: Any = None):
    while True:
        try:
            return class_(input(prompt).strip())
        except:
            if default is not None:
                if callable(default):
                    return default()
                return default


def ask_int(prompt, default: Any = int) -> int:
    return ask_number(prompt, int, default)


def ask_float(prompt, default: Any = float) -> float:
    return ask_number(prompt, float, default)


def ask_time_delta():
    msg = 'enter {} [leave blank for {}]: '
    return timedelta(
        weeks=ask_float(msg.format('weeks', 0)),
        days=ask_float(msg.format('days', 0)),
        hours=ask_float(msg.format('hours', 0)),
        minutes=ask_float(msg.format('minutes', 0)),
        seconds=ask_float(msg.format('seconds', 0))
    )


MONTH_NAME_TO_INT = dict(
    jan=1,
    feb=2,
    mar=3,
    apr=4,
    may=5,
    jun=6,
    jul=7,
    aug=8,
    sep=9,
    oct=10,
    nov=11,
    dec=12
)


def ask_month():
    while True:
        value = input(f'enter month [leave blank for 1/jan]: ').lower().strip()
        if value.isnumeric():
            value = int(value)
            if 1 <= value <= 12:
                return value
        elif value in MONTH_NAME_TO_INT:
            return MONTH_NAME_TO_INT[value]


def ask_date_time():
    msg = 'enter {} [leave blank for {}]: '
    return datetime(
        year=ask_int(msg.format('year', 0)),
        month=ask_month(),
        day=ask_int(msg.format('day', 0)),
        hour=ask_int(msg.format('hour', 0)),
        minute=ask_int(msg.format('minute', 0)),
        second=ask_int(msg.format('second', 0)),
    )


def format_datetime(date: datetime):
    return date.strftime('%B[%m]/%A[%d]/%Y - %I:%M:%S %p')


base_date = (
    datetime.now()
    if input('use current date as base datetime? [Y/N]: ').lower().strip() == 'y'
    else ask_date_time())

while True:
    print(f'\nentered date:\n\t{format_datetime(base_date)}')

    print('\nenter the delta to add to the date')
    delta = ask_time_delta()

    date = base_date + delta
    print(f'\nfinal date: {format_datetime(date)}')
    input('PRESS ENTER TO CONTINUE...')
