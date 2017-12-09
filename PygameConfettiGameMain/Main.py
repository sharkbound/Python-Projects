from src.gameHelper import Setup
from src.gameHelper import Renderer
from src.gameHelper import CorePygameFuncs as Core
from src.gameHelper import ColorFuncs
from src.MiscFuncs import Misc
from src.MiscFuncs import changeSetMode

from src.EventHelper import EventParser

from datetime import datetime

import pygame

pygame.init()

screenWidth = 600  # 800
screenHeight = 200  # 600
particleCount = 1000  # 400
particle_width = 2
particle_height = 2
screenRatio = 0.01  # 0.005
randomParticlePlacement = False

gameDisp = Setup.CreateDisplay(screenWidth, screenHeight)
Core.SetGameTitle('PyGame Snake 1.0')

Colors = ColorFuncs.GetColorList()
xlist = Misc.SetupXList(particleCount, Misc.GetCenterX(), randomParticlePlacement)
ylist = Misc.SetupYList(particleCount, Misc.GetCenterY(), randomParticlePlacement)

minChangX = 0.1
maxChangeX = Misc.GetMaxChangeX(changeSetMode.screen, 10, screenRatio)  # 5
minChangeY = 0.1
maxChangeY = Misc.GetMaxChangeY(changeSetMode.screen, 5, screenRatio)  # 5
canBeNegative = True
trig_count = 0

start = datetime.now()
out_of_bounds_msg_triggered = False
out_of_bounds_already_triggered = False

Looping = True
while Looping:
    for event in pygame.event.get():
        EventParser.ParseEvent(event)

    gameDisp.fill(Colors['white'])
    Misc.DrawBoxes(gameDisp, Colors['blue'], xlist, ylist, particle_width, particle_height, True)
    Renderer.Update()

    Index = 0

    # triggered = False

    for x in xlist:
        # triggered = False;
        xlist[Index] += Misc.RandomNum(-minChangX, maxChangeX, canBeNegative)
        ylist[Index] += Misc.RandomNum(-minChangeY, maxChangeY, canBeNegative)

        xval = xlist[Index]
        yval = ylist[Index]

        if xval > screenWidth or xval <= 0:
            xlist[Index] = Misc.GetCenterX()
            if not out_of_bounds_already_triggered:
                out_of_bounds_msg_triggered = True
                # triggered = True
        elif yval > screenHeight or yval <= 0:
            ylist[Index] = Misc.GetCenterY()
            if not out_of_bounds_already_triggered:
                out_of_bounds_msg_triggered = True
                # triggered = True

        if out_of_bounds_msg_triggered and not out_of_bounds_already_triggered:
            print('\tFirst pixel got out of bounds after {} seconds!'.format(Misc.get_datetime_total_seconds(start)))
            out_of_bounds_already_triggered = True

        Index += 1
