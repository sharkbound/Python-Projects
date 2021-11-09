import tkinter as tk
from tkinter import ttk


def grid(item, x, y, xspan=1, yspan=1, ipadx=None, ipady=None, padx=None, pady=None):
    kw = {'row': y, 'column': x, 'rowspan': xspan, 'columnspan': yspan}
    if ipadx is not None:
        kw['ipadx'] = ipadx
    if ipady is not None:
        kw['ipady'] = ipady
    if padx is not None:
        kw['padx'] = padx
    if pady is not None:
        kw['pady'] = pady
    item.grid(**kw)
