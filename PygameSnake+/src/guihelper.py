import pygame, sys


class Gui:
    def __init__(self, screen):
        self.screen = screen

    def quit(self):
        pygame.quit()
        sys.exit()

    def set_title(self, title):
        pygame.display.set_caption(title)

    def update(self):
        pygame.display.update()

    def background_fill(self, color):
        self.screen.fill(color)
