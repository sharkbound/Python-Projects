from PySide2.QtWidgets import QWidget, QPushButton, QGridLayout

from pyside2_qt_app.util import app_modal, add_grid_widget, column_stretch, row_stretch
from pyside2_qt_app.util.constants import CLICKED
from pyside2_qt_app.util.ui import connect, run


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.ok = QPushButton('hello')

        self.setLayout(self.grid)

        add_grid_widget(self, QPushButton('1'), 0, 0)
        add_grid_widget(self, QPushButton('2'), 1, 0)

        add_grid_widget(self, QPushButton('3'), 0, 1)

        add_grid_widget(self, QPushButton('4'), 0, 2)
        add_grid_widget(self, QPushButton('5'), 1, 2)

        column_stretch(self.grid, 0, 2)

        row_stretch(self.grid, 0, 1)

        app_modal(self)

        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        pass

    def setup_events(self):
        connect(self.ok, CLICKED, self.ok_clicked)

    def ok_clicked(self):
        pass


run(MainWidget())
