import tkinter
from PIL import Image,ImageTk

window = tkinter.Tk()
window.title("GUI")

icon = Image.open("C:\\Users\\hp\\PycharmProjects\\opencv\\MK.jpg")
label = tkinter.Label(window,image = icon)
label.pack()

window.mainloop()