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
    guessy: str = input(f"Enter a {x} character word: ")
    while len(guessy) != x:
        guessy: str = input(f"That wasn't {x} chars! Try again: ")
    return guessy


def main() -> None:
    """The entrypoint and main game loop."""
    s: str = "codes"
    v: bool = False
    q: int = 6
    turn_count: int = 1
    while turn_count <= q and v is False:
        print(f"=== Turn {turn_count}/{q} ===")
        r: str = input_guess(5)
        colors: str = emojified(r, s)
        print(colors)
        if r == s:
            print(f"You won in {turn_count}/{q} turns!")
            v = True
        else:
            turn_count += 1
    if turn_count > q and v is False:
        print(f"X/{q} - Sorry, try again tomorrow!")
    return 


if __name__ == "__main__":
    main()
