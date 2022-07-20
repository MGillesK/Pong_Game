from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align="center", font=("Courier", 30, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()