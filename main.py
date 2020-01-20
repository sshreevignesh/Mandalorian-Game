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
boss=objects.dragon()
boss.render(variables.board_length-200,4)
coin=[objects.coins() for i in range(100)]
for i in range(100):
    coin[i].render(random.randint(10,500),random.randint(5,35))

vertical_lasers=[objects.vertical_laser() for i in range(5)]
for i in range(5):
    vertical_lasers[i].render(random.randint(50,500),random.randint(15,25))

horizontal_lasers=[objects.horizontal_laser() for i in range(5)]
for i in range(5):
    horizontal_lasers[i].render(random.randint(50,500),random.randint(5,35))

diagonal_lasers1=[objects.diagonal_laser1() for i in range(5)]
for i in range(5):
    diagonal_lasers1[i].render(random.randint(50,500),random.randint(15,25))

diagonal_lasers2=[objects.diagonal_laser2() for i in range(5)]
for i in range(5):
    diagonal_lasers2[i].render(random.randint(50,500),random.randint(15,25))


while(1):
    keypressed=input.getpress()
    if keypressed=='q':
        quit()
    if keypressed!='w':
        mando.move(keypressed,2)
        mando.gravity()
    if keypressed!='s':
        mando.move(keypressed,2)

    for i in variables.bullet_list:
        if i.hascollided() or i.getx()>variables.screenpos+variables.screenlength:
            i.destroy()
            variables.bullet_list.remove(i)
            continue
        i.move()
        i.move()
        i.move()
        i.move()
    #Moving the screen move without Moving the Mando
    if(variables.screenpos<variables.board_length-300):
        mando.move('d',2)
        variables.screenpos=variables.screenpos+2
    boss.destroy()
    if(mando.gety()>20):
        boss.render(boss.getx(),mando.gety())
    else:
        boss.render(boss.getx(),boss.gety())

    variables.scene.showboard(variables.screenpos)
    variables.last_ground_touch=variables.last_ground_touch+1
