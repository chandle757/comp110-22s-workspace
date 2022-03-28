"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))

# Define a function named contains
# Two parameters
# 1. needle - the string were searching for
# 2. haystack - the list were searching through


def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm:
    #   For each item in the haystack
    #       Test if it is equal to the needle
    #    If so, return True
    for item in haystack:
        if item == needle:
            return True
    #   After testing all items, return false, because not found
    # Returns true if needle in haystack, false oterwise
    return False


if __name__ == "__main__":
    main()
else:
    print(__name__)