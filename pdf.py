from tkinter import *
import tkinter
from tkinter.filedialog import askopenfile
from docx2pdf import convert
from pdf2docx import Converter
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
#creating the window
win=Tk()
win.geometry("700x570")
win.title("pdf-converter")
win.resizable(False, False)
photo=ImageTk.PhotoImage(file=r"C:\Users\herimorn\Pictures\Saved Pictures\evironment.jpg")
wlabel=Label(win,image=photo)
wlabel.place(x=0,y=0,relwidth=1,relheight=1)
title=Label(win,text="welcome to converter",font=("cursive",50),fg="chocolate")
title.grid(row=1,column=2)
            
#the function for the opening of files
def openword():
    file=askopenfile(filetypes=[("word file","*.docx")])
    convert(file.name,r"C:\Users\herimorn\Desktop\konz.pdf")
    showinfo("done","fileconverted into pdf")
def openpdf():
    file=askopenfile(filetypes=[("word file","*.pdf")])
    cv=Converter(file,start=0,end=None)
    cv.convert(file,r"C:\Users\herimorn\Desktop\john1.docx")
    showinfo("done","fileconverted to word")
b1=Button(win,text="convert to pdf ",width=30,command=openword,bg="red")
b1.place(x=500,y=300)
b2=Button(win,text="convert to word ",width=30,command=openpdf,bg="green")
b2.place(x=100,y=300)

