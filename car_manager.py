from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.increment = MOVE_INCREMENT
        self.all_car = []
        self.hideturtle()

    def make_car(self):
        if 1 == random.randint(1, 6):
            car = Turtle('square')
            car.color(COLORS[random.randint(0, 5)])
            car.pu()
            car.goto(300, random.randint(-250, 250))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.seth(180)
            self.all_car.append(car)

    def car_move(self):
        self.fd(self.speed)

    def faster(self):
        self.speed += MOVE_INCREMENT
