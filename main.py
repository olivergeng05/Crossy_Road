import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scoreboard.write_score()
    car_manager.make_car()
    for i in car_manager.all_car:
        i.fd(car_manager.speed)
        if player.distance(i) < 20 and i.ycor() - 10 < player.ycor() < i.ycor() + 10:
            scoreboard.lose()
            game_is_on = False
    screen.onkey(player.move_fd, 'Up')
    if player.ycor() > player.finish_line:
        scoreboard.score_up()
        car_manager.speed += car_manager.increment
        scoreboard.update_score()
        for i in car_manager.all_car:
            i.clear()
        player.goto(player.start)
    screen.update()

screen.exitonclick()
