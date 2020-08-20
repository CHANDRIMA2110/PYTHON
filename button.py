from tkinter import*
root=Tk()

def myclick():
    mylabel=Label(root,text="done, u clicked",fg="red")
    mylabel.pack()

#creating button
mybutton=Button(root, text="click me",command=myclick,fg="blue",bg="pink")
# mybutton=Button(root, text="click me",state=DISABLED,padx=10, pady=10)


mybutton.pack()
root.mainloop()