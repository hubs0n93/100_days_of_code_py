from turtle import Turtle
FONT = ("Courier", 32, "normal")


class ScoreBoard(Turtle):

    def __init__(self, x_score_position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(x_score_position, 250)
        self.write_score()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(arg=f"{self.score}", font=FONT)
