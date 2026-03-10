from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

snake_shape = ((0, 0), (10, 5), (20, 0), (30, 5), (40, 0), (30, -5), (20, -10), (10, -5))
screen.register_shape("snake", snake_shape)

is_race_on = False
colors = ["red", "green", "orange", "blue", "yellowgreen", "sandybrown"]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for i in range(0, 6):
    tim = Turtle(shape="snake")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=-100 + (i * 40))
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_forward = random.randint(0, 10)
        turtle.forward(random_forward)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("Bravo vous avez gagné!")
            else:
                print(f"Raté, La tortue {winning_color} a gagné!")

screen.exitonclick()