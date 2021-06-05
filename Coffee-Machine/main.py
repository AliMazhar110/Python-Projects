from data import *
from os import system
money = 0.0


def make_coffee(ch):
    if ch == "espresso":
        resources["water"] = resources["water"] - MENU[ch]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[ch]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[ch]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[ch]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU[ch]["ingredients"]["milk"]
    print(f"\nYour {ch}☕ is ready. Enjoy!!")


def count_money(ch):
    lst_currency = [("quarters", 0.25),
                    ("dimes", 0.10),
                    ("nickles", 0.05),
                    ("pennies", 0.01)]
    print("\nEnter Money - ")
    m = 0
    for i in lst_currency:
        p = float(input(f"Enter number of {i[0]} = "))
        m = m + (p * i[1])
    print("paid = "+m)
    if m > MENU[ch]["cost"]:
        return m - MENU[ch]["cost"]
    elif m == MENU[ch]["cost"]:
        return 0
    else:
        return -1


def report():
    for k, v in resources.items():
        print(f"{k} : {v}")
    print("Money :", money)


def refill():
    resources["water"] = 300
    resources["coffee"] = 100
    resources["milk"] = 200


def check_for_ingredients(ch):
    if ch == "espresso":
        if resources["water"] < 50:
            print("Less Water.")
        if resources["coffee"] < 18:
            print("Less Coffee.")
        if resources["milk"] < 150:
            print("Less Milk")
    elif ch == "latte":
        if resources["water"] < 200:
            print("Less Water.")
        if resources["coffee"] < 24:
            print("Less Coffee.")
        if resources["milk"] < 150:
            print("Less Milk.")
    elif ch == "cappuccino":
        if resources["water"] < 250:
            print("Less Water.")
        if resources["coffee"] < 24:
            print("Less Coffee.")
        if resources["milk"] < 100:
            print("Less Milk.")


while 1 == 1:
    system('cls')
    choice = input("What would you like to have(espresso/latte/cappuccino) = ").lower()
    if choice == "stop":
        break
    elif choice == "refill":
        refill()
        continue
    elif choice == "report":
        report()
        continue
    if resources["water"] < 50 or resources["coffee"] < 18:
        print("\nMachine Need Refill 😓.")
        check_for_ingredients(choice)
        continue
    elif choice == "latte":
        if resources["water"] < 200 or resources["coffee"] < 24 or resources["milk"] < 150:
            print("\nDon't have enough supply for latte. You can go with espresso😁.")
            check_for_ingredients(choice)
            continue
    elif choice == "cappuccino":
        if resources["water"] < 250 or resources["coffee"] < 24 or resources["milk"] < 100:
            print("\nDon't have enough supply for cappuccino. You can go with espresso or latte😁.")
            check_for_ingredients(choice)
            continue
    paid = count_money(choice)
    if paid != -1:
        print("Money return =", round(paid, 2))
        money = money + MENU[choice]["cost"]
    elif paid == -1:
        print("\nNot Enough Money. Money Refunded.")
        continue
    make_coffee(choice)
    continue
