while 1 == 1:
    print("\nBand Name Generator\n")
    city = input("Enter your city name = ")
    pet_name = input("Enter your pet's name = ")
    print("Your band name could be : ", city, pet_name)

    status = input("\nDo you want to try again? (yes/no) = ")

    if status == "yes" or status == "Yes" or status == "YES" or status == "Y" or status == "y":
        continue
    else:
        break
