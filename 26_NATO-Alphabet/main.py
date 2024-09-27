import pandas
import re

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# {"A": "Alfa", "B": "Bravo"}
nato_dict = {code['letter']: code['code'] for word, code in data.iterrows()}

def generate_phonetic():
    phonetic_list = []
    user_input = input("\nEnter your name = ")

    filtered_input = re.sub(r'[^a-zA-Z0-9]', "", user_input)

    try:
        phonetic_list = [f"{letter.upper()} - {nato_dict[letter.upper()]}" for letter in filtered_input]
    except KeyError:
        print("Sorry! Only English Alphabets are allowed.")
        generate_phonetic()

    for line in phonetic_list:
        print(line)

while True:
    generate_phonetic()

    again = input("\nWant to try again (Y/N)? ").upper()

    if again != "Y":
        break
