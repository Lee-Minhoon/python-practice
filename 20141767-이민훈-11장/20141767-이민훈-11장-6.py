from tkinter import *
import pickle

setup = open("phone_book.dat", "wb")
setup.close()

def plus():
    global phone_book
    ent1 = str(E1.get())
    ent2 = str(E2.get())
    phone_book[ent1] = ent2
    E1.delete(0, END)
    E2.delete(0, END)
    a = open("phone_book.dat", "rb+")
    pickle.dump(phone_book, a)
    a.close()

def start():
    global phone_book
    global idx
    phone_name = list(phone_book.keys())
    phone_number = list(phone_book.values())
    idx = 0
    E1.delete(0, END)
    E2.delete(0, END)
    E1.insert(0, phone_name[idx])
    E2.insert(0, phone_number[idx])

def nxt():
    global phone_book
    global idx
    phone_name = list(phone_book.keys())
    phone_number = list(phone_book.values())
    if idx+1 == len(phone_name):
        print("마지막입니다.")
    else:
        idx += 1
        E1.delete(0, END)
        E2.delete(0, END)
        E1.insert(0, phone_name[idx])
        E2.insert(0, phone_number[idx])

def bck():
    global phone_book
    global idx
    phone_name = list(phone_book.keys())
    phone_number = list(phone_book.values())
    if idx == 0:
        print("처음입니다.")
    else:
        idx -= 1
        E1.delete(0, END)
        E2.delete(0, END)
        E1.insert(0, phone_name[idx])
        E2.insert(0, phone_number[idx])

def last():
    global phone_book
    global idx
    phone_name = list(phone_book.keys())
    phone_number = list(phone_book.values())
    idx = len(phone_name)-1
    E1.delete(0, END)
    E2.delete(0, END)
    E1.insert(0, phone_name[idx])
    E2.insert(0, phone_number[idx])

def read():
    a = open("phone_book.dat", "rb")
    while True:
        try:
            read = pickle.load(a)
            print(read)
        except EOFError:
            break
    a.close()

wnd = Tk()
phone_book = {}
idx = 0

L1 = Label(wnd, text="이름")
L2 = Label(wnd, text="전화번호")
L1.grid(row=0, columnspan=2)
L2.grid(row=1, columnspan=2)

E1 = Entry(wnd, width=27, bg="yellow")
E2 = Entry(wnd, width=27, bg="yellow")
E1.grid(row=0, column=2, columnspan=4)
E2.grid(row=1, column=2, columnspan=4)

B1 = Button(wnd , width=4, text="추가", command=plus)
B2 = Button(wnd , width=4, text="처음", command=start)
B3 = Button(wnd , width=4, text="다음", command=nxt)
B4 = Button(wnd , width=4, text="이전", command=bck)
B5 = Button(wnd , width=6, text="마지막", command=last)
B6 = Button(wnd , width=8, text="파일읽기", command=read)

B1.grid(row=2, column=0)
B2.grid(row=2, column=1)
B3.grid(row=2, column=2)
B4.grid(row=2, column=3)
B5.grid(row=2, column=4)
B6.grid(row=2, column=5)

wnd.mainloop()
