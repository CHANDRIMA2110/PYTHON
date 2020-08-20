from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("radion button")

r=IntVar()
#to set default value
r.set("2")

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()

Radiobutton(root,text="option 1",variable=r,value=1,command=lambda :clicked(r.get())).pack()
Radiobutton(root,text="option 2",variable=r,value=2,command=lambda :clicked(r.get())).pack()

#my_label=Label(root,text=r.get())
#my_label.pack()

my_button=Button(root,text="click me",command=lambda :clicked(r.get()))
my_button.pack()
root.mainloop()