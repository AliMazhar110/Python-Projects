from os import system
from game_data import data
from art import *
import random

finish = False
score=0
while not finish:
    system('cls')
    print(logo)
    print("Current Score =",score)
    person_one = random.choice(data)
    while True:
        person_two = random.choice(data)
        if(person_one['name'] == person_two['name']):
            continue
        break
    print("A - Name :",person_one['name']+",",person_one['description'],"from",person_one['country'])
    print(vs)
    print("B - Name :",person_two['name']+",",person_two['description'],"from",person_two['country'])
    guess = input("Who has more followers? Type 'A' or Type 'B' - ").upper()
    if guess=='A':
        if person_one['follower_count'] > person_two['follower_count']:
            score+=1
        else:
            print("\nYou got it wrong. You scored =",score,"points.")
            finish=True
            continue
    elif guess=='B':
        if person_one['follower_count'] < person_two['follower_count']:
            score+=1
        else:
            print("\nYou got it wrong. You scored =",score,"points.")
            finish=True
            continue
    else:
        print("\nPlease choose correctly.")
        continue

