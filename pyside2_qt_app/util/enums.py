from enum import IntFlag

from PySide2.QtWidgets import QMessageBox

__all__ = [
    'QuestionBoxResult'
]


class QuestionBoxResult(IntFlag):
    YES = QMessageBox.Yes
    NO = QMessageBox.No
    CANCEL = QMessageBox.Cancel
