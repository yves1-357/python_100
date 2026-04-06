from turtle import Screen, Turtle
from pong import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "q")
ball = Ball()
score = Score()
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 340:
        print("Point à gauche !")
        ball.reset_position()
        score.increase_left_score() 
    
    if  ball.xcor() < -340:
        print("Point à droite !")
        ball.reset_position()
        score.increase_right_score()
    
    if score.l_score > 10 or score.r_score > 10:
        is_game_on = False
        score.game_over()
        screen.update()
    
    ball.move()
    screen.update()
    



























screen.exitonclick()