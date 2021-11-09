from tkinter import ttk
import tkinter as tk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__(screenName='lyric app')


class BaseFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.bind_keys()
        self.setup_ui()

    def bind_keys(self):
        pass

    def setup_ui(self):
        pass


class MainFrame(BaseFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent.minsize(300, 300)

    def setup_ui(self):
        self.btn = ttk.Button(self.parent, text='click me!', command=lambda: self.show_popup())
        self.btn.grid(row=0, column=0, rowspan=2, columnspan=2)

    def show_popup(self):
        OtherFrame(self).tkraise()


class OtherFrame(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        ttk.Button(self, text='yes', command=lambda: self.destroy()).pack()
        ttk.Button(self, text='no').pack()
        self.minsize(300, 300)
        # self.transient()


if __name__ == '__main__':
    app = MainApp()
    main_frame = MainFrame(app)
    app.mainloop()
