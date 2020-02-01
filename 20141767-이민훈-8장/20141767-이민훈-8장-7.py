import turtle
import math

def draw_circle(x, y):
    turtle.penup()
    turtle.color("Black")
    turtle.fillcolor("red")
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def draw_rectangle():
    turtle.penup()
    turtle.color("Black")
    turtle.fillcolor("brown")
    turtle.goto(-15, 0)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(30)
        turtle.lt(90)
        turtle.fd(50)
        turtle.lt(90)
    turtle.end_fill()

def draw_trepezoid():
    x = -200 # 최초 x값
    y = 50 # 최초 y값
    for i in range(0, 11, 1): 
        turtle.penup()
        turtle.color("Black")
        turtle.fillcolor("Green")
        vertex1x = x + i * 15 # 최초 지점 x값
        vertex1y = y + i * 20 # 최초 지점 y값
        turtle.goto(vertex1x, vertex1y) # 최초 지점으로 이동 (왼쪽 아래 꼭짓점)
        
        bottom = vertex1x * -2 # 아랫변 길이
        top = bottom - 30 # 윗변 길이
        vertex2x = bottom / 2 - 15 # 윗변 오른쪽 꼭짓점 x값
        vertex2y = y + (i+1) * 20 # 윗변 오른쪽 꼭짓점 y값
        
        turtle.pendown()
        turtle.begin_fill()
        turtle.fd(bottom) # 아랫변 긋기
        
        ang1 = turtle.towards(vertex2x, vertex2y) # 윗변 오른쪽 꼭짓점을 보는 각도
        dis1 = turtle.distance(vertex2x, vertex2y) # 윗변 오른쪽 꼭짓점 까지의 거리
        turtle.setheading(ang1) # 방향 바꾸기
        turtle.fd(dis1) # 전진
        
        turtle.setheading(180) # 방향 바꾸기
        turtle.fd(top) # 윗변 긋기
        
        ang2 = turtle.towards(vertex1x, vertex1y) # 최초 지점을 보는 각도
        dis2 = turtle.distance(vertex1x, vertex1y) # 최초 지점 까지의 거리
        turtle.setheading(ang2) # 방향 바꾸기
        turtle.fd(dis2) # 전진
        
        turtle.setheading(0) # 방향 바꾸기
        turtle.end_fill()
        # 사다리꼴 그리는법을 새로 변형 해보았습니다.

def draw_star():
    turtle.penup()
    turtle.color("Black")
    turtle.fillcolor("yellow")
    turtle.goto(-50, 330)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(10):
        turtle.fd(100)
        turtle.right(144)
    turtle.end_fill()

def draw_write():
    turtle.penup()
    turtle.color("red")
    turtle.goto(-200,250)
    turtle.write("Merry Christmas", font=("Arial", 24, "italic"))
    turtle.goto(-200,220)
    turtle.write("Happy New Year!", font=("Arial", 24, "italic"))

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.speed(0)
screen = turtle.getscreen()
screen.onkeypress(draw_rectangle, "Down")
screen.onkeypress(draw_trepezoid, "Up")
screen.onkeypress(draw_star, "Left")
screen.onkeypress(draw_write, "Right")
# 배웠던 키입력 함수를 통해서 트리를 그릴 수 있도록 하였습니다.
screen.onscreenclick(draw_circle)
screen.listen()

print("위쪽 방향키를 누르면 잎이 그려집니다.")
print("아래쪽 방향키를 누르면 줄기가 그려집니다.")
print("왼쪽 방향키를 누르면 별이 그려집니다.")
print("오른쪽 방향키를 누르면 글씨가 새겨집니다.")
print("마우스 클릭을 하면 클릭한 곳에 장식이 달립니다")
