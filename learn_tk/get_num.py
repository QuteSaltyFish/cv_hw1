from tkinter import *
from tkinter import messagebox

root=Tk()
num = 0
def com():
    try:
        num = float(e1.get())#获取e1的值，转为浮点数，如果不能转捕获异常
        l1.config(text=str(num))
    except:
        messagebox.showwarning('警告','请输入数字')

e1=Entry(root)
e1.pack()
Button(root,text='click',command=com).pack()
l1=Label(root,text='kernal_size')
l1.pack()

e2 = Entry(root)
e2.pack()
Button(root,text='click',command=com).pack()
l1=Label(root,text='kernal_size')
l1.pack()
mainloop()