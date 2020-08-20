from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.title("dialog box")
mylabel1=Label(root, text="please select a file").pack()

root.filename=filedialog.askopenfilename(initialdir="PycharmProjects",
                                         title="select a file",
                                         filetypes=(("jpg files","*.jpg"),("png files","*.png"),
                                                    ("all files","*.*")))#(description), (extention)

##### open img location
my_label=Label(root,text=root.filename).pack()
#### open img itself
my_img=ImageTk.PhotoImage(Image.open(root.filename))
my_img_lbl=Label(root,image=my_img).pack()

cl_button=Button(root,text="close window",command=quit).pack()

#def open():
#    global my_img
#    root.filename = filedialog.askopenfilename(initialdir="PycharmProjects",
#                                               title="select a file",
#                                               filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"),
#                                                          ("all files", "*.*")))  # (description), (extention)
#    # open img location
#    my_label = Label(root, text=root.filename).pack()
#    # open img itself
#    my_img = ImageTk.PhotoImage(Image.open(root.filename))
#    my_img_lbl = Label(root, image=my_img).pack()
#    cl_button = Button(root, text="close window", command=quit).pack()
#op_button = Button(root, text="open file", command=open).pack()


root.mainloop()