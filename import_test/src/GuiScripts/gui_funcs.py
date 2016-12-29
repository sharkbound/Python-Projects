from tkinter import *
from enum_classes import GuiTextMode as text
import tkinter

gui = Tk()


def setupgui():
    pass


def addmenuitem(item):
    pass


def addtext_pack(text, mode=text.pack):
    label = Label(gui, text=text)
    label.pack()


def startgui():
    gui.mainloop()


def set_title(title_text):
    gui.title(title_text)
