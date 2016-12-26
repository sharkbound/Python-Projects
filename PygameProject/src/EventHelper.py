import pygame
from gameHelper import CorePygameFuncs as Core

class EventParser:
    @staticmethod
    def ParseEvent(event):
        if event.type == pygame.QUIT:
            EventTriggerMethods.Event_Quit()

        if event.type == pygame.KEYDOWN:
            print('pygame.KEYDOWN')

        if event.type == pygame.KEYUP:
            print('pygame.KEYUP')
            EventTriggerMethods.Event_Quit()

class EventTriggerMethods:
    @staticmethod
    def Pre_Exit_Operations():
        print('Quitting Game...')

    @staticmethod
    def Event_Quit():
        EventTriggerMethods.Pre_Exit_Operations()
        Core.Quit()