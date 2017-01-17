import PyQt5
import sys

from PyQt5.QtWidgets import QApplication, QWidget


def main():
    pass

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        self.setWindowTitle('lel')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()

    sys.exit(app.exec())