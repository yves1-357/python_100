from turtle import Turtle, Screen, forward
# from tk import tkinter
import random
tim = Turtle()


#Triangle
for _ in range(3): 
    tim.color('red')
    tim.forward(100)
    tim.left(120)

tim.right(random.randint(1, 360))
#Square
for _ in range(4):
    tim.color('blue')
    tim.forward(100)
    tim.left(90)

tim.right(random.randint(1, 360))

#Pentagon
for _ in range(4):
    tim.color("spring green")
    tim.forward(100)
    tim.right(72)

tim.right(random.randint(1, 360))
#Hexagon
for _ in range(6):
    tim.color("orange")
    tim.forward(90)
    tim.left(300)

tim.right(random.randint(1, 360))

#HEPTAGON
angle = 360/7
tim.left(angle/2)
tim.color("black")
for _ in range(6): 
    tim.right(angle)
    tim.forward(100)

tim.right(random.randint(1, 360))
#OCTAGON
for _ in range(7): 
    tim.color("yellow")
    tim.forward(100)
    tim.left(45)

tim.right(random.randint(1, 360))

#NONAGON
for _ in range(8):
    tim.color("purple")
    tim.forward(100)
    tim.left(40)

tim.right(random.randint(1, 360))

#DECAGON
for _ in range(9):
    tim.color("brown")
    tim.forward(100)
    tim.left(36)

tim.right(random.randint(1, 360))
    

    

   


































screen = Screen()
screen.exitonclick()
