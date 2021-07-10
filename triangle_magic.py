# Using mathematics and probability, this programs creates a cool visualisation.
# The sequnece is as follows:
# There are three corners in a triangle. Each triangle with be assigned a number
# 1,2, or 3. Then the program will randomly generate a dot in the middle between
# the randomly genereated number and the previously placed dot.

# Import the files you created on the side.
# Note to self: Do not use classes yet. First just make sure it works as you wish.

# for random number  generator 
import random
from graphics import *
import math

def draw_user_triangle():
    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    vertices = [p1, p2, p3]

    # Use Polygon object to draw the triangle
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)

def introduction():
    print("Welcome to the program!")
    print("This program will show you an interesting phenomen.")


def get_triangle():
    print("For this experiment to work, we will need an equilateral triangle.")
    x_length = 0
    while (x_length < 100) or x_length > 800:
        try:
            x_length = int(input("Please enter the side length of an equilateral triangle. The value should be an integer between 100 and 800: "))
        except:
            pass
    y_length = x_length * math.sqrt(3)/2
    return x_length, y_length

def draw_dots():
    pass


def main():
    introduction()
    x_length, y_length = get_triangle()

    win = GraphWin('Draw a Triangle', x_length, y_length)
    win.setCoords(0, 0, x_length-1, y_length-1)
    win.setBackground('grey')

    # message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    #message.setTextColor('red')
    #message.setStyle('italic')
    #message.setSize(20)
    #message.draw(win)

    # Get and draw three vertices of triangle
    # Lower left, 1
    p1 = Point(0, 0)
    p1.draw(win)
    # Top middle, 2
    p2 = Point((x_length-1)/2, y_length)
    p2.draw(win)
    # Lower right, 3
    p3 = Point(x_length-1, 0)
    p3.draw(win)
    vertices = [p1, p2, p3]

    # Use Polygon object to draw the triangle
    triangle = Polygon(vertices)
    triangle.setFill('white')
    # triangle.setOutline('cyan')
    triangle.setWidth(2)  # width of boundary line
    triangle.draw(win)


    # Segment that draws new dots
    old_point_list = [0,0]
    count = 0
    while count < 1000:
        # Simulate dice roll
        dice_roll = random.randint(1,6)
        if dice_roll <= 2:
            compare_point = [0,0]
        elif dice_roll <= 4:
            compare_point = [(x_length-1)/2, y_length]
        else:
            compare_point = [x_length-1, 0]

        new_point_list = [(compare_point[0]+old_point_list[0])/2, (compare_point[1]+old_point_list[1])/2]
        new_point =  Point((compare_point[0]+old_point_list[0])/2, (compare_point[1]+old_point_list[1])/2)
        new_point.draw(win)
        old_point_list = new_point_list
        count = count + 1

    # message.setText('Click anywhere to quit') 
    # change text message
    # No text currently pops up
    win.getMouse()
    win.close()

main()
