"""Wordle."""


__author__ = 730403454

i: int = 0

def contains_char(a: str, b: str) -> bool:
    """Is b within a?"""
    assert len(b) == 1
    i: int = 0
    while i < len(a):
        if b == a[i]:
            return True
        else:
            f = False
            z = 0
            while f is not True and z < len(a): 
                if b == a[z]:
                    f = True 
                else:
                    z = z + 1
            if f is True:
                return True
            else:
                return False
        i += 1
def emojified(guess: str, secret: str) -> str:
    """Yellow, white, or green."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    GREEN_BOX: str = "\U0001F7E9"
    python: str = ""
    p: int = 0
    while p < len(secret):
        if contains_char(secret, guess[p]) is False:
            python += WHITE_BOX
        elif secret[p] == guess[p]:
            python += GREEN_BOX
        else:
            python += YELLOW_BOX
        p += 1
    return python
def input_guess(x: int) -> str:
    guessy: str = input(f"Enter a {x} character word:")
    while len(guessy) != x:
        guessy: str = input(f"That wasn't {x} chars! Try again: ")
    return guessy