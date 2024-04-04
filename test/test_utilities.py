import pytest

from utilities import add_num


@pytest.fixture
def pset() -> list[float]:
    return [1.0, 2.1, 3.1]


@pytest.mark.parametrize(
    "ab, expected",
    [([1.0, 2.1], 3.1), ([-1.0, 2.2], 1.2), ([100001.0, 0.01], 100001.01)],
)
def test_add_num(ab: list, expected: float) -> None:
    assert add_num(ab[0], ab[1]) == pytest.approx(expected, abs=1.0e-6)


def test_add_num_with_fixure(pset: list[float]):
    assert add_num(pset[0], pset[1]) == pytest.approx(pset[2], abs=1.0e-6)
