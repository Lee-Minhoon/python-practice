from tkinter import *

W = Tk()

L1 = Label(W, text="간단한 GUI 프로그램!")
L1.pack()

B1 = Button(W, text="환영합니다.")
B2 = Button(W, text="종료")
B1.pack()
B2.pack()

W.mainloop()
