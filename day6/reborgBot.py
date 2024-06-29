# Cracking the maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
# front_is_clear() or wall_in_front(),
# right_is_clear() or wall_on_right(), and at_goal().

def wall_on_left():
    turn_left()
    if wall_in_front():
        turn_right()
        return True
    turn_right()
    return False

while(not at_goal()):
    if not wall_on_left() and not wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
    
