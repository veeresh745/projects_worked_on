#for karel_3.png
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
        
        
            




