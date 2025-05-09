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

# recursive function to draw tree
def Draw_tree(t,left_angle, right_angle, starting_lenght, branch_red, recursion_depth, base_flag, mainBranch_lenght):

    if recursion_depth == 0 or starting_lenght < 1:
        t.penup()
        return
    ## for base line branch show red color and for other show green color
    t.pencolor("red" if base_flag else "green")
    
   
    t.forward(starting_lenght)
    
    # Save current postion and head
    pos = t.position()
    heading = t.heading()

    # Draw left branch
    ## tree_width calculate the width of the branch to reduce width for child branch
    tree_width = round(((starting_lenght - 1) / ( mainBranch_lenght - 1)) * 0.9 + 0.1, 2)

    t.pensize(5*tree_width)
    t.left(left_angle)
    Draw_tree(t,left_angle, right_angle, starting_lenght * branch_red, branch_red, recursion_depth -1, False,mainBranch_lenght)

    ## return to postion heading
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

    ## Draw right Branch
    ## calculate width of the branch 
    ## mianBranch_length is main orginal length of the base branch
    tree_width = round(((starting_lenght - 1) / ( mainBranch_lenght - 1)) * 0.9 + 0.1, 2)
    t.pensize(5*tree_width)
    t.right(right_angle)
    Draw_tree(t,left_angle, right_angle, starting_lenght * branch_red, branch_red, recursion_depth -1, False,mainBranch_lenght)

     ## return to postion heading
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

## input function for check user input
def check_input(message,min, max = None, default = None):
    try:
        input_value = input(message)
        if input_value == "":
            if default is not None:
                return default
        input_value = float(input_value)
        if(input_value >= min and ( max is None or input_value <= max)):
            return input_value
        else:
            print(f"Please enter value between {min} and {max} Value")

    except ValueError:
        print("Invalid input please enter value again")

def main():

    try:
        print("Pressure Enter to use default value")
        left_angle = check_input("Please enter left angle of Tree (default: 20): ", 1, 360, 20)
        right_angle = check_input("Please enter right angle of Tree (default: 25): ", 1, 360, 25)
        starting_lenght = check_input("Please enter starting Branch length (default: 100): ", 1, 1000, 100)
        branch_red = check_input("Please enter the branch length reduction factor in Percentage % (default: 70): ", 1, 100, 70)
        recursion_depth = check_input("Please enter Recursion depth of the Tree (default: 5): ", 1, 20, 5)
        branch_red /= 100

        ### setup parameters
        t = turtle
        s = turtle.Screen()
        s.title("Tree Pattern")
        s.bgcolor("White")
        s.screensize(800,500)
        t.pencolor("green")
        t.pensize(5) ### pen size or thickness
        t.penup()  ## lift the pen up and doest not draw
        t.goto(0, -200)  # move pen to buttom
        t.left(90)
        t.pendown()

        ## Call recursive function to draw tree
        Draw_tree(t,left_angle, right_angle, starting_lenght, branch_red, recursion_depth, True,starting_lenght)
        t.hideturtle() ## hide turtle arrow at the end 
        turtle.done()
    except ValueError:
         print("Invalid input please enter value again")



### Run when this file is executed
if __name__ == '__main__' :
    main()


    





