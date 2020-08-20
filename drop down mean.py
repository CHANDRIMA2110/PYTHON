from tkinter import *
root=Tk()
clicked=StringVar()

options=["monday","tuesday","wednesday","thursday","friday","saturday"]
#set a default value
clicked.set("choose days")

drop=OptionMenu(root,clicked,*options).pack()
#drop=OptionMenu(root,clicked,"monday","tuesday","wednesday","thursday","friday","saturday").pack()
def show():
    my_label=Label(root, text=clicked.get())
    my_label.pack()
my_btn=Button(root, text="show selection",command=show).pack()
root.mainloop()