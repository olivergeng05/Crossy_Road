from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()

    def write_score(self):
        self.goto(-280, 250)
        self.write(arg=f'Level: {self.score}', align='left', font=FONT)

    def update_score(self):
        self.clear()
        self.write_score()

    def score_up(self):
        self.score += 1

    def lose(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f'Game Over, Level: {self.score}', align='center', font=FONT)