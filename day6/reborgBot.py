# Cracking the maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
# front_is_clear() or wall_in_front(),
# right_is_clear() or wall_on_right(), and at_goal().

while(not at_goal()):
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif right_is_clear():
        turn_right()
