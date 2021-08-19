from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score_board_right = ScoreBoard(100)
score_board_left = ScoreBoard(-100)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    #Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.x_direction_bounce()
        ball.accelerate_ball()
    time.sleep(ball.ball_speed)

    #Ball goes out of bounds on right site
    if ball.xcor() > 400:
        ball.reset_ball()
        score_board_left.add_point()

    #Ball goes out on left site
    if ball.xcor() < -400:
        ball.reset_ball()
        score_board_right.add_point()












screen.exitonclick()

