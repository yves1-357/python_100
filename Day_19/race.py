from turtle import Turtle, Screen
import random
Screen()
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
colors = ["red", "green", "orange", "blue", "yellowgreen", "sandybrown"]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


for i in range(0, 6):
    tim = Turtle(shape= "turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=-100 + (i * 40))
    all_turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_fowrad = random.randint(0, 10)
        turtle.forward(random_fowrad)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("Bravo vous avez gagné")
            else:
                print(f"Raté, La tortue {winning_color} à gagné ")
        

    

screen.exitonclick()
