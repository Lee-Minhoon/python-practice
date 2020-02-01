print("연습문제 - 3/1번")
x=int(input("x: "))
y=int(input("y: "))
print("두수의 합 : ",x+y)
print("두수의 차 : ",x-y)
print("두수의 곱 : ",x*y)
print("두수의  평균 : ",(x+y)/2)
print("큰 수 : ",max(x,y))
print("작은 수 : ",min(x,y))
input("Enter를 치시오")

print()
print("연습문제 - 3/3번")
n=int(input("정수를 입력하시오: "))
a=n//1000   #1000의 자리수
b=n//100%10 #100의 자리수
c=n//10%10  #10의 자리수
d=n%10      #1의 자리수
s=a+b+c+d   #자리수의 합
print(a,b,c,d)
print("자리수의 합: ",s) 
input("Enter를 치시오")

print()
print("연습문제 - 3/4번") #5번 문제가 4번과 연결되어 4번도 풀게 되었습니다.
x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
dis=((x1-x2)**2+(y1-y2)**2)**0.5
x3=max(x1,x2)-min(y1,y2)
y3=max(y1,y2)-min(y1,y2)
print("두점 사이의 거리= ",dis)
input("Enter를 치시오")

print()
print("연습문제 - 3/5번")
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.lt(45)
t.fd(dis)
t.up()
t.goto(0,0)
t.setheading(0)
t.down()
t.fd(x3)
t.lt(90)
t.fd(y3)
print("일치한다.")
input("Enter를 치시오")
t.reset()

print()
print("연습문제 - 3/7번")
import time
x = time.time()
h = x//3600%24 #영국과 1시간 시차가 납니다. 어떤 부분이 잘못되었는지 잘모르겠습니다.
m = x//60%60
print("현재시간(영국 그리니치 시각): %d시%d분" %(h,m))
input("Enter를 치시오")

print()
print("연습문제 - 4/2번")
print("'apple'"+"'grape'")
print("'apple'"*3)
input("Enter를 치시오")

print()
print("연습문제 - 4/4번")
st = str(input("문자열을 입력하시오: "))
print(st + "하는 중")
input("Enter를 치시오")

print()
print("연습문제 - 4/6번")
on = float(input("1번째 숫자: "))
tw = float(input("2번째 숫자: "))
th = float(input("3번째 숫자: "))
fo = float(input("4번째 숫자: "))
lst = [on, tw, th, fo]
print(lst[0]+lst[1]+lst[2]+lst[3])
input("Enter를 치시오")

print()
print("연습문제 - 4/8번")
t.shape("turtle")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))
gotolist = [x1, y1, x2, y2, x3, y3]
for i in [1, 3, 5]:
    tw = t.towards(gotolist[i-1], gotolist[i])
    t.setheading(tw)
    t.goto(gotolist[i-1], gotolist[i])
input("Enter를 치시오")
t.reset()
