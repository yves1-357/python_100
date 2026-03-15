from snake import Snake
from food import Food
from score import Score
from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True

food = Food()
score = Score()
while is_game_on:
    snake.move_snake()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    
    if snake.segments[0].xcor() > 290  or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        is_game_on = False
        score.game_over()
    
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            is_game_on = False
            score.game_over()
        
    screen.update()
    time.sleep(0.1)

screen.exitonclick()