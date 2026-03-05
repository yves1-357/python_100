from turtle import Turtle, Screen
import random

tim = Turtle()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def circle(size):
    tim.pensize(1)
    tim.speed("fastest")
    for i in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)
        

screen = Screen()
screen.colormode(255)

circle(5)
screen.exitonclick()