from PySide2 import QtCore, QtWidgets, QtGui


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(QtWidgets.QLabel(''))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.show()

    app.exec_()
