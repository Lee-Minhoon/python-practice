import turtle
import random

def draw_square(x, y):
    color = ["red", "blue", "yellow", "green", "orange", "purple", "skyblue"]
    rand = random.randint(0, 6)
    t.penup()
    t.fillcolor(color[rand])
    t.goto(x-25, y-25)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.lt(90)
    t.end_fill()

#===========================================================

t = turtle.Turtle()
t.shape("turtle")
t.color("Black")
t.speed(0)
screen = t.getscreen()
screen.onscreenclick(draw_square)
screen.listen()

