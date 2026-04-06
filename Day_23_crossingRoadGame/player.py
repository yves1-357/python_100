from turtle import  Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.FINISH_LINE_Y = FINISH_LINE_Y

    def go_up(self):
        position_y = self.ycor()
        nouvelle_y = position_y + MOVE_DISTANCE
        self.goto(self.xcor(), nouvelle_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)



