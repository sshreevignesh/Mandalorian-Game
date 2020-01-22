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
    coin[i].render(random.randint(10,variables.board_length-400),random.randint(5,35))

vertical_lasers=[objects.vertical_laser() for i in range(5)]
for i in range(5):
    vertical_lasers[i].render(random.randint(50,variables.board_length-400),random.randint(15,25))

horizontal_lasers=[objects.horizontal_laser() for i in range(5)]
for i in range(5):
    horizontal_lasers[i].render(random.randint(50,variables.board_length-400),random.randint(5,35))

diagonal_lasers1=[objects.diagonal_laser1() for i in range(5)]
for i in range(5):
    diagonal_lasers1[i].render(random.randint(50,variables.board_length-400),random.randint(15,25))

diagonal_lasers2=[objects.diagonal_laser2() for i in range(5)]
for i in range(5):
    diagonal_lasers2[i].render(random.randint(50,variables.board_length-400),random.randint(15,25))

magnet=objects.magnet()
magnet.render(random.randint(50,variables.board_length-400),random.randint(15,25))
iter=0
lasttime=0
while(1):
    iter=iter+1
    if variables.scene.getbosslives()<1:
        variables.scene.updatescore(5000)
        variables.scene.showboard(variables.screenpos)
        quit()
    keypressed=input.getpress()
    if keypressed=='q' or variables.scene.getlives()<'1':
        quit()
    if keypressed!='w':
        mando.move(keypressed,2)
        mando.gravity()
    if keypressed!='s'and keypressed!='f' and keypressed!='g':
        mando.move(keypressed,2)
        if variables.boost==1:
            mando.move(keypressed,2)
    if mando.getx()>variables.magnetx-50 and mando.getx()<variables.magnetx:
        mando.move('d',3)
    if mando.getx()<variables.magnetx+50 and mando.getx()>variables.magnetx:
        mando.move('a',3)
    for i in variables.bullet_list:
        if i.hascollided() or i.getx()>variables.screenpos+variables.screenlength:
            i.destroy()
            variables.bullet_list.remove(i)
            continue
        for j in range(4):
            i.move()
        if variables.boost==1:
            if i.hascollided() or i.getx()>variables.screenpos+variables.screenlength:
                i.destroy()
                variables.bullet_list.remove(i)
                continue
            for j in range(4):
                i.move()

    for i in variables.iceball_list:
        if i.hascollided() or i.getx()<variables.screenpos:
            i.destroy()
            variables.iceball_list.remove(i)
            continue
        for j in range(4):
            i.move()
        if variables.boost==1:
            if i.hascollided() or i.getx()>variables.screenpos+variables.screenlength:
                i.destroy()
                variables.iceball_list.remove(i)
                continue
            for j in range(4):
                i.move()


    #Moving the screen move without Moving the Mando
    if(variables.screenpos<variables.board_length-300):
        mando.move('d',2)
        variables.screenpos=variables.screenpos+2
        if variables.boost==1:
            mando.move('d',2)
            variables.screenpos=variables.screenpos+2
    boss.destroy()
    if(mando.gety()>20):
        boss.render(boss.getx(),mando.gety())
    else:
        boss.render(boss.getx(),boss.gety())

    if variables.screenpos > variables.board_length-400 and int(round(time.time()))-lasttime>2:
        boss.shoot()
        lasttime=int(round(time.time()))

    variables.scene.showboard(variables.screenpos)
    variables.last_ground_touch=variables.last_ground_touch+1
    if variables.boost==1:
        variables.last_ground_touch=variables.last_ground_touch+1
