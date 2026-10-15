import inspect
import re

import pytest

month_calendar = pytest.importorskip(
    "month_calendar", reason="month_calendar.py not implemented"
)


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(month_calendar, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


def test_no_date_modules():
    source = inspect.getsource(month_calendar)
    assert not re.search(r"\b(import|from)\s+(datetime|calendar)\b", source), (
        "Work the dates out yourself: do not import datetime or calendar."
    )


@pytest.mark.parametrize(
    "year, expected",
    [(2024, True), (2023, False), (1900, False), (2000, True), (2100, False)],
)
def test_is_leap(year, expected):
    assert function("is_leap")(year) is expected


@pytest.mark.parametrize(
    "year, month, expected",
    [
        (2026, 1, 31),
        (2026, 4, 30),
        (2026, 9, 30),
        (2026, 12, 31),
        (2023, 2, 28),
        (2024, 2, 29),
        (1900, 2, 28),
        (2000, 2, 29),
    ],
)
def test_days_in_month(year, month, expected):
    assert function("days_in_month")(year, month) == expected


@pytest.mark.parametrize(
    "year, month, day, expected",
    [
        (1900, 1, 1, 0),
        (1900, 1, 7, 6),
        (1900, 3, 1, 3),
        (2000, 2, 29, 1),
        (2000, 3, 1, 2),
        (2024, 12, 31, 1),
        (2026, 10, 15, 3),
        (2099, 12, 31, 3),
    ],
)
def test_day_of_week(year, month, day, expected):
    assert function("day_of_week")(year, month, day) == expected


@pytest.mark.parametrize(
    "year, month, expected",
    [
        (
            2026,
            10,
            "Mo Tu We Th Fr Sa Su\n"
            "          1  2  3  4\n"
            " 5  6  7  8  9 10 11\n"
            "12 13 14 15 16 17 18\n"
            "19 20 21 22 23 24 25\n"
            "26 27 28 29 30 31",
        ),
        # Starts on a Monday and ends on a Sunday: no partial weeks at all.
        (
            2021,
            2,
            "Mo Tu We Th Fr Sa Su\n"
            " 1  2  3  4  5  6  7\n"
            " 8  9 10 11 12 13 14\n"
            "15 16 17 18 19 20 21\n"
            "22 23 24 25 26 27 28",
        ),
        # Starts on a Sunday: six week lines, the last one a single day.
        (
            2024,
            9,
            "Mo Tu We Th Fr Sa Su\n"
            "                   1\n"
            " 2  3  4  5  6  7  8\n"
            " 9 10 11 12 13 14 15\n"
            "16 17 18 19 20 21 22\n"
            "23 24 25 26 27 28 29\n"
            "30",
        ),
        # A leap February.
        (
            2024,
            2,
            "Mo Tu We Th Fr Sa Su\n"
            "          1  2  3  4\n"
            " 5  6  7  8  9 10 11\n"
            "12 13 14 15 16 17 18\n"
            "19 20 21 22 23 24 25\n"
            "26 27 28 29",
        ),
    ],
)
def test_month_calendar(year, month, expected):
    assert function("month_calendar")(year, month) == expected
