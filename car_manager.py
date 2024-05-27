from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANT = 5
color_value = random.choice(COLORS)
y_random_value = random.randint(-250, 250)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=20/20, stretch_len=40/20)
        self.color(color_value)
        self.penup()
        self.goto(x=280, y=y_random_value)
