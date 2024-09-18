from turtle import Turtle


class Paddle:
    def __init__(self, x):
        self.plate = Turtle("square")
        self.plate.color("white")
        self.plate.shapesize(stretch_wid=5, stretch_len=1)
        self.plate.penup()
        self.plate.goto(x)

    def go_up(self):
        if self.plate.ycor() < 240:
            self.plate.goto(self.plate.xcor(), self.plate.ycor() + 20)

    def go_down(self):
        if self.plate.ycor() > -240:
            self.plate.goto(self.plate.xcor(), self.plate.ycor() - 20)

    def return_turtle(self):
        return self.plate
