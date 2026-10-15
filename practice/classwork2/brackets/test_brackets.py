import pytest

brackets = pytest.importorskip("brackets", reason="brackets.py not implemented")


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(brackets, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


@pytest.mark.parametrize("close, expected", [(")", "("), ("]", "["), ("}", "{")])
def test_matching(close, expected):
    assert function("matching")(close) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", -1),
        ("abc", -1),
        ("(a[b]{c})", -1),
        ("print(x[0])", -1),
        ("}", 0),
        # The right count of each kind, in the wrong order.
        ("([)]", 2),
        ("())(", 2),
        ("{[}]", 2),
        ("(()", 3),
        ("x = [1, (2, 3]", 13),
        ("((", 2),
    ],
)
def test_first_error(text, expected):
    assert function("first_error")(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", True),
        ("{[()]}", True),
        ("()[]{}", True),
        ("((", False),
        ("))((", False),
        ("[(])", False),
        # Counting alone is not enough: same number of each, still wrong.
        (")(", False),
    ],
)
def test_is_balanced(text, expected):
    assert function("is_balanced")(text) is expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("abc", 0),
        ("()", 1),
        ("(()())", 2),
        ("((()))()", 3),
        ("[{()}]{}", 3),
        ("(a[b]{c})", 2),
    ],
)
def test_max_depth(text, expected):
    assert function("max_depth")(text) == expected
