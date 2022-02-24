"""Building list utility functions."""

__author__ = "730403454"


def only_evens(numbers: list[int]) -> list[int]:
    """Returns only the even numbers."""
    evens: list[int] = list()
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


def sub(set: list[int], start_index: int, end_index: int) -> list[int]:
    """Creates a well oiled subset."""
    i: int = start_index
    subset: list[int] = list()
    if len(set) > 0 and start_index < len(set) and end_index > 0:
        while i < end_index:
            subset.append(set[i])
            i += 1
        return subset
    else:
        return []


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Combines two list."""
    big_list: list[int] = list()
    for digit in first_list:
        big_list.append(digit)
    for numeral in second_list:
        big_list.append(numeral)
    return big_list

         
