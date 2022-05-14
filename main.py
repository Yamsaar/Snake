from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# initiate objects from classes
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_not_over = True
while game_not_over:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    """ how to detect collision with the wall """
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game_not_over = False
        score.game_over()

    """ how to detect collision with food """
    if snake.head.distance(food) < 15:
        food.refresh_positions()
        snake.extend()
        score.increase_score()

    """ how to detect collision with tail """
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_not_over = False
            score.game_over()

screen.exitonclick()
