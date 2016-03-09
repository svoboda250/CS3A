"""Assignment 4.1: Turtle House: draw a house using the turtle module"""
__author__ = 'Jenny Hamer'

import turtle
house = turtle.Turtle()


def squares(length):
    for i in range(4):
        house.fd(length)
        house.lt(90)

def house_block(height, base):
    for i in range(2):
        house.fd(base)
        house.lt(90)
        house.fd(height)
        house.lt(90)
        
"""
ended up not using function
def roof_triangle(length): # all sides are same length, therefore all angles are equivalent
    for i in range(2):
        house.fd(length)
        house.lt(60)
"""        
        

house.penup()
house.goto(100, -100) # starting location for drawing
house.pendown()
house.lt(180)
house_block(50, 200)

turtle.update()

house.rt(60)
house.fd(200)
house.lt(120)
house.fd(200)
#roof_triangle(200) --> didn't work well, so drew step by step

turtle.update()

house.rt(60)
house.penup()
house.goto(80, -110)
house.pendown()
squares(30)

turtle.update()

house.penup()
house.goto(-50, -110)
house.pendown()
squares(30)

turtle.update()
