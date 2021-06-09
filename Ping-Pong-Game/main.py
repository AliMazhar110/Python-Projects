from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
from divider import Divider
import time

screen = Screen()
screen.title("Ping-Pong-Game")
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.tracer(0)
screen.listen()

# creating paddle 1
r_paddle = Paddle((350, 0))
# creating paddle 2
l_paddle = Paddle((-350, 0))
# creating scoreboard
score = Score()
# creating divider object
div = Divider()

t = 0.05
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# creating ball
striker = Ball()
game_is_on = True
# getting rounds by users
stages = screen.numinput("Rounds", "Enter Number of Rounds: ", 3, minval=1, maxval=7)
# timer
for i in range(3, -1, -1):
    div.timer(i)
    screen.update()
    time.sleep(1)
div.clean()
# running infinite while loop
while game_is_on:
    screen.update()
    time.sleep(t)
    striker.move()
    # detect collision
    if striker.distance(striker.xcor(), 290) < 15 or striker.distance(striker.xcor(), -290) < 15:
        striker.collision()

    # detect collision with right-paddle
    if striker.distance(r_paddle.return_turtle()) < 45 and striker.xcor() > 320:
        t = t - 0.001
        striker.bounce()

    # detect collision with left-paddle
    if striker.distance(l_paddle.return_turtle()) < 45 and striker.xcor() < -320:
        t = t - 0.001
        striker.bounce()

    # detect when r_paddle misses
    if striker.xcor() > 390:
        stages -= 1
        t = 0.05
        score.add_point_to_left()
        if stages == 0:
            break
        striker.to_center()
        for i in range(3, -1, -1):
            div.timer(i)
            screen.update()
            time.sleep(1)
        div.clean()

    # detect when l_paddle misses
    if striker.xcor() < -390:
        stages -= 1
        t = 0.05
        score.add_point_to_right()
        if stages == 0:
            break
        striker.to_center()
        for i in range(3, -1, -1):
            div.timer(i)
            screen.update()
            time.sleep(1)
        div.clean()

# detect winner
div.winner(score.left_score(), score.right_score())

screen.exitonclick()
