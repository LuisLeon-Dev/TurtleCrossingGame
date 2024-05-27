from turtle import Screen
import time
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)


player = Player()
car_manager = CarManager()

screen.onkey(player.go_up, key="Up")

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
