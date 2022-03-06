"""A dictionary."""

__author__ = "730403454"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Invert."""
    mirror: dict[str, str] = {}
    for key in original:
        for kev in original:
            if key == kev and original[key] != original[kev]:
                raise KeyError("Not so fast, bucko!")
            else:
                mirror[original[key]] = key
    return mirror


def favorite_color(colors: dict[str, str]) -> str:
    most_popular: str = ""
    tote: dict[str, int] = {}
    for trip in colors:
        tote[colors[trip]] = 1
        for voyage in colors:
            if colors[trip] == colors[voyage]:
                tote[colors[trip]] += 1
    print(tote)
    while len(tote) > 1:
        for bag in tote:
            for brand in tote:
                if tote[bag] > tote[brand]:
                    tote.pop(brand)
    for key in tote:
        most_popular = key
        return most_popular


def count(rope: list[str]) -> dict[str, int]:
    expansion: dict[str, int] = {}
    for link in rope:
        expansion[link] = 0
    for chain in rope:
        if chain in expansion:
            expansion[chain] += 1
    return expansion
        






        







