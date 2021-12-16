from turtle import Screen, Turtle, position
from snake import Snake
import time

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BRu| Snake")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

screen.exitonclick()