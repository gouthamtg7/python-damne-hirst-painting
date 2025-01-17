color_list = [
    (245, 190, 85),   # Warm yellow
    (182, 50, 75),    # Deep pink
    (120, 200, 215),  # Light cyan
    (240, 100, 100),  # Bright red
    (160, 215, 90),   # Lime green
    (75, 135, 220),   # Sky blue
    (255, 165, 0),    # Orange
    (200, 90, 150),   # Magenta
    (100, 190, 100),  # Mint green
    (225, 130, 60)    # Coral
]
import random
import turtle as t
from turtle import Turtle,Screen
timmy  = Turtle()
screen = Screen()
t.colormode(255)
def put_dot_and_move():
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    timmy.forward(50)
z =0
for i in range(7):
    timmy.setposition(0,-z)
    for j in range(7):
        put_dot_and_move()
    z+=50
screen.exitonclick()