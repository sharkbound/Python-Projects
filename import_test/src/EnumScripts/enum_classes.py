from enum import Enum


class LineMode(Enum):
    nothing = 1
    newlinetab = 2
    newline = 3
    tab1 = 4
    tab2 = 5
    newlinetab2 = 6
    space2 = 7
    space1 = 8
    space3 = 9

class GuiTextMode(Enum):
    pack = 1
