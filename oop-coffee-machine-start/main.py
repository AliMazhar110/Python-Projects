from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()
while 1 == 1:
    choice = input("what would you like to have (/"+menu.get_items() + ") = ").lower()
    if choice == "off":
        break
    if choice == "report":
        coffee.report()
        money.report()
        continue
    check = menu.find_drink(choice)
    if coffee.is_resource_sufficient(check):
        if money.make_payment(check.cost):
            coffee.make_coffee(check)


