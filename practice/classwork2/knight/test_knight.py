import pytest

knight = pytest.importorskip("knight", reason="knight.py not implemented")


def function(name):
    """The student's function, or a skip if it is not written yet."""
    func = getattr(knight, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")
    return func


@pytest.mark.parametrize(
    "square, expected",
    [
        ("a1", True),
        ("h8", True),
        ("e4", True),
        ("i1", False),
        ("a9", False),
        ("a0", False),
        ("A1", False),
        ("e44", False),
        ("", False),
    ],
)
def test_is_valid_square(square, expected):
    assert function("is_valid_square")(square) is expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        ("g1", "f3", True),
        ("d4", "b5", True),
        ("d4", "f3", True),
        ("h8", "g6", True),
        ("g1", "g3", False),
        ("d4", "f6", False),
        ("d4", "d4", False),
        # Wraps around the board edge if columns are compared carelessly.
        ("a1", "h2", False),
    ],
)
def test_is_knight_move(start, end, expected):
    assert function("is_knight_move")(start, end) is expected


@pytest.mark.parametrize(
    "square, expected",
    [("a1", 2), ("h8", 2), ("b1", 3), ("h5", 4), ("b2", 4), ("c3", 8), ("d4", 8)],
)
def test_knight_moves(square, expected):
    assert function("knight_moves")(square) == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        ("a1", "a1", 0),
        ("a1", "b3", 1),
        ("g1", "f3", 1),
        ("a1", "c5", 2),
        ("a1", "a3", 2),
        ("e4", "f5", 2),
        ("e4", "e5", -1),
        ("a1", "b2", -1),
        ("a1", "h8", -1),
    ],
)
def test_min_moves(start, end, expected):
    assert function("min_moves")(start, end) == expected
