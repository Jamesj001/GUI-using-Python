import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("GUI")
window.geometry('400x400')

label = tkinter.Label(window, text="Hello world").pack()
frame1 = tkinter.Frame(window).pack()
frame2 = tkinter.Frame(window).pack(side="bottom")
def func1():
    messagebox.showinfo('Message title','Message content')

def func2():
    tkinter.Label(window,text="hi").pack()

def leftclick(event):
    tkinter.Label(window,text="left click").pack()
def rightclick(event):
    tkinter.Label(window, text="right click").pack()
def middleclick(event):
    tkinter.Label(window, text="middle click").pack()

bt1 = tkinter.Button(frame1, text="Enter1", bg="orange", fg="red",command=func1).pack()
bt2 = tkinter.Button(frame2, text="Enter2", bg="green", fg="blue",command=func2).pack()

window.bind("<Button-1>",leftclick)
window.bind("<Button-2>",middleclick)
window.bind("<Button-3>",rightclick)

window.mainloop()