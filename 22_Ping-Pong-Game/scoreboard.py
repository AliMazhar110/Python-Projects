from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "bold"))

    def add_point_to_right(self):
        self.r_score += 1
        self.update()

    def add_point_to_left(self):
        self.l_score += 1
        self.update()

    def left_score(self):
        return int(self.l_score)

    def right_score(self):
        return int(self.r_score)
