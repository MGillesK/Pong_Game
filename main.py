from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # controls the animation. when turned to 0, animation is not visible

r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0)) #double bracket for the positon in the class Paddle
ball = Ball()
scoreboard_r = Scoreboard((150,250))
scoreboard_l = Scoreboard((-150, 250))

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="q", fun=l_paddle.move_up)
screen.onkey(key="a", fun=l_paddle.move_down)


game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.y_move *= -1

    if ball.xcor() >= 350 and ball.distance(r_paddle) < 50 or ball.xcor() <= -350 and ball.distance(l_paddle) < 50:
        ball.x_move *= -1.1

    if ball.xcor() > 380:
        scoreboard_l.increase_score()
        ball.goto(0,0)
        ball.x_move = -10

    if ball.xcor() < -380:
        scoreboard_r.increase_score()
        ball.goto(0, 0)
        ball.x_move = 10

screen.exitonclick()
