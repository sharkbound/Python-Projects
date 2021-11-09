from typing import Union, Callable

from PySide2.QtCore import SIGNAL, Qt
from PySide2.QtWidgets import QWidget, QDialog, QMainWindow

from pyside2_qt_app.util import APP

__all__ = [
    'connect',
    'run',
    'show',
    'text',
    'move',
    'app_modal',
    'window_modal',
    'no_modal',
    'add_grid_widget',
    'size',
    'resize',
    'column_stretch',
    'row_stretch'
]


def connect(obj, signal, handler):
    APP.connect(obj, SIGNAL(signal), handler)


def show(obj):
    obj.show()


def run(obj):
    show(obj)
    APP.exec_()


def text(widget, new_text: Union[Callable, str] = None):
    if isinstance(new_text, str):
        widget.setText(new_text)
    elif callable(new_text):
        widget.setText(new_text(widget.text()))
    else:
        return widget.text()


def move(obj, x, y):
    obj.move(x, y)


def app_modal(obj):
    obj.setWindowModality(Qt.ApplicationModal)


def window_modal(obj):
    obj.setWindowModality(Qt.WindowModal)


def no_modal(obj):
    obj.setWindowModality(Qt.NonModal)


def add_grid_widget(grid, obj, x, y):
    _get_layout(grid).addWidget(obj, y, x)


def size(obj, w, h):
    obj.setSize(w, h)


def resize(obj, w, h):
    obj.resize(w, h)


def column_stretch(grid, index, weight):
    _get_layout(grid).setColumnStretch(index, weight)


def row_stretch(grid, index, weight):
    _get_layout(grid).setRowStretch(index, weight)


def _get_layout(obj):
    if isinstance(obj, (QWidget, QDialog, QMainWindow)):
        return obj.layout()
    return obj
