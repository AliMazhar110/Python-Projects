# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score
# pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {code['letter']: code['code'] for word, code in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


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
