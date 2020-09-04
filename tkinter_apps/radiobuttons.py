from functools import partial
from tkinter import *

tk = Tk()
BG_COLOR = 'gray10'
tk.config(bg=BG_COLOR)
tk.wm_minsize(200, 200)


def on_selection(selected_data: IntVar, label_var: StringVar):
    label_var.set({0: 'option 1', 1: 'option 2'}.get(selected_data.get(), 'nothing selected :('))


def make_dark(element, modify_fg=True):
    options = {'bg': BG_COLOR}
    if modify_fg:
        options['fg'] = 'white'
    element.config(**options)
    return element


def main():
    radio_var = IntVar()
    label_var = StringVar()
    label_var.set('nothing selected :(')
    label = make_dark(Label(tk, textvariable=label_var))
    label.grid(row=2, column=0)
    make_dark(Radiobutton(tk, text='option 1', variable=radio_var, value=0, command=partial(on_selection, radio_var, label_var)),
              modify_fg=False).grid(
        row=1, column=0)
    make_dark(Radiobutton(tk, text='option 2', variable=radio_var, value=1, command=partial(on_selection, radio_var, label_var)),
              modify_fg=False).grid(
        row=1, column=1)
    tk.mainloop()


main()
