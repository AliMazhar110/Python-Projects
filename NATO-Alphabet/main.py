import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# {"A": "Alfa", "B": "Bravo"}
nato_dict = {code['letter']: code['code'] for word, code in data.iterrows()}

def generate_phonetic():
    phonetic_list = []
    user_input = input("Enter your name = ")
    try:
        phonetic_list = [f"{letter.upper()} - {nato_dict[letter.upper()]}" for letter in user_input]
    except KeyError:
        print("Sorry! Only English Alphabets are allowed.")
        generate_phonetic()

    for line in phonetic_list:
        print(line)

generate_phonetic()
