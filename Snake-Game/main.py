from turtle import Screen
from scoreboard import Score
import time

from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)
screen.listen()

turtles = []
for i in range(3):
    turtles.append(Snake())
food = Food()
score = Score()
screen.onkey(turtles[0].up, "Up")
screen.onkey(turtles[0].down, "Down")
screen.onkey(turtles[0].left, "Left")
screen.onkey(turtles[0].right, "Right")

game_is_on = True
i = 1

while game_is_on:
    screen.update()
    time.sleep(0.1)
    turtles[0].move_forward()
    t = turtles[0].head()

    # detect collision with food.
    if t.distance(food.pos()) < 15:
        score.add_score()
        food.position()
        turtles.append(Snake())

    # detect collision with wall.
    if t.xcor() > 280 or t.xcor() < -280 or t.ycor() > 280 or t.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with tail.
    for i in range(1, len(turtles)):
        if t.distance(turtles[0].send_turtle(i)) < 10:
            game_is_on = False
            score.game_over()

    # if head collision with any segment in the tail:
        # trigger game_over




screen.exitonclick()
