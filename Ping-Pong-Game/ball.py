from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def collision(self):
        if self.ycor() > 0:
            self.y_move = -10
        elif self.ycor() < 0:
            self.y_move = 10

    def bounce(self):
        if self.xcor() > 0:
            self.x_move = -10
        elif self.xcor() < 0:
            self.x_move = 10

    def to_center(self):
        self.goto(0, 0)
