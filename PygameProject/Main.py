from gameHelper import Setup
from gameHelper import Renderer
from gameHelper import CorePygameFuncs as Core
from gameHelper import ColorFuncs
from MiscFuncs import Misc
from MiscFuncs import changeSetMode

from EventHelper import EventParser

import pygame

pygame.init()

screenWidth = 600  # 800
screenHeight = 200  # 600
particleCount = 30  # 400
screenRatio = 0.005  # 0.005
randomParticlePlacement = True

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

Looping = True
while Looping:
    for event in pygame.event.get():
        EventParser.ParseEvent(event)

    gameDisp.fill(Colors['white'])
    Misc.DrawBoxes(gameDisp, Colors['black'], xlist, ylist, 10, 10, True)
    Renderer.Update()

    Index = 0

    #triggered = False

    for x in xlist:
        #triggered = False;
        xlist[Index] += Misc.RandomNum(-minChangX, maxChangeX, canBeNegative)
        ylist[Index] += Misc.RandomNum(-minChangeY, maxChangeY, canBeNegative)

        xval = xlist[Index]
        yval = ylist[Index]

        if xval > screenWidth or xval <= 0:
            xlist[Index] = Misc.GetCenterX()
            #triggered = True
        elif yval > screenHeight or yval <= 0:
            ylist[Index] = Misc.GetCenterY()
            #triggered = True
        '''
        if triggered:
            trig_count += 1
            print('triggered! {}'.format(trig_count))
            x = Misc.GetCenterX()  # Misc.SetupXList(1, Misc.GetCenterX(), randomParticlePlacement)
            y = Misc.GetCenterY()  # Misc.SetupYList(1, Misc.GetCenterX(), randomParticlePlacement)
            # Misc.DrawBoxes(gameDisp, Colors['black'], x, y, 500, 500, False)
            Renderer.DrawRect(gameDisp, Colors['red'], x, y, 300, 300)
            Renderer.Update()
        '''
        Index += 1
