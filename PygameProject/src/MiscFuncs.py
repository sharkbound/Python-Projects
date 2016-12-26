import random
from gameHelper import Renderer
import gameHelper as game
import math
from enum import Enum


class changeSetMode(Enum):
    manual = 1
    screen = 2


class Misc:
    @staticmethod
    def RandomNum(min, max, CanBeNegative=False):
        if not CanBeNegative:
            min = math.fabs(min)
            max = math.fabs(max)

        value = random.uniform(min, max)
        randNum = random.randint(0, 1)

        if (randNum == 1 and CanBeNegative):
            value = -value

        return value

    @staticmethod
    def DrawBoxes(display, color, xlist, ylist, width, height, randomcolor=False):
        index = 0
        length = len(xlist)
        colorList = None
        colorDict = None

        if randomcolor:
            colorList = list(game.ColorFuncs.GetColorList())
            colorDict = game.ColorFuncs.GetColorList()

        while index < length:
            if randomcolor:
                color = Misc.GetRandomColor(colorList, colorDict)
            Renderer.DrawRect(display, color, xlist[index], ylist[index], width, height)
            index += 1

    @staticmethod
    def SetupXList(NumberOfEntries, value, randomplacement=False):
        loop = 0
        list = []

        if randomplacement:
            import Main

            while loop < NumberOfEntries:
                list.append(random.randint(0, Main.screenWidth))
                loop += 1
        else:
            while loop < NumberOfEntries:
                list.append(value)
                loop += 1

        return list

    @staticmethod
    def SetupYList(NumberOfEntries, value, randomplacement=False):
        loop = 0
        list = []

        if randomplacement:
            import Main

            while loop < NumberOfEntries:
                list.append(random.randint(0, Main.screenHeight))
                loop += 1
        else:
            while loop < NumberOfEntries:
                list.append(value)
                loop += 1

        return list

    @staticmethod
    def GetRandomColor(colorlist, colordict):
        # colorList = list(game.ColorFuncs.GetColorList())
        # colorDict = game.ColorFuncs.GetColorList()
        randomIndex = random.randint(0, len(colorlist) - 1)
        color = colordict[colorlist[randomIndex]]
        return color

    @staticmethod
    def GetMaxChangeX(mode, value, percent=0.005):

        if mode == changeSetMode.manual:
            return value
        elif mode == changeSetMode.screen:
            import Main
            print('XChange after percent is applied: {}'.format(int(Main.screenWidth * percent)))
            return int(Main.screenWidth * percent)

    @staticmethod
    def GetMaxChangeY(mode, value, percent=0.005):

        if mode == changeSetMode.manual:
            return value
        elif mode == changeSetMode.screen:
            import Main
            print('YChange after percent is applied: {}'.format(int(Main.screenHeight * percent)))
            return int(Main.screenHeight * percent)

    @staticmethod
    def GetCenterX():
        import Main
        return int(Main.screenWidth / 2)

    @staticmethod
    def GetCenterY():
        import Main
        return int(Main.screenHeight / 2)
