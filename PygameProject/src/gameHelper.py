import pygame


class Renderer:
    @staticmethod
    def Update():
        # Updates a specific area of surface
        pygame.display.update()

    @staticmethod
    def AdvanceToNextFrame():
        # Updates entire surface
        pygame.display.flip()

    @staticmethod
    def DrawRect(display, color, x, y, width, height):
        pygame.draw.rect(display, color, [x, y, width, height])


class Setup:
    @staticmethod
    def CreateDisplay(width, height):
        return pygame.display.set_mode((width, height))


class CorePygameFuncs:
    @staticmethod
    def Quit():
        pygame.quit()
        quit()

    @staticmethod
    def SetGameTitle(name):
        pygame.display.set_caption(name)


class ColorFuncs:
    @staticmethod
    def GetColorList():
        return {
            'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255),
            'yellow': (240, 255, 0), 'black': (0, 0, 0)
        }

    def test(*t):
        return 1

    def __repr__(self):
        return str(ColorFuncs.GetColorList())
