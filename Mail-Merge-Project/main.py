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
