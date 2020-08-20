from tkinter import *
root=Tk()
root.title("codeing")
root.iconbitmap("icon_img.png")

#auto exit button
button_quit=Button(root, text="click to exit program",command=root.quit,padx=30,pady=10)
button_quit.pack()
root.mainloop()