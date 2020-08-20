from tkinter import *
from math import *
root = Tk()
root.title("simple calculator")
#search box
e = Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button(number):
    #e.delete(0, END)
    current =e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0,END)

def add():
    _1st_no=e.get()
    global f_num
    global math            #math is variable name
    math="addition"        #math value is addition
    f_num=float(_1st_no)
    e.delete(0, END)
def sub():
    _1st_no = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = float(_1st_no)
    e.delete(0, END)
def mul():
    _1st_no = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(_1st_no)
    e.delete(0, END)
def div():
    _1st_no = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(_1st_no)
    e.delete(0, END)

def equ():
    _2nd_no=e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0, f_num + float(_2nd_no))
    elif math=="substraction":
        e.insert(0, f_num - float(_2nd_no))
    elif math=="multiplication":
        e.insert(0, f_num * float(_2nd_no))
    elif math=="division":
        e.insert(0, f_num / float(_2nd_no))


#creating button
button1=Button(root, text="1", padx=40,pady=20, command=lambda : button(1)) #pass the value of the button
button2=Button(root, text="2", padx=40,pady=20, command=lambda : button(2))
button3=Button(root, text="3", padx=40,pady=20, command=lambda : button(3))
button4=Button(root, text="4", padx=40,pady=20, command=lambda : button(4))
button5=Button(root, text="5", padx=40,pady=20, command=lambda : button(5))
button6=Button(root, text="6", padx=40,pady=20, command=lambda : button(6))
button7=Button(root, text="7", padx=40,pady=20, command=lambda : button(7))
button8=Button(root, text="8", padx=40,pady=20, command=lambda : button(8))
button9=Button(root, text="9", padx=40,pady=20, command=lambda : button(9))
button0=Button(root, text="0", padx=40,pady=20, command=lambda : button(0))
buttonDOT=Button(root, text=".", padx=40,pady=20, command=lambda : button("."))

buttonCLR=Button(root, text="C", padx=40,pady=20, command=clear)
buttonADD =Button(root, text="+", padx=40,pady=20, command=add)
buttonSUB =Button(root, text="-", padx=40,pady=20, command=sub)
buttonDIV =Button(root, text="/", padx=40,pady=20, command=div)
buttonMUL =Button(root, text="*", padx=40,pady=20, command=mul)
buttonEQ=Button(root, text="=", padx=40,pady=20, command=equ)


#put into d screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=1)

buttonCLR.grid(row=0, column=4)
buttonADD.grid(row=1, column=4)
buttonSUB.grid(row=2, column=4)
buttonDIV.grid(row=3, column=4)
buttonMUL.grid(row=4, column=4)
buttonEQ.grid(row=4, column=2)
buttonDOT.grid(row=4, column=0)


root.mainloop()