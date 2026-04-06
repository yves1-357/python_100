from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()
    

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Score : {self.l_score}", align="center", font=("Arial", 14, "bold"))
        self.goto(100, 200)
        self.write(f"Score : {self.r_score}", align="center", font=("Arial", 14, "bold"))

    def increase_left_score(self):
        self.l_score += 1
        self.update_score()
    
    def increase_right_score(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("Red")
        self.write("Game Over !", align="center", font=("Arial", 10, "bold"))
