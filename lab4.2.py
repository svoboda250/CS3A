#Assignment 4.2: Turtle Drawing: fun shapes
__author__ = 'Jenny Hamer'

import turtle
shape = turtle.Turtle()
shape.speed(10)
def my_shape(n, angle, length):
    for i in range(n):
        shape.fd(length)
        shape.rt(angle)

my_shape(99, 77, 111)

shape.penup()
shape.goto(-50, -100)
shape.pendown()

my_shape(100, 113, 140)

shape.penup()
shape.goto(140, 50)
shape.pendown()

my_shape(101, 67, 115)

shape.penup()
shape.goto(50, 110)
shape.pendown()

my_shape(200, 73, 100)
