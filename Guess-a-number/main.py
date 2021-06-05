#Number Guessing Game Objectives:
from art import logo
import random
from os import system
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
while 1==1:
    system('cls')
    print(logo)
    number = random.randint(1,100)
    print("\nGuess a number between 1 - 100");
    level = input("\nSelect a level 'EASY' or 'HARD' = ").lower()
    if level == "easy":
        attempts = 10
    else:
        attempts = 5
    finish = False
    print(f"\nYou have {attempts} attempts.")
    while not finish:
        if attempts==0:
            print("\nNo Attempts Left. You Lost.")
            print(f"The number was {number}")
            finish = True
            continue
        guess = int(input("\nGuess a number = "))
        if guess == number:
            print(f"\nCorrect. You got it. Number was {number}")
            finish = True
        elif guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low")
        attempts-=1
        print(f"attempts Left: {attempts}")
    again = input("\nDo you want to play again(yes/no)? = ")
    if(again!="yes"):
        break
    else:
        continue
