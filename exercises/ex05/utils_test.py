"""Test for utils."""

__author__ = "730403454"

from utils import only_evens, sub, concat


def test_only_evens_single_item() -> None:
    """First."""
    xs: list[int] = [3]
    assert only_evens(xs) == []


def test_only_evens_multiple_items() -> None:
    """Let."""
    ys: list[int] = [1, 2, 3, 4]
    assert only_evens(ys) == [2, 4]


def test_only_evens_multiple_items_again() -> None:
    """Me."""
    zs: list[int] = [2, 4, 6, 8]
    assert only_evens(zs) == [2, 4, 6, 8]
    

def test_sub_return_empty() -> None:
    """Hop."""
    bs: list[int] = [5, 6, 7, 8]
    start: int = 5 
    end: int = 1
    assert sub(bs, start, end) == []


def test_sub_return_real_subset() -> None:
    """Out."""
    cs: list[int] = [5, 6, 7, 8]
    begining: int = 2
    ending: int = 4
    assert sub(cs, begining, ending) == [7, 8]


def test_sub_return_real_again() -> None:
    """The."""
    ds: list[int] = [1, 2, 3, 4, 5, 6]
    go: int = 1
    finish: int = 4
    assert sub(ds, go, finish) == [2, 3, 4]


def test_concat_empty() -> None:
    """MF."""
    es: list[int] = []
    fs: list[int] = []
    assert concat(es, fs) == []


def test_concat_real_move_in() -> None:
    """Porcshe."""
    gs: list[int] = [1, 2, 3, 4]
    silence: list[int] = [6, 8, 10, 12]
    assert concat(gs, silence) == [1, 2, 3, 4, 6, 8, 10, 12]


def test_conact_all_jokes() -> None:
    """IDWHTADSLAH."""
    hs: list[int] = [2, 5, 7]
    ms: list[int] = [9]
    assert concat(hs, ms) == [2, 5, 7, 9]