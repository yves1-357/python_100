from turtle import Turtle, Screen
import random

tim = Turtle()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
def draw_hirst():
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle() 

    # 1. On se place en bas à gauche (une seule fois)
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0) 
    start_x = tim.xcor()
    start_y = tim.ycor()
    for row in range(10):
        for _ in range(10):
            tim.dot(20, random_color()) 
            tim.forward(50) 

        new = start_y + (row + 1) * 50
        tim.goto(start_x, new)
        

screen = Screen()
screen.colormode(255)

draw_hirst()
screen.exitonclick()