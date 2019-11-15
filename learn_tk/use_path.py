import os, sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("/home/wangmingke/Desktop/HomeWork/cv_hw1/func.py")))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
FUNC_DIR = "/home/wangmingke/Desktop/HomeWork/cv_hw1"
DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(FUNC_DIR)
import cv2
import func
from tkinter import *
import tkinter.filedialog




root = Tk()


def xz():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        string_filename = ""
        for i in range(0, len(filenames)):
            string_filename += str(filenames[i])
        lb.config(text="please wait for a moment")
        hw = func.hw1(string_filename)
        hw.Gaussian()
        img = cv2.imread('result/Gaussian.png')
        cv2.imshow('Gaussian Filter', img)
        lb.config(text="The File hase been shown"+string_filename)
    else:
        lb.config(text="您没有选择任何文件")

 
lb = Label(root, text='')
lb.pack()
btn = Button(root, text="Please selecet the pic you want to process", command=xz)

btn.pack()
root.mainloop()
