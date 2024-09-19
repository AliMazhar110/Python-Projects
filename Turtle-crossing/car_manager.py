from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Cars:
    def __init__(self):
        self.cars = []

    def create_cars(self):
        car = Turtle("square")
        car.penup()
        ind = randint(0, 5)
        car.color(COLORS[ind])
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        y = randint(-220, 220)
        car.goto(290, y)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(10)

    def collision(self, hero):
        for car in self.cars:
            if hero.distance(car.pos()) < 20:
                return -1
