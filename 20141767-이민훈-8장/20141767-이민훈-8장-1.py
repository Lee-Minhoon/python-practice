import random
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()

t1.color("red")
t2.color("green")
t3.color("blue")
t4.color("black")
# 총 4마리의 거북이가 경주하는것을 만들어보았습니다.

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")

t1.shapesize(3)
t2.shapesize(3)
t3.shapesize(3)
t4.shapesize(3)

t1.pensize(3)
t2.pensize(3)
t3.pensize(3)
t4.pensize(3)

t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)

def race():
    a = [0, 0, 0, 0]
    b = ["빨간색", "초록색", "파란색", "검은색"]
    
    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    
    t1.goto(-450,150)
    t2.goto(-450,50)
    t3.goto(-450,-50)
    t4.goto(-450,-150)

    t1.pendown()
    t2.pendown()
    t3.pendown()
    t4.pendown()
    
    for i in range(20):
        d1 = random.randint(1, 50)
        d2 = random.randint(1, 50)
        d3 = random.randint(1, 50)
        d4 = random.randint(1, 50)
        
        t1.forward(d1)
        t2.forward(d2)
        t3.forward(d3)
        t4.forward(d4)

        a[0] += d1
        a[1] += d2
        a[2] += d3
        a[3] += d4

    if max(a) == a[0]:
        print("1등은 : {} 거북이" .format(b[0]))
    elif max(a) == a[1]:
        print("1등은 : {} 거북이" .format(b[1]))
    elif max(a) == a[2]:
        print("1등은 : {} 거북이" .format(b[2]))
    else:
        print("1등은 : {} 거북이" .format(b[3]))
    # 1등을 한 거북이가 어떤거북이인지 출력되도록 하였습니다.

s = "Y"

while s == "Y":
    race()
    s = turtle.textinput("", "다시 하실래요? Y/N")
    t1.clear()
    t2.clear()
    t3.clear()
    t4.clear()
    # 게임을 다시 진행하고싶다면 Y를 입력시 반복되도록 코딩하였습니다.

t1.reset()
t2.reset()
t3.reset()
t4.reset()

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
# 교수님 거북이는 for문을 이용한 배열로 만들수 없는지 궁금합니다.
