from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import func
from PIL import Image, ImageTk
root=Tk()
kernal_size = 0
sigma = 0
def get_kernal_size():
    try:
        global kernal_size
        kernal_size = int(e1.get())#获取e1的值，转为浮点数，如果不能转捕获异常
        l1.config(text='kernal_size='+str(kernal_size))
    except:
        messagebox.showwarning('警告','请输入数字')

# def get_sigma():
#     try:
#         global sigma
#         sigma = int(e2.get())#获取e1的值，转为浮点数，如果不能转捕获异常
#         l2.config(text='sigma='+str(sigma))
#     except:
#         messagebox.showwarning('警告','请输入数字')


def printcoords():
    l1.config(text='PLS WAIT')
    # l2.config(text='PLS WAIT')
    global kernal_size
    global sigma
    File = filedialog.askopenfilename(title='Choose an image.')
    pic = func.hw1(File)
    pic.Mean_filter(kernal_size)

    filename = ImageTk.PhotoImage(Image.open('result/Mean.gif'))
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)
    l1.config(text='Pls input kernal_size')

e1=Entry(root)
e1.pack()
Button(root,text='click',command=get_kernal_size).pack()
l1=Label(root,text='Pls input kernal_size')
l1.pack()

# e2 = Entry(root)
# e2.pack()
# Button(root,text='click',command=get_sigma).pack()
# l2=Label(root,text='Pls input sigma')
# l2.pack()


#setting up a tkinter canvas with scrollbars
frame = Frame(root, bd=4, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
xscroll = Scrollbar(frame, orient=HORIZONTAL)
xscroll.grid(row=1, column=0, sticky=E+W)
yscroll = Scrollbar(frame)
yscroll.grid(row=0, column=1, sticky=N+S)
canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
xscroll.config(command=canvas.xview)
yscroll.config(command=canvas.yview)
frame.pack(fill=BOTH,expand=1)


#function to be called when mouse is clicked
Button(root,text='choose',command=printcoords).pack()

mainloop()