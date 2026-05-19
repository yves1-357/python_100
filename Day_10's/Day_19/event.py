from turtle import Turtle, Screen
Screen()
tim = Turtle()


def move_forwards():
    tim.forward(10)
    

def move_backwards():
    tim.backward(10)
    

def move_counter_clockwise():
    tim.left(10)
    

def move_right():
    tim.right(10)
    

def delete_move():
    tim.clear()
    tim.home()
    
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=delete_move)


screen.exitonclick()
