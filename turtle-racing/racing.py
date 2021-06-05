from turtle import Turtle, Screen
import random

# to check if the user has entered the bet
race_is_on = False

# creating turtles object
meliodas = Turtle("turtle")
ban = Turtle("turtle")
escanor = Turtle("turtle")
gowther = Turtle("turtle")
king = Turtle("turtle")
diane = Turtle("turtle")
colours = ["red", "green", "orange", "purple", "yellow", "blue"]
turtles = [meliodas, ban, escanor, gowther, king, diane]

# screen object
screen = Screen()
screen.setup(width=800, height=500)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter the color: ")

# filling colors in turtles
for i in range(len(colours)):
    turtles[i].penup()
    turtles[i].fillcolor(colours[i])

# arranging turtles to the starting point
count = 0
for i in range(-200, 250, 75):
    turtles[count].goto(x=-360, y=i)
    count += 1

winner = " "
# check user_bet
if user_bet:
    race_is_on = True
while race_is_on:
    random_index = random.randint(0, 5)
    turtles[random_index].forward(5)
    for t in turtles:
        if t.xcor() == 400:
            winner = t
            break
    if winner != " ":
        break

# checking for winner
if winner.fillcolor() == user_bet:
    print("You won.", end=" ")
else:
    print("You Lost.", end=" ")
print("Winner is", winner.fillcolor())

# screen will not close automatically
screen.exitonclick()

