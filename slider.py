from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.geometry("400x400")

vertical= Scale(root,from_=0,to=400)
vertical.pack()
horizontal=Scale(root,from_=0,to=500,orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x"+ str(vertical.get()))
btn=Button(root,text="click", command=slide).pack()
root.mainloop()