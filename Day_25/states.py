from turtle import Turtle, Screen
import pandas as pd 

screen = Screen()
screen.title("Us sates game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

writer = Turtle()
writer.penup()
writer.hideturtle() 

df = pd.read_csv("50_states.csv")
liste_states = df["state"].to_list()

guessed_states = []
missing_states = []

while len(guessed_states) < 50:
    answer_user = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_user in liste_states:
        guessed_states.append(answer_user)
        ligne_etat = df[df.state == answer_user]
        pos_x = ligne_etat.x.item()
        pos_y = ligne_etat.y.item()
        writer.goto(pos_x, pos_y)
        writer.write(answer_user)
    
    elif answer_user == "Exit":
        missing_states = [state for state in liste_states if state not in guessed_states]
        break
dv = pd.DataFrame(missing_states, columns=["États manquants"])
dv.to_csv("missing_states.csv", index=False)
print("Bravo, vous avez finit")


screen.exitonclick()

