from tkinter import *
root=Tk()
root.title("freame work")

frame= LabelFrame(root,text="This is frame broder...", padx=20, pady=15)#space of the inside the frame
frame.pack(padx=100,pady=100)#space of the outside of the frame
b=Button(frame,text="Dont click",command=frame.quit)
b1=Button(frame,text="click")
b.grid(row=0,column=0)
b1.grid(row=1,column=2)


root.mainloop()