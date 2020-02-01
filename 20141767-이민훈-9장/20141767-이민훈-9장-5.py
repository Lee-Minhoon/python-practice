import turtle
import random

def draw_circle():
    color = ["red", "blue", "yellow", "green", "orange", "purple", "skyblue"]
    rand = random.randint(0, 6)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.fillcolor(color[rand])
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

def draw_three():
    color = ["red", "blue", "yellow", "green", "orange", "purple", "skyblue"]
    rand = random.randint(0, 6)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.fillcolor(color[rand])
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.fd(50)
        t.lt(120)
    t.end_fill()

def draw_four():
    color = ["red", "blue", "yellow", "green", "orange", "purple", "skyblue"]
    rand = random.randint(0, 6)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.fillcolor(color[rand])
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.lt(90)
    t.end_fill()

def draw_five():
    color = ["red", "blue", "yellow", "green", "orange", "purple", "skyblue"]
    rand = random.randint(0, 6)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.fillcolor(color[rand])
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.fd(50)
        t.lt(72)
    t.end_fill()

def draw_six():
    color = ["red", "blue", "yellow", "green", "orange", "purple", "skyblue"]
    rand = random.randint(0, 6)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.fillcolor(color[rand])
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(6):
        t.fd(50)
        t.lt(60)
    t.end_fill()

#===========================================================

t = turtle.Turtle()
t.color("Black")
t.speed(0)

s = turtle.textinput("", "도형 몇개를 그려보실래요?")
s = int(s)

for i in range(s):
    if 0 == random.randint(0, 4):
        draw_circle()
    elif 1 == random.randint(0, 4):
        draw_three()
    elif 2 == random.randint(0, 4):
        draw_four()
    elif 3 == random.randint(0, 4):
        draw_five()
    else:
        draw_six()
