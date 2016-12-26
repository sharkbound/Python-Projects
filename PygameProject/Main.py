from gameHelper import Setup
from gameHelper import Renderer
from gameHelper import CorePygameFuncs as Core
from gameHelper import ColorFuncs
from MiscFuncs import Misc
from MiscFuncs import changeSetMode

from EventHelper import EventParser

import pygame

pygame.init()

screenWidth = 600#800
screenHeight = 600#600
particleCount = 400
screenRatio = 100
randomParticlePlacement = False

gameDisp = Setup.CreateDisplay(screenWidth, screenHeight)
Core.SetGameTitle('PyGame Snake 1.0')

Colors = ColorFuncs.GetColorList()
xlist = Misc.SetupXList(particleCount, screenWidth/2, randomParticlePlacement)
ylist = Misc.SetupYList(particleCount, screenHeight/2, randomParticlePlacement)

minChangX = 0.1
maxChangeX = Misc.GetMaxChangeX(changeSetMode.setByScreenDimensions, 5, screenRatio)#5
minChangeY = 0.1
maxChangeY = Misc.GetMaxChangeY(changeSetMode.setByScreenDimensions, 5, screenRatio)#5
canBeNegative = True

Looping = True
while Looping:
    for event in pygame.event.get():
        EventParser.ParseEvent(event)

    gameDisp.fill(Colors['white'])
    Misc.DrawBoxes(gameDisp, Colors['black'], xlist, ylist, 5, 5, True)
    Renderer.Update()

    Index = 0

    for x in xlist:
        xlist[Index] += Misc.RandomNum(-minChangX, maxChangeX, canBeNegative)
        ylist[Index] += Misc.RandomNum(-minChangeY, maxChangeY, canBeNegative)

        xval = xlist[Index]
        yval = ylist[Index]

        if xval > screenWidth:
            xlist[Index] = screenWidth / 2
        elif yval > screenHeight:
            ylist[Index] = screenHeight / 2

        Index += 1
