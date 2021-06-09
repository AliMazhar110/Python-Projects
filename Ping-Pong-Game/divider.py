from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")

    def timer(self, i):
        self.clear()
        self.write(i, align="center", font=("Courier", 80, "bold"))

    def clean(self):
        self.clear()

    def winner(self, left, r):
        if left > r:
            self.write("Winner Is Left Player.", align="center", font=("Courier", 20, "bold"))

        elif left < r:
            self.write("Winner Is Right Player.", align="center", font=("Courier", 20, "bold"))

        else:
            self.write("Draw.", align="center", font=("Courier", 20, "bold"))
