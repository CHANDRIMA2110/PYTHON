from tkinter import*
root=Tk()
###################creating level
mylabel=Label(root, text="hello world")
mylabel2=Label(root, text="my name is chandrima ghosh")
#####another way in one line
# mylabel=Label(root, text="hello world").grid(row=0,column=0)
# mylabel2=Label(root, text="my name is chandrima ghosh").grid(row=1,column=5)
#############puttinging into d screen
mylabel.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)

root.mainloop()