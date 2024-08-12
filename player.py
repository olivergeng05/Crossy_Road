from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.seth(90)
        self.pu()
        self.start = (0, -280)
        self.finish_line = FINISH_LINE_Y
        self.goto(STARTING_POSITION)
        self.shape('turtle')

    def move_fd(self):
        self.fd(MOVE_DISTANCE)
