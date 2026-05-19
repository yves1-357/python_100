from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_game_on = True
coordonées_depart = [(0, 0),(-20, 0), (-40, 0)]
segments = []
for i in coordonées_depart:
    tim = Turtle(shape= "square")
    tim.color("white")
    tim.penup()
    tim.goto(i)
    segments.append(tim)

while is_game_on:
    for i in range(len(segments) - 1, 0 , -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)
    segments[0].forward(5)
    screen.update()
    time.sleep(0.1)




























screen.exitonclick()