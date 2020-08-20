from tkinter import *

root=Tk()
var=IntVar()
var1=StringVar()

c=Checkbutton(root, text="check this box 1 ", variable=var).pack()
c1=Checkbutton(root, text="check this box 2 ", variable=var1,onvalue="On",offvalue="Off")
c1.deselect()
c1.pack()

def show():
    my_lbl = Label(root, text=var.get())
    my_lbl.pack()
my_btn=Button(root,text="selection1",command=show).pack()

def show2():
    my_lbl1 = Label(root, text=var1.get())
    my_lbl1.pack()
my_btn1=Button(root,text="selection2",command=show2).pack()

root.mainloop()