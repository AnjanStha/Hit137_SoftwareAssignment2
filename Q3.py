# Question 3 
# Create a program that use recursive function to generates a tree pattern using Python's 
# turtle graphics. The program should take the following parameters from the user: 
# Left and right branch angles 
# Starting branch length 
# Recursion depth 
# Branch length reduction factor 
# Example: 
# The tree with branch left at 20 degrees and right at 25 degrees, starting with a branch 
# length of 100 pixels, and make each new branch 70% long as its parent branch, letting it 
# branch out 5 times.

import turtle
### setup parameters
# t = turtle
# s = turtle.Screen()
# s.title("Tree Pattern")
# s.bgcolor("White")
# s.screensize(800,500)
# t.pencolor("green")
# t.pensize(3)
# t.penup()  ## lift the pen up and doest not draw
# t.goto(0, -200)  # move pen to buttom
# t.left(90)
# t.pendown()


# #### parameters for user input
# left_angle = 20     # left angle
# right_angle = 25   #right angle
# starting_lenght = 100  #starting branch lenght
# branch_red = 0.7   #branch lenght reduction factor
# #recursion_depth  = 5 # Recursion depth6

# recursive function to draw tree
def Draw_tree(t,left_angle, right_angle, starting_lenght, branch_red, recursion_depth):

    if recursion_depth == 0 or starting_lenght < 1:
        return
   
    t.forward(starting_lenght)
    
    # Save current postion and head
    pos = t.position()
    heading = t.heading()

    # Draw left branch
    t.left(left_angle)
    Draw_tree(t,left_angle, right_angle, starting_lenght * branch_red, branch_red, recursion_depth -1)
    #input("pase for draw....1... Enter to continue")

    ## return to postion heading
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()
    #input("pase for draw....2... Enter to continue")


    ## Draw right Branch
    t.right(right_angle)
    Draw_tree(t,left_angle, right_angle, starting_lenght * branch_red, branch_red, recursion_depth -1)

     ## return to postion heading
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()
    #input("pase for draw....3... Enter to continue")

## input function for check 
def check_input(message,min, max = None):
    try:
        input_value = float(input(message))
        if(input_value >= min and ( max is None or input_value <= max)):
            return input_value
        else:
            print(f"Please enter value between {min} and {max} Value")

    except ValueError:
        print("Invalid input please enter value again")

def main():

    try:
        left_angle = check_input("Please enter left angle of Tree ",1, 180)
        right_angle = check_input("Please enter right angle of Tree ",1,180)
        starting_lenght = check_input("Please enter starting Branch length ",1)
        branch_red = check_input("Please enter the branch lenght reduction factor in Percentage % (70) ",1, 100)
        recursion_depth = check_input("Please enter Recursion depth of the Tree ",1)
        branch_red /= 100

        ### setup parameters45
        t = turtle
        s = turtle.Screen()
        s.title("Tree Pattern")
        s.bgcolor("White")
        s.screensize(800,500)
        t.pencolor("green")
        t.pensize(3)
        t.penup()  ## lift the pen up and doest not draw
        t.goto(0, -200)  # move pen to buttom
        t.left(90)
        t.pendown()

        ## Call recursive function to draw tree
        Draw_tree(t,left_angle, right_angle, starting_lenght, branch_red, recursion_depth)
        turtle.done()
    except ValueError:
         print("Invalid input please enter value again")



### Run when this file is executed
if __name__ == '__main__' :
    main()


    





