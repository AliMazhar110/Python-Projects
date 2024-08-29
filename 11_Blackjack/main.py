from art import logo
import random
from os import system


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def score(lst):
    if sum(lst) > 21 and 11 in lst:
        lst.remove(11)
        lst.append(1)
    return sum(lst)


def print_score(player, dealer):
    print("\nYour cards =", player, "  Current Score =", score(player))
    print("Computer's Cards = ", dealer, " Computer's Score =", score(dealer))


while 1 == 1:
    system('cls')
    print(logo)
    user_cards = []
    dealer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    finish = False
    
    while not finish:
        print("\nYour cards =", user_cards, "  Current Score =", score(user_cards))
        print("Computer's First Card = ", dealer_cards[0])

        if score(user_cards) < 21:
            choice = input("\nHit or Stand = ").lower()
            if choice == "hit":
                user_cards.append(deal_card())
                continue
            elif choice == "stand":
                while score(dealer_cards) < 17:
                    dealer_cards.append(deal_card())
                print_score(user_cards, dealer_cards)

                if score(dealer_cards) > 21:
                    print("\nBUST. You Won.")
                elif score(dealer_cards) == 21 and len(dealer_cards) == 2:
                    print("\nBlackJack. You Lose.")
                elif score(user_cards) > score(dealer_cards):
                    print("\nYou Won.")
                elif score(user_cards) < score(dealer_cards):
                    print("\nYou Lost.")
                else:
                    print("\nDraw.")

                finish = True

        elif score(user_cards) > 21:
            print("\nBUST. You got carried away.")
            finish = True

        else:
            if score(dealer_cards) == 21:
                print_score(user_cards, dealer_cards)

                if len(user_cards) == 2 and len(dealer_cards) == 2:
                    print("\nDraw")
                elif len(user_cards) == 2:
                    print("\nBlackJack. You Win.")
                elif len(dealer_cards) == 2:
                    print("\nBlackJack. You Lose.")
                else:
                    print("\nDraw.")

            elif len(user_cards) == 2:
                print_score(user_cards, dealer_cards)
                print("\nBlackjack. You Won.")

            else:  
                while score(dealer_cards) < 17:
                    dealer_cards.append(deal_card())

                print_score(user_cards, dealer_cards)

                if score(dealer_cards) > 21:
                    print("\nBUST. You win.")
                else:
                    print("\nYou Win.")
            finish = True

    again = input("\nDo you want to play again(y/n) = ").lower()

    if again != 'y' :
        break
    else:
        continue
