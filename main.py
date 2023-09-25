from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Tidy Up : Create a Snake, Food, and Scoreboard Class

snake = Snake()
food = Food()
score = Scoreboard()
snake_speed = 0.1

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake_speed)
    # time.sleep(0.1)

    snake.move()
    # Detect collision with food by comparing snake Turtle to food Turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        snake_speed *= 0.99

    # Detect collision with the wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        score.reset()
        snake.reset()

    # Detect collision with the tail - if head collides with any segment in the tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         score.game_over()
    #         game_is_on = False

    # Detect collision with the tail using slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
