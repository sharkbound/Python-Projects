from utils.tkinterutil import *

app = tk.Tk()

n = ttk.Notebook(app)

f = ttk.Frame(n)
grid(ttk.Button(f, text='tab1'), 0, 0)
n.add(f, text='tab1')

f = ttk.Frame(n)
grid(ttk.Button(f, text='tab2'), 0, 0)
n.add(f, text='tab2')

grid(n, 0, 0, xspan=100, yspan=100)

app.mainloop()
