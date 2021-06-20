from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.points = 0
        self.goto(-220, 270)

    def score(self):
        self.pendown()
        self.clear()
        self.write(f"Level: {self.points}", align="center", font=FONT)

    def increase_points(self):
        self.points += 1

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER.", align="center", font=FONT)
