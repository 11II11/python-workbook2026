# Big Numbers by Hand (Very Hard)

Do arithmetic on numbers written as strings — the way you learned it at
school, in a column, digit by digit.

**The rule:** you may turn only *one digit* into a number at a time:
`int(a[i])` is fine, `int(a)` is not. The tests check this.

All inputs are non-negative whole numbers written with digits only. Results
have no leading zeros, except the number zero itself, which is `"0"`.

## Task

- Create a function `strip_zeros(a)` that removes leading zeros:
  `"007"` → `"7"`, `"000"` → `"0"`
- Create a function `compare(a, b)` that returns `1` if `a > b`, `-1` if
  `a < b`, and `0` if they are equal
- Create a function `add(a, b)` that returns `a + b`
- Create a function `subtract(a, b)` that returns `a - b`; you may assume
  `a >= b`
- Create a function `multiply(a, b)` that returns `a * b`

## Examples

| Call                                     | Returns                    |
|------------------------------------------|----------------------------|
| `strip_zeros("00120")`                   | `"120"`                    |
| `compare("123", "99")`                   | `1`                        |
| `compare("007", "7")`                    | `0`                        |
| `add("958", "67")`                       | `"1025"`                   |
| `add("99999999999999999999", "1")`       | `"100000000000000000000"`  |
| `subtract("1000", "1")`                  | `"999"`                    |
| `subtract("500", "500")`                 | `"0"`                      |
| `multiply("12", "34")`                   | `"408"`                    |
| `multiply("123456789", "987654321")`     | `"121932631112635269"`     |

Hints:

- `add`: walk both strings from the end, keep a `carry`, and build the result
  by adding each new digit to the *front*
- `compare`: after `strip_zeros`, a longer number is bigger; equal lengths are
  compared digit by digit from the left
- `multiply`: multiply `a` by each digit of `b` (repeated `add` works), shift
  it by adding `"0"`s at the end, and add the parts up — exactly like column
  multiplication
