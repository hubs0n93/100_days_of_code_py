from turtle import Turtle
BALL_SPEED = 0.08
BALL_ACCELERATION = 0.9


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_direction = 10
        self.x_direction = 10
        self.ball_speed = BALL_SPEED

    def wall_bounce(self):
        self.y_direction *= (-1)

    def x_direction_bounce(self):
        self.x_direction *= (-1)

    def move(self):
        x_cor = self.xcor() + self.x_direction
        y_cor = self.ycor() + self.y_direction
        self.goto(x_cor, y_cor)

    def reset_ball(self):
        self.goto(0, 0)
        self.x_direction_bounce()
        self.ball_speed = BALL_SPEED

    def accelerate_ball(self):
        self.ball_speed *= BALL_ACCELERATION