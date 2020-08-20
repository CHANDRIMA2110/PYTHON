from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("codeing")
root.iconbitmap("icon.ico")
#my_img=ImageTk.PhotoImage(Image.open("food1.jpg"))
my_img=ImageTk.PhotoImage(Image.open("icon_img.png"))
my_label=Label(image=my_img)
my_label.pack()
#auto exit button
button_quit=Button(root, text="click to exit program",command=root.quit)
button_quit.pack()
root.mainloop()