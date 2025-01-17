import turtle as t
from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
t.colormode(255)
colors = (0,0,0)
tim.speed("fastest")
tim.width(2)
def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    colors = (r,b,g)
    return colors
def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        new_heading = current_heading + size_of_gap
        tim.setheading(new_heading)
spirograph(10)
screen.exitonclick()
