import pytest

big_numbers = pytest.importorskip(
    "big_numbers", reason="big_numbers.py not implemented"
)


def _one_digit_int(value=0, *args):
    """`int` that refuses to convert a whole multi-digit string at once."""
    if isinstance(value, str) and len(value.strip()) > 1:
        pytest.fail(f"int({value!r}): convert one digit at a time, not the number")
    return int(value, *args)


@pytest.fixture(autouse=True)
def digit_by_digit(monkeypatch):
    # A module-level name shadows the builtin, so this `int` is the one the
    # student's code calls.
    monkeypatch.setattr(big_numbers, "int", _one_digit_int, raising=False)


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(big_numbers, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


@pytest.mark.parametrize(
    "a, expected",
    [("120", "120"), ("00120", "120"), ("007", "7"), ("000", "0"), ("0", "0")],
)
def test_strip_zeros(a, expected):
    assert function("strip_zeros")(a) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("123", "99", 1),
        ("99", "123", -1),
        ("555", "555", 0),
        # Same length: the first differing digit decides.
        ("12345", "12354", -1),
        ("007", "7", 0),
        ("100000000000000000000", "99999999999999999999", 1),
    ],
)
def test_compare(a, b, expected):
    assert function("compare")(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("0", "0", "0"),
        ("2", "3", "5"),
        ("958", "67", "1025"),
        ("67", "958", "1025"),
        ("99999999999999999999", "1", "100000000000000000000"),
        (
            "123456789012345678901234567890",
            "987654321098765432109876543210",
            "1111111110111111111011111111100",
        ),
    ],
)
def test_add(a, b, expected):
    assert function("add")(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("5", "3", "2"),
        ("1000", "1", "999"),
        ("500", "500", "0"),
        ("1025", "67", "958"),
        ("100000000000000000000", "1", "99999999999999999999"),
    ],
)
def test_subtract(a, b, expected):
    assert function("subtract")(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("12", "34", "408"),
        ("0", "12345", "0"),
        ("12345", "0", "0"),
        ("1", "987", "987"),
        ("999", "999", "998001"),
        ("123456789", "987654321", "121932631112635269"),
    ],
)
def test_multiply(a, b, expected):
    assert function("multiply")(a, b) == expected
