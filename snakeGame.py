import random
import time
from turtle import *


class make_Snake:
    def __init__(self):
        self.speed = 0.5
        self.score = 0
        self.ycor = [0, -20, -40]
        self.blocks = []

    def make_the_body(self):
        for j in range(0, 3):
            head = Turtle(shape="square")
            head.color("white")
            head.penup()
            head.goto(0, self.ycor[j])
            self.blocks.append(head)
        self.head = self.blocks[0]

    def move(self):
        for i in range(len(self.blocks)-1, 0, -1):
            x_cor = self.blocks[i-1].xcor()
            y_cor = self.blocks[i-1].ycor()
            self.blocks[i].goto(x_cor, y_cor)
        self.head.forward(20)

    def add_block(self):
        head_0 = Turtle(shape="square")
        head_0.color("blue")
        head_0.penup()
        self.blocks.append(head_0)

    def up(self):
        if self.head.heading() != 270:
            print("w is pressed")
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)