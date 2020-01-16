#check whether coin and laser at the same time works
# TODO Implement collision detection for the movements
# TODO make gravity accelerating

import variables
import design
import time
class person:
    # initialises the length,height and coordinates of the character
    def __init__(self,character):
        self._length=len(character[0])
        self._height=len(character)
        self._character=character

    def render(self,x,y):
        self._xcoor=x
        self._ycoor=y
        for i in range(self._height):
            for j in range(self._length):
                variables.scene.change(i+y-self._height,j+x,self._character[i][j])


class Mandalorian(person):

    def __init__(self):
        self._character=design.mandalorian
        self._length=len(self._character[0])
        self._height=len(self._character)

    def move(self,c,num):
        for i in range(num):
            if c=='d':
                #collision detection with the screen ends
                if self._xcoor==variables.screenpos+variables.screenlength-self._length:
                    break

                #collision detection with lasers
                for i in range(self._height):
                    if (variables.scene.getxy(i+self._ycoor-self._height,self._xcoor+self._length) in ['|','0','-','\\','/']):
                        variables.scene.updatelives()
                        break

                #collecting coins
                for i in range(self._height):
                    if (variables.scene.getxy(i+self._ycoor-self._height,self._xcoor+self._length) == '$'):
                        variables.scene.updatescore(10)

                for i in range(self._height):
                    for j in range(self._length):
                        variables.scene.change(i+self._ycoor-self._height,j+self._xcoor+1,self._character[i][j])
                for i in range(self._height):
                    variables.scene.change(i+self._ycoor-self._height,self._xcoor,' ')
                self._xcoor=self._xcoor+1

            if c=='a':
                #collision detection with screen end
                if self._xcoor==variables.screenpos:
                    break

                #collecting coins
                for i in range(self._height):
                    if (variables.scene.getxy(i+self._ycoor-self._height,self._xcoor-1) == '$'):
                        variables.scene.updatescore(10)

                #collision detection with lasers
                for i in range(self._height):
                    if (variables.scene.getxy(i+self._ycoor-self._height,self._xcoor-1) in ['|','0','-','\\','/']):
                        variables.scene.updatelives()

                for i in range(self._height):
                    for j in range(self._length):
                        variables.scene.change(i+self._ycoor-self._height,j+self._xcoor-1,self._character[i][j])
                for i in range(self._height):
                    variables.scene.change(i+self._ycoor-self._height,self._xcoor+self._length-1,' ')
                self._xcoor=self._xcoor-1

            if c=='w':

                variables.last_ground_touch=0

                #collision detection with ceiling
                if(self._ycoor-self._height==3):
                    return

                #collecting coins
                for j in range(self._length):
                    if variables.scene.getxy(self._ycoor-2,j+self._xcoor) == "$":
                        variables.scene.updatescore(10)

                for i in range(self._height):
                    for j in range(self._length):
                        variables.scene.change(i+self._ycoor-1-self._height,j+self._xcoor,self._character[i][j])
                for j in range(self._length):
                    variables.scene.change(self._ycoor-1,self._xcoor+j,' ')
                self._ycoor=self._ycoor-1

    def gravity(self):

        for k in range(int(1+variables.last_ground_touch/5)):
            #collision detection with floor
            if self._ycoor==38:
                break

            #collecting coins
            for j in range(self._length):
                if variables.scene.getxy(self._ycoor,j+self._xcoor)=="$":
                    variables.scene.updatescore(10)

            for i in range(self._height):
                for j in range(self._length):
                    variables.scene.change(i+self._ycoor+1-self._height,j+self._xcoor,self._character[i][j])
            for j in range(self._length):
                variables.scene.change(self._ycoor-self._height,self._xcoor+j,' ')
            self._ycoor=self._ycoor+1

class destroyables(person):

    def __init__(self):
        self._length=len(self._character[0])
        self._height=len(self._character)

    def destroy(self):
        for i in range(self._height):
            for j in range(self._length):
                variables.scene.change(i+self._ycoor-self._height,j+self._xcoor,' ')

class vertical_laser(destroyables):

    def __init__(self):
        self._character=design.vertical_laser
        self._length=len(self._character[0])
        self._height=len(self._character)

class coins(destroyables):

    def __init__(self):
        self._character=design.coin
        self._length=1
        self._height=1

    def render(self,x,y):
        self._xcoor=x
        self._ycoor=y
        variables.scene.change(y,x,self._character)
