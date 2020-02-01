from tkinter import *

def plus():
    global total
    plus = float(E1.get())
    total = total + plus
    L2['text'] = str(total)

def minus():
    global total
    minus = float(E1.get())
    total = total - minus
    L2['text'] = str(total)

def zero():
    plus = float(E1.get())
    L2['text'] = ""
    
W = Tk()
W.title("Calculator")
total = 0

L1 = Label(W, text="현재합계 : ")
L1.grid(row=0, column=0)

L2 = Label(W, text="")
L2.grid(row=0, column=1, columnspan=2)

E1 = Entry(W, width=24, bg="yellow")
E1.grid(row=1, column=0, columnspan=3)

B1 = Button(W, width=8, text="더하기", command=plus)
B2 = Button(W, width=8, text="빼기", command=minus)
B3 = Button(W, width=8, text="초기화", command=zero)
B1.grid(row=2, column=0)
B2.grid(row=2, column=1)
B3.grid(row=2, column=2)

W.mainloop()
