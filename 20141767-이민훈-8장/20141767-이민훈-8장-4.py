import turtle
import math
import random
import sys

x = random.randint(100, 350)
p = turtle.Turtle()
p.shape("turtle")
p.penup()
p.goto(-350, 0)
p.pendown()

p1 = turtle.Turtle()
p1.shape("circle")
p1.shapesize(2)
p1.color("red")
p1.penup()
p1.goto(x, 0)
# 목표물 생성

def fire(a, b):
    for i in range(180):
        c = b / 100
        sin = math.sin(3.14 * i / 180)
        p.goto(i * (a / c) - 350, sin * b)
    if 30 > p.distance(p1.pos()):
        p.penup()
        p.goto(-350, 0)
        p.clear()
        p.color("blue")
        p.write("Victory! ", font=("Arial", 150, "italic"))
        # 목표물을 맞출시 승리하는 시스템입니다.
        p1.hideturtle()
        sys.exit()

s1 = turtle.textinput("", "발사 세기 : ")
s1 = int(s1)
s2 = turtle.textinput("", "발사 각도 : ")
s2 = int(s2)
# 발사 세기와 발사 각도를 입력받아 자동으로 발사되도록 설정 해보았습니다.

fire(s1, s2)
