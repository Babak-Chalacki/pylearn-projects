import turtle
import random

lineMaker = turtle.Turtle()
lineMaker.speed(0)

number_of_sides = 3
forward_length = 60

while number_of_sides <= 10:
    lineMaker.pencolor(random.random(), random.random(), random.random())
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        lineMaker.forward(forward_length)
        lineMaker.left(angle)
    
    forward_length += 10
    lineMaker.penup()
    lineMaker.goto(0, -10 * number_of_sides)
    lineMaker.pendown()
    number_of_sides += 1

turtle.done()