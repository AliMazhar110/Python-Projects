# day - 16
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# prettytable introduction
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

# day - 18
from turtle import *
import random
pablo = Turtle()
pablo.shape("turtle")
pablo.color("red", "green")

# building square
# for i in range(0, 4):
#     pablo.forward(100)
#     pablo.right(90)

# building dashed line
# for i in range(10):
#     pablo.forward(10)
#     pablo.penup()
#     pablo.forward(5)
#     pablo.pendown()

# making all the shapes in single go
# color = ["orange", "red", "yellow", "green", "brown", "purple", "pink", "black"]
# for i in range(3, 11):
#     pablo.pencolor(color[i-3])
#     for j in range(i):
#         pablo.forward(100)
#         pablo.right(360/i)


# random walk
# def left():
#     pablo.left(90)
#
#
# def right():
#     pablo.right(90)


# colormode(255)


# def get_colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_set = (r, g, b)
#     return color_set


# pablo.speed("fastest")
# pablo.pensize(10)
# direction = [left, right]
# direction = [0, 90, 180, 270]
# for i in range(100):
#     pablo.color(get_colors())
#     pablo.forward(20)
#     pablo.setheading(random.choice(direction))
#      random.choice(direction)()


# Spirograph
colormode(255)


def get_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_set = (r, g, b)
    return color_set


pablo.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        pablo.color(get_colors())
        pablo.circle(100)
        pablo.setheading(pablo.heading() + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
