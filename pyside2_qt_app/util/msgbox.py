from PySide2.QtWidgets import QMessageBox

from .constants import YES_NO_CANCEL
from .enums import QuestionBoxResult

__all__ = [
    'about'
]


def about(parent, title, text):
    QMessageBox.about(parent, title, text)


def question(parent, title, text, buttons=YES_NO_CANCEL) -> QuestionBoxResult:
    code = QMessageBox.question(parent, title, text, buttons)
    return QuestionBoxResult(code)
