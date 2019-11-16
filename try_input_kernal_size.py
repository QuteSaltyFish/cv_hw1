from tkinter import* 

kernal_size = 3
sigma = 1

def change_kernal_size(event):    
        #清理entry2  
        kernal_size = entry1.get()
        entry2.delete(0, END)    #将entry1接收到的文本插入entry2    
        entry2.insert(10, kernal_size)    #清空entry2控件    
        entry1.delete(0, END)    #初始化
   
        
def change_sigma(event):
    sigma = entry3.get()
    entry4.delete(0, END)    #将entry1接收到的文本插入entry2    

    entry4.insert(10, kernal_size)    #清空entry2控件    
    entry3.delete(0, END)    #初始化

#function to be called when mouse is clicked
def printcoords():
    File = filedialog.askopenfilename(parent=myWindow, initialdir="C:/",title='Choose an image.')
    pic = func.hw1(File)
    pic.Gaussian()

    filename = ImageTk.PhotoImage(Image.open('result/Gaussian.gif'))
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)


myWindow = Tk()#设置标题
myWindow.title('Python GUI Learning') #标签+单行文本框


Label(myWindow, text="input_kernal").grid(row=0)
Label(myWindow, text="kernal").grid(row=1) #Entry绑定回车事件

Label(myWindow, text="inputsigma").grid(row=2)
Label(myWindow, text="sigma").grid(row=3) #Entry绑定回车事件

frame = Frame(myWindow, bd=2, relief=SUNKEN).grid(row=4, column=0)


# frame = Frame(myWindow, bd=2, relief=SUNKEN)
# frame.grid_rowconfigure(0, weight=1)
# frame.grid_columnconfigure(0, weight=1)
xscroll = Scrollbar(frame, orient=HORIZONTAL)
xscroll.grid(row=5, column=0, sticky=E+W)
yscroll = Scrollbar(frame)
yscroll.grid(row=4, column=1, sticky=N+S)
canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
canvas.grid(row=4, column=0, sticky=N+S+E+W)
xscroll.config(command=canvas.xview)
yscroll.config(command=canvas.yview)
# frame.pack(fill=BOTH,expand=1)




entry1=Entry(myWindow)
entry1.bind("<Return>", change_kernal_size)
entry2=Entry(myWindow)

entry3=Entry(myWindow)
entry3.bind("<Return>", change_sigma)
entry4=Entry(myWindow)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1) 
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1) 
#进入消息循环



Button(myWindow,text='choose',command=printcoords)
frame.pack(fill=BOTH,expand=1)

myWindow.mainloop()
