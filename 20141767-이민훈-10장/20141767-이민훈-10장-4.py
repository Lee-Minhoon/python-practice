from tkinter import *

def change():
    i = float(E1.get())
    c = i * 2.54
    L4['text'] = str(c)

W = Tk()

L1 = Label(W, text="인치를 센티미터로 변환하는 프로그램")
L1.grid(row=0, column=0, columnspan=2)
L2 = Label(W, width=15, text="인치를 입력하시오 : ")
L2.grid(row=1, column=0)
L3 = Label(W, width=15, text="변환결과 : ")
L3.grid(row=2, column=0)
L4 = Label(W, width=15, text="")
L4.grid(row=2, column=1)

E1 = Entry(W, width=15, bg="yellow")
E1.grid(row=1, column=1)

B1 = Button(W, text="변환!", command=change)
B1.grid(row=3, column=1)

W.mainloop()
