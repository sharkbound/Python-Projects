from PySide2.QtWidgets import QApplication, QMessageBox

__all__ = [
    'APP',
    'CLICKED',
    'YES',
    'NO',
    'YES_NO',
    'CANCEL',
    'YES_NO_CANCEL',
]

APP = QApplication([])
CLICKED = 'clicked()'

YES = QMessageBox.Yes
NO = QMessageBox.No
CANCEL = QMessageBox.Cancel
YES_NO = YES | NO
YES_NO_CANCEL = YES_NO | CANCEL
