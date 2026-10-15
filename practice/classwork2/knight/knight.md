# Knight's Moves (Very Hard)

Chess squares are named by a column letter `a`–`h` and a row digit `1`–`8`:
`"a1"` is the bottom-left corner, `"h8"` the top-right.

A knight moves in an "L": two squares in one direction and one square to the
side. From `d4` it can reach `b3`, `b5`, `c2`, `c6`, `e2`, `e6`, `f3`, `f5`.

## Task

- Create a function `is_valid_square(square)` that returns `True` for a
  2-character string with a letter `a`–`h` and a digit `1`–`8`
- Create a function `is_knight_move(start, end)` that returns `True` if a
  knight on `start` can jump to `end` in one move
- Create a function `knight_moves(square)` that returns how many squares the
  knight can jump to from `square` without leaving the board
- Create a function `min_moves(start, end)` that returns the smallest number
  of moves the knight needs: `0`, `1` or `2` — or `-1` if it needs more
  than two

## Examples

| Call                          | Returns |
|-------------------------------|---------|
| `is_valid_square("e4")`       | `True`  |
| `is_valid_square("i1")`       | `False` |
| `is_knight_move("g1", "f3")`  | `True`  |
| `is_knight_move("g1", "g3")`  | `False` |
| `knight_moves("d4")`          | `8`     |
| `knight_moves("a1")`          | `2`     |
| `min_moves("a1", "a1")`       | `0`     |
| `min_moves("a1", "b3")`       | `1`     |
| `min_moves("a1", "c5")`       | `2`     |
| `min_moves("e4", "e5")`       | `-1`    |

Hints:

- the distance between columns is `abs(ord(start[0]) - ord(end[0]))`
- `knight_moves`: go over all 64 squares with two nested loops,
  `for col in "abcdefgh":` and `for row in "12345678":`, and count the ones
  `is_knight_move` accepts
- `min_moves` for 2: is there a middle square that is one knight move from
  both `start` and `end`?
