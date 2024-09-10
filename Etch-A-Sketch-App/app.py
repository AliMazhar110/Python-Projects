from turtle import Turtle, Screen

adam = Turtle()
adam.pensize(5)
adam.fillcolor("red")
adam.pencolor("yellow")


def front():
    adam.forward(10)


def back():
    adam.back(10)


def clockwise():
    adam.right(10)


def counter():
    adam.left(10)


def clean():
    adam.clear()
    adam.penup()
    adam.home()
    adam.pendown()


screen = Screen()
screen.listen()
screen.onkey(front, "w")
screen.onkey(back, "s")
screen.onkey(counter, "a")
screen.onkey(clockwise, "d")
screen.onkey(clean, "c")
screen.exitonclick()
