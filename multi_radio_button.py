from tkinter import *
root=Tk()
root.title("radion button")

MODES=[
    ("biriyani","biriyani"),
    ("rice","rice"),
    ("veg food","veg food"),
    ("non-veg","non-veg"),
]

pizz=StringVar()
pizz.set("rice")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizz,value=mode).pack(anchor=W)

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()

#my_label=Label(root,text=pizz.get())
#my_label.pack()

my_button=Button(root,text="click me",command=lambda :clicked(pizz.get()))
my_button.pack()
root.mainloop()