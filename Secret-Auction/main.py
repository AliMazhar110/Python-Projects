from art import logo
from os import system
print(logo)
biders={}

def add_to_biders(name,price):
    biders[name]=price
def find_highest_bidder():
    price_lst = list(biders.values())
    bider_lst = list(biders.keys())
    highest_price = sorted(price_lst,reverse=True)
    highest_bid=highest_price[0]
    position=price_lst.index(highest_bid)
    print("\nThe highest bidder is",bider_lst[position],"and the bid is $"+str(highest_bid))

print("Welcome to secret auction program")
while 1==1:
    name = input("\nWhat is your name? = ")
    price = int(input("Enter your bid = $"))
    check_for_other = input("Are there any other biders(yes/no)? = ").lower()
    add_to_biders(name,price)
    system('cls')
    if(check_for_other=="no"):
        break
    else:
        continue
find_highest_bidder()
