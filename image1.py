from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("image slide show")

#my_img=ImageTk.PhotoImage(Image.open("food1.jpg"))
my_img1=ImageTk.PhotoImage(Image.open("smallf1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("smallf2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("smallf3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("smallf4.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("smallf5.jpg"))
my_img6=ImageTk.PhotoImage(Image.open("smallf6.jpg"))
my_img7=ImageTk.PhotoImage(Image.open("smallf7.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7]
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward=Button(root,text="Next", command=lambda: forward(image_number+1))
    button_back = Button(root, text="Prev", command=lambda: back(image_number - 1))
    if image_number==7:
        button_forward=Button(root, text="Next",state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=1)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text="Next", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="Prev", command=lambda: back(image_number-1))
    if image_number==1:
        button_back=Button(root, text="Prev",state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=1)


button_back=Button(root,text="Prev", command=back,state=DISABLED)
button_exit=Button(root,text="Exit Slide",command=root.quit)
button_forward=Button(root,text="Next",command=lambda :forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=2)
button_forward.grid(row=1,column=1)

root.mainloop()