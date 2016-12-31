from tkinter import *

gui = Tk()


def addmenuitem(item):
    # todo: add this
    pass


def packtxt(text):
    label = Label(gui, text=text)
    label.pack()


def startgui():
    gui.mainloop()


def set_title(title):
    gui.title(title)
