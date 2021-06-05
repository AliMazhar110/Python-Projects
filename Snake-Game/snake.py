from turtle import Turtle


class Snake:
    turtles = []

    def __init__(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        if len(self.turtles) != 0:
            turtle.goto(self.turtles[-1].pos())
        self.turtles.append(turtle)

    def move_forward(self):
        for seq_num in range(len(self.turtles) - 1, 0, -1):
            self.turtles[seq_num].goto(self.turtles[seq_num - 1].pos())
        self.turtles[0].forward(20)

    def left(self):
        if self.turtles[0].heading() == 0:
            return
        self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() == 180:
            return
        self.turtles[0].setheading(0)

    def up(self):
        if self.turtles[0].heading() == 270:
            return
        self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() == 90:
            return
        self.turtles[0].setheading(270)

    def head(self):
        return self.turtles[0]

    def send_turtle(self, i):
        return self.turtles[i]
