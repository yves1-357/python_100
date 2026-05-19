import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()
counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter > 6:
        car_manager.create_car()
        counter = 0
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
            screen.update()

    if player.ycor() > player.FINISH_LINE_Y:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()




screen.exitonclick()














# screen.exitonclick()