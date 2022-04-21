#solved thfor karel_2.jpg
#This time karel don't know where the flag is
# so i have used while loop to chaeck whether it is at goal
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

def crosspath():
    move()
    jump()

while not at_goal():
    crosspath()



