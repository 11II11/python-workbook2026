import threading

import pytest

kaprekar = pytest.importorskip("kaprekar", reason="kaprekar.py not implemented")

TIME_LIMIT = 5


def function(name):
    """The student's function, or a skip if it is not written yet.

    Losing the leading zero of a number like 0999 sends `kaprekar_steps` into
    an endless loop, so every call gets a time limit instead of freezing the
    whole test run. The stuck thread is a daemon and dies with pytest.
    """
    func = getattr(kaprekar, name, None)
    if func is None:
        pytest.skip(f"{name} not implemented")

    def limited(*args):
        result = {}

        def run():
            try:
                result["value"] = func(*args)
            except Exception as error:  # re-raised below, in the test itself
                result["error"] = error

        worker = threading.Thread(target=run, daemon=True)
        worker.start()
        worker.join(TIME_LIMIT)
        if worker.is_alive():
            pytest.fail(f"{name}{args} did not finish in {TIME_LIMIT}s: endless loop?")
        if "error" in result:
            raise result["error"]
        return result["value"]

    return limited


@pytest.mark.parametrize(
    "n, expected",
    [(3524, 5432), (6174, 7641), (1000, 1000), (21, 2100), (9090, 9900)],
)
def test_digits_desc(n, expected):
    assert function("digits_desc")(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(3524, 2345), (6174, 1467), (3087, 378), (1000, 1), (21, 12)],
)
def test_digits_asc(n, expected):
    assert function("digits_asc")(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(3524, 3087), (3087, 8352), (8352, 6174), (6174, 6174), (1000, 999)],
)
def test_kaprekar_step(n, expected):
    assert function("kaprekar_step")(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (6174, 0),
        (8352, 1),
        (3524, 3),
        (2111, 5),
        # 999 is really 0999: the leading zero must not be lost on the way.
        (1000, 5),
        (9998, 5),
        (1111, -1),
        (7777, -1),
    ],
)
def test_kaprekar_steps(n, expected):
    assert function("kaprekar_steps")(n) == expected


@pytest.mark.parametrize(
    "k, expected",
    [(-1, 9), (0, 1), (1, 356), (3, 2124), (7, 1980), (8, 0)],
)
def test_count_with_steps(k, expected):
    assert function("count_with_steps")(k) == expected
