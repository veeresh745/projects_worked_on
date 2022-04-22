#solved for karel_clear_1.jpg
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

for i in range(6):
    crosspath()



