from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

        
    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        nouvelle_x = new_x + self.x_move
        nouvelle_y = new_y + self.y_move
        self.goto(nouvelle_x, nouvelle_y)

    def bounce_y(self):
        self.y_move = self.y_move *-1

    def bounce_x(self):
       self.x_move = self.x_move *-1 
       self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


