from turtle import Turtle
FONT = ("Courier", 12, "bold")
Level = 1 


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = Level
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.color("Red")
        self.write("Game Over !", align="center", font=FONT)

