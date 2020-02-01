import turtle

def tg(n):
    color = ["red", "blue", "yellow", "green", "purple", "white", "black", "orange"]
    # 앞서 배운내용을 이용해 리스트에 색상들을 미리 저장하고 8가지 색상을 번갈아가며 사용하도록 설정하였습니다.
    
    a = 360/n
    for i in range(n):
        t.setheading(a*i-90)
        t.color("black", color[i%8])
        t.begin_fill()
        t.circle(100, -180)
        t.circle(200, a)
        t.left(180)
        t.circle(-100, -180)
        t.end_fill()

t = turtle.Turtle()
s = turtle.textinput("", "몇 등분한 태극무늬를 그리실래요?")
s = int(s)
# 2등분 된 태극문양을 변형하여 몇 등분한 태극무늬를 그릴지 정하여 그릴수있도록 코딩하였습니다.

t.pensize(3)
t.speed(0)

tg(s)

t.hideturtle()
