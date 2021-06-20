import time
from turtle import Screen
from player import Player
from car_manager import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
# creating Player Instance
hero = Player()
# creating Cars Instance
cars = Cars()
# creating Scoreboard Instance
board = Scoreboard()
# UP Key
screen.onkeypress(hero.up, "Up")
# Down Key
screen.onkeypress(hero.down, "Down")
game_is_on = True
steps = 0
board.score()
t = 0.1
while game_is_on:
    time.sleep(t)
    if steps % 3 == 0:
        cars.create_cars()
    cars.move_cars()
    status = cars.collision(hero.return_hero())
    if status == -1:
        board.game_over()
        break
    steps += 1
    if hero.finished() == 1:
        board.increase_points()
        board.score()
        hero.to_home()
        t = t - 0.01
    screen.update()
screen.exitonclick()
