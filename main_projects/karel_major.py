#in this challenge, karel can face any direction and when i
#hit run button it will start fron any direction, any position randomly
#and i have solved a major bug as well, where in certain condition
#karel was going in infinite loop
#image karel_final.png
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()





