from art import logo
import random
from os import system

while 1 == 1:
    system('cls')
    print(logo)
    number = random.randint(1, 100)
    print("\nGuess a number between 1 - 100")
    level = input("\nSelect a level 'EASY' or 'HARD' = ").lower()
    if level == "easy":
        attempts = 10
    else:
        attempts = 5

    finish = False
    print(f"\nYou have {attempts} attempts.")

    while not finish:
        if attempts == 0:
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

        attempts -= 1
        print(f"attempts Left: {attempts}")

    again = input("\nDo you want to play again(yes/no)? = ")
    if again != "yes":
        break
    else:
        continue
