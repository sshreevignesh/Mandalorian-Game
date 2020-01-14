#TODO implement movement of boards

import sys
import termios
import tty
import time
import signal
import design
import objects
import boards
import variables
import input
import os
from getch import _getChUnix as getChar

# variables.scene.showboard()
mando=objects.Mandalorian()
mando.render(10,10)
last_moved= int(round(time.time() * 1000))
while(1):
    keypressed=input.getpress()
    if keypressed=='q':
        quit()
    if keypressed!='w':
        variables.count=variables.count+1
    mando.move(keypressed)

    mando.gravity()

    #Moving the screen move without Moving the Mando
    mando.move('d')
    variables.screenpos=variables.screenpos+1

    variables.scene.showboard(variables.screenpos)
    variables.last_ground_touch=variables.last_ground_touch+1
