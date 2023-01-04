import random
import time
from turtle import *
import snakeGame
import food
import scoreBoard

gameisOn = True
tracer(0)

screen = Screen()
screen.setup(1000, 700)
screen.bgcolor("black")

snake = snakeGame.make_Snake()
snake.make_the_body()
food = food.Food()
score = scoreBoard.Score()
while gameisOn:
    update()
    snake.move()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.left, "a")
    if snake.head.distance(food) < 18:
        food.goto(random.randint(-500, 500), random.randint(-350, 350))
        snake.add_block()
        score.increase_score_board()
    screen.listen()
    time.sleep(0.1)

screen.exitonclick()
