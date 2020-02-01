import turtle
import random
import time
import sys

def turnleft():
    p.lt(15)

def turnright():
    p.rt(15)

def booster():
    p.fd(10)
    
def play():
    a = random.randint(1, 10)
    p.fd(20)
    a1.fd(a*3)
    a1.left(random.randint(0, 120))
    a2.fd(a*3)
    a2.right(random.randint(0, 120))
    if a == 1:
        a1.hideturtle()
        x1 = random.randint(-300, 300)
        y1 = random.randint(-300, 300)
        a1.goto(x1, y1)
    elif a == 10:
        a2.hideturtle()
        x2 = random.randint(-300, 300)
        y2 = random.randint(-300, 300)
        a2.goto(x2, y2)
    else:
        a1.showturtle()
        a2.showturtle()
    # 랜덤함수를 이용하여 좀더 변칙적인 움직임을 가지도록 하였습니다.
    if 30 > p.distance(a1.pos()):
        p.write("패배!", False, "center", ("", 30))
        t2 = (time.time() - t1) * 100
        print("당신의 점수는 : {}" .format(int(t2)))
        sys.exit()
    elif 30 > p.distance(a2.pos()):
        p.write("패배!", False, "center", ("", 30))
        t2 = (time.time() - t1) * 100
        print("당신의 점수는 : {}" .format(int(t2)))
        sys.exit()
    screen.ontimer(play, 1)
    # 두 지점의 거리를 계속 비교하여 30 이내이면 패배하도록하였습니다.
    # 이전에 배운 time 함수를 이용해 1초당 100점의 점수를 주도록 하였습니다.

t1 = time.time()

p = turtle.Turtle()
p.color("blue")
p.shape("turtle")
p.penup()
p.speed(0)
screen = p.getscreen()
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(booster, "Up")
screen.listen()

a1 = turtle.Turtle()
a1.color("red")
a1.shape("circle")
a1.shapesize(2)
a1.penup()
a1.speed(0)
x1 = random.randint(-300, 300)
y1 = random.randint(-300, 300)
a1.goto(x1, y1)

a2 = turtle.Turtle()
a2.color("red")
a2.shape("circle")
a2.shapesize(2)
a2.penup()
a2.speed(0)
x2 = random.randint(-300, 300)
y2 = random.randint(-300, 300)
a2.goto(x2, y2)

play()
