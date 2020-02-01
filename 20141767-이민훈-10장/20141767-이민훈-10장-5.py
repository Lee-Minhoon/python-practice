from tkinter import *
import tkinter.messagebox

def show():
    a = str(E1.get())
    b = str(E2.get())
    c = str(E3.get())
    tkinter.messagebox.showinfo("정보", "이름:%s\n직업:%s\n국적:%s"%(a,b,c))

def quit():
    W.destroy()
    W.quit()

W = Tk()

L1 = Label(W, width=15, text="이름")
L1.grid(row=0, column=0, columnspan=2)
L2 = Label(W, width=15, text="직업")
L2.grid(row=1, column=0, columnspan=2)
L3 = Label(W, width=15, text="국적")
L3.grid(row=2, column=0, columnspan=2)

E1 = Entry(W, width=15, bg="yellow")
E1.grid(row=0, column=2)
E2 = Entry(W, width=15, bg="yellow")
E2.grid(row=1, column=2)
E3 = Entry(W, width=15, bg="yellow")
E3.grid(row=2, column=2)

B1 = Button(W, width=8, text="show", command=show)
B1.grid(row=3, column=0)
B2 = Button(W, width=7, text="quit", command=quit)
B2.grid(row=3, column=1)

W.mainloop()
