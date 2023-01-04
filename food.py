import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.x_cor = random.randint(-500, 500)
        self.y_cor = random.randint(-350, 350)
        self.goto(self.x_cor, self.y_cor)
