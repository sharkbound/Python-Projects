import tkinter as tk

root = tk.Tk()
root.bind('<Escape>', lambda *_: root.quit())


class Buttons(tk.LabelFrame):
    def __init__(self):
        super().__init__(root, text=self.__class__.__name__, labelanchor='n')

        self.text_var = tk.StringVar()
        self.text = tk.Entry(self, textvariable=self.text_var)
        self.button = tk.Button(self, text='???')
        self.bind_events()
        self.add()

    def add(self):
        self.button.pack(side='bottom')
        self.text.pack(side='top')

    def pack(self):
        super().pack()

    def bind_events(self):
        self.text.bind('<Return>', self.text_enter_pressed)

    def text_enter_pressed(self, _):
        self.button.config(text=self.text_var.get())


Buttons().pack()

root.mainloop()
