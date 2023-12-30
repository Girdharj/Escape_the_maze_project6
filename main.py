"""Please visit the website to run the code"""

"""https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    if right_is_clear()!= True:
        while right_is_clear()!= True and at_goal()!= True:
            while wall_in_front() != True and at_goal()!= True:
                if right_is_clear()!= True and at_goal()!=True:
                    move()
                else:
                    turn_right()
                    if wall_in_front != True and at_goal()!=True:
                        move()                  
            if right_is_clear()== True and at_goal()!=True:
                turn_right()
                if wall_in_front != True:
                    move()
            else:
                turn_left()
    else:
        turn_right()
        while front_is_clear() == True:
            if at_goal()== True:
                break
            move()
        
