from tkinter import *
root = Tk()

#search box
e = Entry(root)
#e = Entry(root,width=30,bg="yellow",borderwidth=5)
e.pack()
e.insert(0, "type here..")

def myclick():
    mylabel=Label(root, text='You are searching about - ' + e.get())
    mylabel.pack()

#creating button
mybutton = Button(root, text="search",command=myclick,fg="blue",bg="pink")
mybutton.pack()
root.mainloop()