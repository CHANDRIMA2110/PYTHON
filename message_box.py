from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("message box")

def info():
    messagebox.showinfo("(write heading)","hi, information msg\n (inside the body)")
def warn():
    messagebox.showwarning("(write heading)", "warning msg\n (inside the body)")
def error():
    messagebox.showerror("(write heading)", "error msg\n (inside the body)")
def qus():
    messagebox.askquestion("(write heading)", "question msg\n (inside the body)")
def quscancel():
    messagebox.askokcancel("(write heading)", "qus msg\n (inside the body)")
def qusyes():
    messagebox.askyesno("(write heading)", "qus msg\n (inside the body)")


button1=Button(root,text="Popup a info",command=info)
button1.pack()
button2=Button(root,text="Popup a warning",command=warn)
button2.pack()
button3=Button(root,text="Popup a error",command=error)
button3.pack()
button4=Button(root,text="Popup a qus with yes/no",command=qus)
button4.pack()
button5=Button(root,text="Popup a qus with ok/cancel",command=quscancel)
button5.pack()
button6=Button(root,text="Popup a qus with yes/no",command=qusyes)
button6.pack()


root.mainloop()