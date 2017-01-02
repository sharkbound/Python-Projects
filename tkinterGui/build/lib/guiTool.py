from tkinter import *
import tkinter

if __name__ == '__main__':
    print("this script must be imported!")
else:
    gui = Tk()


def addmenuitem(item):
    # todo: add this
    pass


def addbtn(text, **kwargs):
    def callback_print():
        print("Default click event!")

    button = tkinter.Button(gui, text=text, command=kwargs.get("cmd", callback_print))
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
