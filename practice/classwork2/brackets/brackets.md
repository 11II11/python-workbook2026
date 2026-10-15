# Bracket Checker (Very Hard)

Code editors underline a bracket that has no pair. Write the checker.

Three kinds of brackets count: `()`, `[]` and `{}`. Every other character is
ignored. Brackets are **balanced** when every opening bracket is closed by the
same kind, in the right order: `"([]{})"` is balanced, `"([)]"` is not.

## Task

- Create a function `matching(close)` that returns the opening bracket for a
  closing one: `")"` → `"("`, `"]"` → `"["`, `"}"` → `"{"`
- Create a function `first_error(text)` that returns:
  - the index of the first closing bracket that has no matching opener, or
    closes the wrong kind
  - `len(text)` if all closers were fine but some brackets are never closed
  - `-1` if the text is balanced
- Create a function `is_balanced(text)` that returns `True` or `False`
- Create a function `max_depth(text)` that returns the deepest nesting level
  in a balanced text: `"(()())"` has depth 2

## Examples

| Call                          | Returns |
|-------------------------------|---------|
| `matching("]")`               | `"["`   |
| `first_error("(a[b]{c})")`    | `-1`    |
| `first_error("([)]")`         | `2`     |
| `first_error("())(")`         | `2`     |
| `first_error("(()")`          | `3`     |
| `is_balanced("{[()]}")`       | `True`  |
| `is_balanced("((")`           | `False` |
| `max_depth("[{()}]{}")`       | `3`     |
| `max_depth("abc")`            | `0`     |

Hint: keep the brackets that are still open in a **string**, `stack = ""`.
Add an opener with `stack += ch`; the last open bracket is `stack[-1]`;
remove it with `stack = stack[:-1]`.
