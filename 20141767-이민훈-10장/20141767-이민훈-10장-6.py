from tkinter import *
import random

def a():
    global P1
    global P2
    global P3
    global computer
    computer = random.randint(1, 3)
    L1.configure(image = P1)
    L1.image = P1
    if computer == 1:
        L3.configure(image = P1)
        L3.image = P1
        L4['text'] = "무승부"
    elif computer == 2:
        L3.configure(image = P2)
        L3.image = P2
        L4['text'] = "패배"
    else:
        L3.configure(image = P3)
        L3.image = P3
        L4['text'] = "승리"

def b():
    global P1
    global P2
    global P3
    global computer
    computer = random.randint(1, 3)
    L1.configure(image = P2)
    L1.image = P2
    if computer == 1:
        L3.configure(image = P1)
        L3.image = P1
        L4['text'] = "승리"
    elif computer == 2:
        L3.configure(image = P2)
        L3.image = P2
        L4['text'] = "무승부"
    else:
        L3.configure(image = P3)
        L3.image = P3
        L4['text'] = "패배"

def c():
    global P1
    global P2
    global P3
    global computer
    computer = random.randint(1, 3)
    L1.configure(image = P3)
    L1.image = P3
    if computer == 1:
        L3.configure(image = P1)
        L3.image = P1
        L4['text'] = "패배"
    elif computer == 2:
        L3.configure(image = P2)
        L3.image = P2
        L4['text'] = "승리"
    else:
        L3.configure(image = P3)
        L3.image = P3
        L4['text'] = "무승부"

W = Tk()
computer = random.randint(1, 3)

P1 = PhotoImage(file="a.gif")
P2 = PhotoImage(file="b.gif")
P3 = PhotoImage(file="c.gif")

L1 = Label(W, text="")
L1.grid(row=0, column=0)
L2 = Label(W, width=30, text="VS", font='helvetica 30')
L2.grid(row=0, column=1)
L3 = Label(W, text="")
L3.grid(row=0, column=2)
L4 = Label(W, text="결과", font='helvetica 30 bold')
L4.grid(row=1, column=0, columnspan=3)

B1 = Button(W, width=30, text="가위", command=a)
B1.grid(row=2, column=0)
B2 = Button(W, width=30, text="바위", command=b)
B2.grid(row=2, column=1)
B2 = Button(W, width=30, text="보", command=c)
B2.grid(row=2, column=2)

W.mainloop()

# 이미지 출처 : https://tgd.kr/169422
