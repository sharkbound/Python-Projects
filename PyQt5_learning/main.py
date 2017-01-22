import PyQt5
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


def main():
    pass


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.window_size = (600, 500)

    def initUI(self):
        self.resize(600, 500)
        self.setWindowTitle('PyQt5 App')
        self.show()
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

    def add_btn(self, title='button', tooltip='', action=None, autosize=True, pos=(), size=()):
        btn = QPushButton(self)
        btn.setText(title)
        if (tooltip != ''):
            btn.setToolTip(tooltip)
        if autosize and size == ():
            btn.resize(btn.sizeHint())
        if size != ():
            btn.resize(size[0], size[1])
        if pos == ():
            btn.move(50, 50)
        else:
            btn.move(pos[0], pos[1])
        if action != None:
            btn.clicked.connect(action)

    def set_font(self, font, size):
        QToolTip.setFont(QFont(font, size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.add_btn(title='I... AM.... BUTTON!!!!', tooltip='Tooltip', pos=(gui.window_size[0] / 2 - 60, gui.window_size[1]-60), size=(), action=QCoreApplication.instance().quit)



    gui.set_font('Dina', 10)
    gui.initUI()
    sys.exit(app.exec())
