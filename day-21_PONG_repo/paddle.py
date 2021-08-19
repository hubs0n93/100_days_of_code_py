from turtle import Turtle
PADDLE_SPEED = 20


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcor, ycor)

    def up(self):
        new_y = self.ycor() + PADDLE_SPEED
        if new_y < 300:
            self.goto(self.xcor(), new_y)
        else:
            pass

    def down(self):
        new_y = self.ycor() - PADDLE_SPEED
        if new_y > -300:
            self.goto(self.xcor(), new_y)
        else:
            pass
