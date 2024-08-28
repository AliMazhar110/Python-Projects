while 1 == 1:
    print("\nWelcome to tip calculator\n")

    amt = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
    people = int(input("How many people to split the bill? "))

    tip_percent = (tip/100)+1
    total = amt*tip_percent
    pay = round(total/people, 2)

    pay = "{:.2f}".format(pay)
    print(f"Each person should pay: ${pay}")

    status = input("\nDo you want to calculate again? (yes/no) = ")

    if status == "yes" or status == "Yes" or status == "YES" or status == "Y" or status == "y":
        continue
    else:
        break
