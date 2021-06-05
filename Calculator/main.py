from art import logo
from os import system
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={"+":add,"-":subtract,"*":multiply,"/":divide}
def print_operations():
    for sym in operations:
        print(sym)
while 1==1:
    system("cls")
    print(logo)
    num1 = float(input("\nEnter first number = "))
    while 1==1:
        print_operations();
        operation_to_perform = input("Enter the operation you want to perform = ")
        num2 = float(input("Enter second number = "))
        answer = operations[operation_to_perform](num1,num2)
        print(f"{num1} {operation_to_perform} {num2} = {answer}")
        try_again = input("\nDo you want to continue(yes/no)? = ").lower()
        if try_again=="yes":
            num1 = answer
            continue
        else:
            break
    system("cls")
    start = input("\nDo you want to start a new calculation(yes/no)? = ").lower()
    if(start=="yes"):
        continue
    break