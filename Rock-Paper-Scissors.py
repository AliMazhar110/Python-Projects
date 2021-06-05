import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("Type '0' for 'rock', '1' for 'paper' , '2' for scissors = "))
print("Your move - ")
if user_choice==0:
  print(rock)
elif user_choice==1:
  print(paper)
elif user_choice==2:
  print(scissors)
else:
  print("You Lose")
  quit()
comp_choice = random.randint(0,2)
print("Computer move - ")
if comp_choice==0:
  print(rock)
elif comp_choice==1:
  print(paper)
elif comp_choice==2:
  print(scissors)
if user_choice>comp_choice and user_choice-comp_choice != 2 or user_choice-comp_choice == -2:
  print("You Win!!!!")
elif comp_choice==user_choice: 
  print("Draw!!!")
else:
  print("You Lose!!!")
