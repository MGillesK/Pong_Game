from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self): # no need for paddle = Turtle() => inheritance => The code knows Paddle is a Turtle
        super().__init__() # important so the CPU understands where all the attributes come from (ie : xcor)
        self.shape("circle")
        # self.shapesize(stretch_wid=2, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.speed("slow")
        self.y_move = 10
        self.x_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # def wall_bounce(self):
    #     # always check first!!! The code stays in move function
    #     self.y_move *= -1  # and does not use the __init__ anymore
    #
    # def paddle_bounce(self):
    #     self.x_move *= -1
    # def reset_position(self):
    #     ball.goto(0, 0)
    #     ball.x_move = 10