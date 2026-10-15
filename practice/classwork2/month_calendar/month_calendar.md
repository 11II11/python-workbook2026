# Month Calendar (Very Hard)

Print a month the way a wall calendar shows it, for any year from 1900 on.

You may not import `datetime` or `calendar` — the point is to work the dates
out yourself. One fact to start from: **1 January 1900 was a Monday.**

## Task

- Create a function `is_leap(year)` — a leap year is divisible by 4, except
  centuries, which must be divisible by 400
- Create a function `days_in_month(year, month)` that returns 28, 29, 30
  or 31
- Create a function `day_of_week(year, month, day)` that returns the day of
  the week as a number: `0` is Monday, `1` Tuesday, ..., `6` Sunday
- Create a function `month_calendar(year, month)` that returns the calendar
  as **one string** of lines joined by `"\n"`:
  - the first line is `Mo Tu We Th Fr Sa Su`
  - then one line per week, Monday to Sunday
  - every day takes 2 characters, right-aligned, and days are separated by
    one space; an empty day before the 1st is 3 spaces
  - no spaces at the end of a line, and no `"\n"` at the end of the string

## Examples

| Call                          | Returns |
|-------------------------------|---------|
| `is_leap(1900)`               | `False` |
| `is_leap(2000)`               | `True`  |
| `days_in_month(2024, 2)`      | `29`    |
| `day_of_week(1900, 1, 1)`     | `0`     |
| `day_of_week(2026, 10, 15)`   | `3`     |

`print(month_calendar(2026, 10))` shows:

```
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
```

Hints:

- `day_of_week`: count the days from 1 January 1900 up to the date — whole
  years first, then whole months, then the days — and take `% 7`
- `f"{day:2d}"` gives a day 2 characters wide; `.rstrip()` removes spaces at
  the end of a line
