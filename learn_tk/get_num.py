from tkinter import *
from tkinter import messagebox

root=Tk()
kernal_size = 0
sigma = 0
def get_kernal_size():
    try:
        kernal_size = float(e1.get())#获取e1的值，转为浮点数，如果不能转捕获异常
        l1.config(text=str(kernal_size))
    except:
        messagebox.showwarning('警告','请输入数字')

def get_sigma():
    try:
        sigma = float(e2.get())#获取e1的值，转为浮点数，如果不能转捕获异常
        l2.config(text=str(sigma))
    except:
        messagebox.showwarning('警告','请输入数字')

e1=Entry(root)
e1.pack()
Button(root,text='click',command=get_kernal_size).pack()
l1=Label(root,text='kernal_size')
l1.pack()

e2 = Entry(root)
e2.pack()
Button(root,text='click',command=get_sigma).pack()
l2=Label(root,text='sigma')
l2.pack()
mainloop()