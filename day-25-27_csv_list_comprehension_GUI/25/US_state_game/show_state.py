from turtle import Turtle


class ShowState(Turtle):
    def __init__(self, state_name, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(position)
        self.write(arg=state_name, align="center", font=("Arial", 8, "normal"))

