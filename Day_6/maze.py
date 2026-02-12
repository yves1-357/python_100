def turn_l():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
       turn_l()
       move()
    elif front_is_clear():
        move()
    else:
        turn_left()