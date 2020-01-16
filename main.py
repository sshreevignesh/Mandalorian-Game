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
import random
from getch import _getChUnix as getChar

# variables.scene.showboard()
mando=objects.Mandalorian()
mando.render(10,10)
coin=[objects.coins() for i in range(100)]
for i in range(100):
    coin[i].render(random.randint(10,2500),random.randint(5,35))
vertical_laser1=objects.vertical_laser()
vertical_laser1.render(150,30)
while(1):
    keypressed=input.getpress()
    if keypressed=='q':
        quit()
    if keypressed!='w':
        mando.move(keypressed,2)
        mando.gravity()
    mando.move(keypressed,2)

    # mando.gravity()

    #Moving the screen move without Moving the Mando
    mando.move('d',2)
    variables.screenpos=variables.screenpos+2

    variables.scene.showboard(variables.screenpos)
    variables.last_ground_touch=variables.last_ground_touch+1
