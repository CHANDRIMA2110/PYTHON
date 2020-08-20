from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("message box")

def qusyes():
    response=messagebox.askyesno("(write heading)", "qus msg\n (inside the body)")
    Label(root, text=response).pack()
    if response==1:
        Label(root, text="you clicked yes").pack()
    else:
      Label(root, text="you clicked no").pack()

#askokcancel, askyesno -- return 1, 0
# askques-- return---yes, no
#showerror--return--ok
#show warning--return --ok
#showinfo--return--ok


button6=Button(root,text="Popup a qus with yes/no",command=qusyes)
button6.pack()

root.mainloop()