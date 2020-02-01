from tkinter import *
import random

def guess(a):
    guess = int(E1.get())
    if guess > a:
        if guess > a + 20:
            L1['text'] = "너무 높아요"
        else:
            L1['text'] = "높아요"
    elif guess < a :
        if guess < a - 20:
            L1['text'] = "너무 낮아요"
        else:
            L1['text'] = "낮아요"
    else:
        L1['text'] = "정답!!"

def restart():
    global answer
    answer = random.randint(1,100)
    L1['text'] = ""
    
W = Tk()
answer = random.randint(1,100)

L1 = Label(W, text="")
L1.grid(row=0, column=0)

E1 = Entry(W, width=24, bg="yellow")
E1.grid(row=1, column=0, columnspan=2)

B1 = Button(W, width=10, text="숫자를 입력", command=lambda:guess(answer))
B2 = Button(W, width=14, text="게임을 다시 실행", command=restart)
B1.grid(row=2, column=0)
B2.grid(row=2, column=1)

W.mainloop()
