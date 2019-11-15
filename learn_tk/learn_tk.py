import tkinter as tk 
from tkinter.filedialog import askdirectory

def selectPath():
    path_ = askdirectory()
    path.set(path_)

top = tk.Tk()
top.title("CV Homework1")
top.geometry("800x600+100+100")
top.resizable(False, True)

my_label = tk.Label(top,text="loading",background="yellow",width=15,height=2)   
my_label.pack()
img_gif = tk.PhotoImage(file = 'result/mean.gif')
label_img = tk.Label(top, image = img_gif)
label_img.pack()

tk.Label(top,text = "目标路径:").grid(row = 0, column = 0)
tk.Entry(top, textvariable = path).grid(row = 0, column = 1)
tk.Button(top, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
top.mainloop()

# from tkinter import *
# from tkinter.filedialog import askdirectory

# def selectPath():
#     path_ = askdirectory()
#     path.set(path_)

# root = Tk()
# path = StringVar()

# Label(root,text = "目标路径:").grid(row = 0, column = 0)
# Entry(root, textvariable = path).grid(row = 0, column = 1)
# Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)

# root.mainloop()