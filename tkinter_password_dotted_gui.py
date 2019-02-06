from tkinter import *


def getpass():
    root = Tk()
    Label(root, text='enter your password:').pack()
    string = StringVar(root)
    pass_input = Entry(root, show='*', textvar=string)
    pass_input.bind('<Return>', lambda _: root.quit())
    pass_input.pack()
    root.mainloop()
    return string.get()


print(getpass())
