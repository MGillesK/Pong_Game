from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position): # no need for paddle = Turtle() => inheritance => The code knows Paddle is a Turtle
        super().__init__() # important so the CPU understands where all the attributes come from (ie : xcor)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        y += 10
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor()
        y -= 10
        self.goto(self.xcor(), y)