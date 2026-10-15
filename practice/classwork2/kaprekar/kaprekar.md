# Kaprekar's Constant (Very Hard)

Take any 4-digit number whose digits are not all the same. Arrange its digits
in descending order, then in ascending order, and subtract:

```
3524:  5432 - 2345 = 3087
3087:  8730 - 0378 = 8352
8352:  8532 - 2358 = 6174
6174:  7641 - 1467 = 6174   ← stuck here forever
```

Every such number reaches **6174** in at most 7 steps. Numbers below 1000 are
treated as 4 digits with leading zeros: `21` is `0021`, so its digits are
`2, 1, 0, 0`.

## Task

- Create a function `digits_desc(n)` that returns the 4 digits of `n`
  arranged in descending order, as a number: `3524` → `5432`, `21` → `2100`
- Create a function `digits_asc(n)` — the same in ascending order:
  `3524` → `2345`, `21` → `12` (that is, `0012`)
- Create a function `kaprekar_step(n)` that returns
  `digits_desc(n) - digits_asc(n)`
- Create a function `kaprekar_steps(n)` that returns how many steps it takes
  `n` to reach 6174 (`0` for 6174 itself), or `-1` if all 4 digits are the
  same (`1111`, `7777`, ...), since those fall to 0 and never get there
- Create a function `count_with_steps(k)` that returns how many numbers from
  1000 to 9999 have `kaprekar_steps` equal to `k`

## Examples

| Call                      | Returns |
|---------------------------|---------|
| `digits_desc(3524)`       | `5432`  |
| `digits_asc(3087)`        | `378`   |
| `kaprekar_step(3524)`     | `3087`  |
| `kaprekar_steps(3524)`    | `3`     |
| `kaprekar_steps(6174)`    | `0`     |
| `kaprekar_steps(1111)`    | `-1`    |
| `count_with_steps(0)`     | `1`     |
| `count_with_steps(7)`     | `1980`  |

Hint: you cannot sort without lists yet — and you do not need to. Go through
the digits `"9"`, `"8"`, ..., `"0"` and add each one as many times as it
occurs: `f"{n:04d}".count("5")` tells how many 5s there are.
