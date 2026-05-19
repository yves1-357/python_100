from turtle import Turtle, Screen
import random

tim = Turtle()
directions = [0, 90, 180, 270]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
def walk():
    tim.pensize(20)
    tim.speed("fastest")
    while True:
        tim.color(random_color())
        tim.forward(30)
        angle = random.choice(directions)
        tim.setheading(angle)



screen = Screen()
screen.colormode(255)

walk()
screen.exitonclick()