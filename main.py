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
mando.render(10,35)
while(1):
    os.system('clear')
    keypressed=input.getpress()
    # print(keypressed)
    if keypressed=='q':
        quit()
    mando.move(keypressed)
    variables.scene.showboard(0)
    time.sleep(0.05)
