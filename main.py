import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


player = Player()
screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.bgcolor("gray")
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()