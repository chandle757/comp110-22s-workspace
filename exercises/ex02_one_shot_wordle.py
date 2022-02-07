"""One Shot Wordle"""


__author__ = "730403454"

x: str = ("python")
guess: str = input(f"What is your {len(x)}-letter guess? ")
i: int = 0
y: str = ("")
z: int = 0
f: bool = False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while len(guess) != len(x):
    guess: str = input(f"That was not {len(x)} letters! Try again: ")
while i < len(x):
    if guess[i] == x[i]:
        y = str(y + GREEN_BOX)
    else:
        f = False
        z = 0
        while f is not True and z < len(x): 
            if guess[i] == x[z]:
                f = True 
            else:
                z = z + 1
        if f is True:
            y = str(y + YELLOW_BOX) 
        else:
            y = str(y + WHITE_BOX)
    i = i + 1
print(y)
if (guess) != x:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
