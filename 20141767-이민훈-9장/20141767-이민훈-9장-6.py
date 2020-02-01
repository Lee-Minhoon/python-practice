import turtle
import random

def draw_star():
    color = ["red", "blue", "yellow", "green", "orange", "purple", "skyblue"]
    rand = random.randint(0, 6)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(50, 150)
    t.penup()
    t.color(color[rand])
    t.fillcolor(color[rand])
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(10):
        t.fd(size)
        t.rt(144)
    t.end_fill()

#===========================================================

t = turtle.Turtle()
t.speed(0)
s = turtle.getscreen()
s.bgcolor("Black")

a = turtle.textinput("", "도형 몇개를 그려보실래요?")
a = int(a)

for i in range(a):
    draw_star()
