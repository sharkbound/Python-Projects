from tkinter import *
import tkinter

gui = Tk()


def addmenuitem(item):
    # todo: add this
    pass


def addbtn(text, *func):
    button = tkinter.Button(gui, text="textbtn")
    button.pack()


def addtxt(text):
    label = Label(gui, text=text)
    label.pack()
def addchkbtn(text):
    chkbtn = Checkbutton(gui, text=text)
    chkbtn.pack()

def startgui():
    gui.mainloop()


def set_title(title):
    gui.title(title)


def set_width_height(width, height):
    frame = Frame(gui, width=width, height=height)
    frame.pack()