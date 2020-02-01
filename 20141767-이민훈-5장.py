import random
import turtle
import math

def five_three(a):
    if a >= 25:
        print("짧은바지를 입으세요")
    else:
        print("긴바지를 입으세요")
def five_five(a, b, c):
    if a-b == c:
        print("정답입니다.")
    else:
        print("오답입니다.")
def five_seven():
    gold = 0
    print("당첨번호는 {}입니다." .format(rn))
    if a1 == b1:
        gold = gold + 500000
    if a2 == b2:
        gold = gold + 500000
    return gold
def six_eight(a, b):
    for i in range(5):
        t.fd(a)
        t.rt(144)
    t.rt(b)
def six_ten(a):
    for i in range(a):
        t.fd(250)
        t.rt(90)
        t.fd(25)
        t.rt(90)
        t.fd(250)
        t.lt(90)
        t.fd(25)
        t.lt(90)

#======================================================
        
print("연습문제 - 5/3번")
temperature = int(input("현재 온도를 입력하시오: "))
five_three(temperature)
input("Enter를 치시오")

print()
print("연습문제 - 5/5번")
x = random.randint(1, 100)
y = random.randint(1, 100)
if x >= y:
    answer = int(input("{} - {} = " .format(x, y)))
    five_five(x, y, answer)
else:
    answer = int(input("{} - {} = " .format(y, x)))
    five_five(y, x, answer)
input("Enter를 치시오")

print()
print("연습문제 - 5/7번")
rn = random.randint(1, 99)
an = int(input("복권번호를 입력하시오(두자릿수): "))
a1 = rn // 10
a2 = rn % 10
b1 = an // 10
b2 = an % 10
gold = five_seven()
print("당첨 금액은 {}원입니다." .format(gold))
input("Enter를 치시오")

print()
print("연습문제 - 6/2번")
year = 0
balance = 1000

while balance <= 2000:
    year = year + 1
    interest = balance * 0.07
    balance = balance + interest
print(year, "년이 걸립니다.")
input("Enter를 치시오")
# while balance >= 2000:   ->   while balance <= 2000:
# while 반복문은 특정한 조건이 만족될때 무한루프를 돌기때문에
# 2천만원이상이라고 조건을 넣으면 조건이 만족되지않아 바로 빠져나와 0년이 나온다.
# 그러므로 관계연산자를 >= 에서 <= 로 수정하여야 한다.


print()
print("연습문제 - 6/4번")
answer = 0
while answer != 27:
    answer=int(input("3 * 9 = "))
print("맞았습니다.")
input("Enter를 치시오")

print()
print("연습문제 - 6/6번")
answer = "N"
while answer == "N":
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print("첫번째 주사위 = {} 두번째 주사위 = {}" .format(a, b))
    answer = str(input("그만 하실래요? Y/N: "))
input("Enter를 치시오")

print()
print("연습문제 - 6/8번")
dis = int(input("길이: "))
ang = int(input("각도: "))
re = int(input("횟수: "))
t = turtle.Turtle()
t.speed(0)
for i in range(re):
    six_eight(dis, ang)
input("Enter를 치시오")
t.reset()

print()
print("연습문제 - 6/10번")
t.shape("turtle")
t.up()
t.goto(-300, 300)
t.down()
re = int(input("횟수: "))
six_ten(re)
input("Enter를 치시오")
t.reset()

print()
print("연습문제 - 6/12번")
for i in range(360):
    sin = math.sin(3.14 * i / 180.0)
    t.goto(i, sin * 180)
input("Enter를 치시오")
t.reset()
# 6장 12번 문제는 수학을 잘하지 못해서 인터넷을 참고하였습니다..
