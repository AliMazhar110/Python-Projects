# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open(file="Input/Names/invited_names.txt", mode="r") as invited:
    names = invited.read()
guests = names.split()
with open(file="Input/Letters/starting_letter.txt", mode="r") as letter:
    promt = letter.read()
for name in guests:
    with open(file=f"Output/ReadyToSend/{name}.txt", mode="w") as sender:
        promt_copy = promt
        promt_copy = promt_copy.replace("[name]", name)
        sender.writelines(promt_copy)
        print("File created Successfully")
