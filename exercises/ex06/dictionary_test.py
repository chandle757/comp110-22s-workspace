"""Dictionary test."""

__author__ = "730403454"

from dictionary import invert, favorite_color, count


def test_invert_single_item() -> None:
    """Not."""
    xs: dict[str, str] = {"Ball": "Fall"}
    assert invert(xs) == {"Fall": "Ball"}


def test_invert_multiple() -> None:
    """Your."""
    ys: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(ys) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2multiple() -> None:
    """average."""
    zs: dict[str, str] = {'apple': 'cat'}
    assert invert(zs) == {'cat': 'apple'}


def test_favorite_color_first() -> None:
    """joe."""
    bs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(bs) == "blue"


def test_favorite_color_single() -> None:
    """Bait."""
    cs: dict[str, str] = {"Lasha": "brown"}
    assert favorite_color(cs) == "brown"


def test_favorite_color_tie() -> None: 
    """Jeff."""
    ds: dict[str, str] = {"Jeff": "green", "Brenda": "blue"}
    assert favorite_color(ds) == "green"


def test_count_1_item() -> None:
    """Bring."""
    es: list[str] = ["Wow"]
    assert count(es) == {"Wow": 1}


def test_count_multiple_sets() -> None: 
    """That."""
    fs: list[str] = ["Wow", "I", "am", "am", "Wow"]
    assert count(fs) == {"Wow": 2, "am": 2, "I": 1}


def test_count_multiple_again() -> None:
    """This."""
    gs: list[str] = ["yes", "yes", "no", "no"]
    assert count(gs) == {"yes": 2, "no": 2}