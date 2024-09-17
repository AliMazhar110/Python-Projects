from turtle import Turtle
FONT = ("Courier", 20, "italic")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.pendown()

    def set_score(self):
        with open("data.txt", mode="r") as previous:
            self.high_score = previous.readline()
        self.update_scoreboard()

    def rewrite(self, new_score):
        with open("data.txt", mode="w") as previous:
            previous.write(str(new_score))
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.rewrite(self.score)
        self.score = 0
        self.set_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Game Over. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
