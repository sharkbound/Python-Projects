from gameHelper import Setup, Renderer, ColorFuncs, CorePygameFuncs as Core
from MiscFuncs import Misc, changeSetMode
from EventHelper import EventParser
from datetime import datetime
from LoggingFuncs import log, delete_log_folder, create_log_folder

import pygame

pygame.init()
delete_log_folder()
create_log_folder()

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
            log('\n\tPixel of index {} is out of bounds! \n\t\tY: {} \n\t\tX: {} [Out Of Bounds]\n'.format(Index, ylist[Index],
                                                                                                 xlist[Index]))

            xlist[Index] = Misc.GetCenterX()

        elif yval > screenHeight or yval <= 0:
            log('\n\tPixel of index {} is out of bounds! \n\t\tY: {} [Out of bounds] \n\t\tX: {}\n'.format(Index, ylist[Index],
                                                                                                 xlist[Index]))

            ylist[Index] = Misc.GetCenterY()

        Index += 1
