"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730403454"

from ast import If
from tokenize import Ignore

x: int = 0
first_word_guess: str = input("Enter a 5-character word: ")
if len(first_word_guess) != 5:
        print("Error: Word must contain 5 characters")
        exit()
else:
        Ignore
first_letter_guess: str = input("Enter a letter: ")
if len(first_letter_guess) != 1:
        print ("Error: Character must be a single character.")
        exit()
else:
        Ignore
print("Searching for " + first_letter_guess + " in " + first_word_guess)
if first_letter_guess == first_word_guess[0]:
        print(first_letter_guess + " found at index 0")
        x = x + 1
else:
        Ignore 
if first_letter_guess == first_word_guess[1]:
        print( first_letter_guess + " found at index 1")
        x = x + 1
else:
       Ignore
if first_letter_guess == first_word_guess[2]:
        print( first_letter_guess + " found at index 2")
        x = x + 1
else:
        Ignore
if first_letter_guess == first_word_guess[3]:
        print( first_letter_guess + " found at index 3")
        x = x + 1
else:
        Ignore
if first_letter_guess == first_word_guess[4]:
        print( first_letter_guess + " found at index 4")  
        x = x + 1 
else:
        Ignore   
if x > 0:
        if x == 1:
                print("1 instance of " + first_letter_guess + " found in " + first_word_guess)
        else:
                print(str(x) + " instances of " + first_letter_guess + " found in " + first_word_guess)
else: 
        print("No instances of " + first_letter_guess + " found in " + first_word_guess)


                         