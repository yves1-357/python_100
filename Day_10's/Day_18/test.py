from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colors = ["red", "blue", "spring green", "orange", "black", "AliceBlue", "purple", "brown", "pink", "teal"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):  # de 3 à 10 côtés
    tim.color(random.choice(colors))  # ou utilise colors[shape_side_n-3] pour garder l’ordre
    draw_shape(shape_side_n)
   

screen.exitonclick()