from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("new window")

def open():
    global my_img
    top=Toplevel()
    top.title("2nd window")
    # lbl=Label(root, text="hello").pack()
    my_img = ImageTk.PhotoImage(Image.open("smallf1.jpg"))
    my_label = Label(top, image=my_img)
    my_label.pack()
    button2 = Button(top, text="close window", command=top.destroy)
    button2.pack()

# for main window button
button=Button(root,text="open 2nd window", command=open).pack()

mainloop()