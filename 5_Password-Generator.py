# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

while 1 == 1:

    print("\nWelcome to the PyPassword Generator!\n")
    nr_letters = int(input("How many letters would you like in your password? = "))
    nr_symbols = int(input("How many symbols would you like? = "))
    nr_numbers = int(input("How many numbers would you like? = "))

    password = []
    for i in range(0, nr_letters):
        choice = random.randint(0, len(letters)-1)
        password.append(letters[choice])

    for i in range(0, nr_symbols):
        choice = random.randint(0, len(symbols)-1)
        password.append(symbols[choice])

    for i in range(0, nr_numbers):
        choice = random.randint(0, len(numbers)-1)
        password.append(numbers[choice])

    random.shuffle(password)
    passwordString = "".join(password)
    print(passwordString)

    status = input("\nWant to create another password? (yes/no) = ")

    if status == "yes" or status == "Yes" or status == "YES" or status == "Y" or status == "y":
        continue
    else:
        break
