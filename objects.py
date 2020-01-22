#Boss loses two lives on one bullet, fix that
#Colour
#Shield
#Boss attack
#fix falling on horizontal laser (Try collison with ycoor-1 or something)
#check whether coin and laser at the same time works
#check if collison works properly with inputs other than 'd'
# TODO Implement collision detection for the movements

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

    def getx(self):
        return self._xcoor

    def gety(self):
        return self._ycoor

class Mandalorian(person):

    def __init__(self):
        self._character=design.mandalorian
        self._length=len(self._character[0])
        self._height=len(self._character)

    def shoot(self):
        bullet1= bullet()
        bullet1.render(self._xcoor+4,self._ycoor-4)
        variables.bullet_list.append(bullet1)

    def boost(self):
        variables.boost=(variables.boost+1)%2

    def move(self,c,num):
        for i in range(num):
            if c=='d':
                #collision detection with the screen ends
                if self._xcoor==variables.screenpos+variables.screenlength-self._length:
                    break

                if self._xcoor==variables.board_length-210:
                    break

                #collision detection with lasers
                for i in range(self._height):
                    if (variables.scene.getxy(i+self._ycoor-self._height,self._xcoor+self._length) in ['|','0','-','\\','/']):
                        for i in range(self._height):
                            for j in range(self._length):
                                variables.scene.change(i+self._ycoor-self._height,j+self._xcoor,' ')
                        self._xcoor=self._xcoor+15
                        self.render(self._xcoor,self._ycoor)
                        variables.scene.updatelives()
                        break

                #collecting coins
                for i in range(self._height):
                    if (variables.scene.getxy(i+self._ycoor-self._height,self._xcoor+self._length) == '$'):
                        variables.scene.change(i+self._ycoor-self._height,self._xcoor+self._length," ")
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
                        variables.scene.change(i+self._ycoor-self._height,self._xcoor-1," ")
                        variables.scene.updatescore(10)

                #collision detection with lasers
                for i in range(self._height):
                    if (variables.scene.getxy(i+self._ycoor-self._height,self._xcoor-1) in ['|','0','-','\\','/']):
                        self.move('d',10)
                        variables.scene.updatelives()
                        break

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
                    if variables.scene.getxy(self._ycoor-self._height-1,j+self._xcoor) == "$":
                        variables.scene.change(self._ycoor-self._height-1,j+self._xcoor," ")
                        variables.scene.updatescore(10)

                #collision detection with lasers
                for j in range(self._length):
                    if variables.scene.getxy(self._ycoor-self._height-1,j+self._xcoor in ['|','0','-','\\','/']):
                        self.move('d',10)
                        variables.scene.updatelives()
                        break

                for i in range(self._height):
                    for j in range(self._length):
                        variables.scene.change(i+self._ycoor-1-self._height,j+self._xcoor,self._character[i][j])
                for j in range(self._length):
                    variables.scene.change(self._ycoor-1,self._xcoor+j,' ')
                self._ycoor=self._ycoor-1

            if c=='s':
                if i==0:
                    self.shoot()

            if c=='f':
                self.boost()
                break

    def gravity(self):

        for k in range(int(1+variables.last_ground_touch/5)):
            #collision detection with floor
            if self._ycoor==38:
                break

            #collecting coins
            for j in range(self._length):
                if variables.scene.getxy(self._ycoor,j+self._xcoor)=="$":
                    variables.scene.change(self._ycoor,j+self._xcoor," ")
                    variables.scene.updatescore(10)

            #collision detection with lasers
            for j in range(self._length):
                if variables.scene.getxy(self._ycoor-1,j+self._xcoor in ['|','0','-','\\','/']):
                    self.move('d',10)
                    variables.scene.updatelives()
                    break

            for i in range(self._height):
                for j in range(self._length):
                    variables.scene.change(i+self._ycoor+1-self._height,j+self._xcoor,self._character[i][j])
            for j in range(self._length):
                variables.scene.change(self._ycoor-self._height,self._xcoor+j,' ')
            self._ycoor=self._ycoor+1

class dragon(person):
    def __init__(self):
        self._character=design.dragon
        self._length=len(self._character[0])
        self._height=len(self._character)

    def destroy(self):
        for i in range(self._height):
            for j in range(self._length):
                variables.scene.change(i+self._ycoor-self._height,j+self._xcoor,' ')

    def shoot(self):
        iceball1= iceball()
        iceball1.render(self._xcoor-100,self._ycoor)
        variables.iceball_list.append(iceball1)


class destroyables(person):

    def __init__(self):
        self._length=len(self._character[0])
        self._height=len(self._character)

    def render(self,x,y):
        self._xcoor=x
        self._ycoor=y
        for i in range(self._height):
            for j in range(self._length):
                variables.scene.change(i+y-self._height,j+x,self._character[i][j])
    def destroy(self):
        for i in range(self._height):
            for j in range(self._length):
                variables.scene.change(i+self._ycoor-self._height,j+self._xcoor,' ')

class vertical_laser(destroyables):

    def __init__(self):
        self._character=design.vertical_laser
        self._length=len(self._character[0])
        self._height=len(self._character)

class horizontal_laser(destroyables):

    def __init__(self):
        self._character=design.horizontal_laser
        self._length=len(self._character[0])
        self._height=len(self._character)

class diagonal_laser1(destroyables):

    def __init__(self):
        self._character=design.diagonal_laser1
        self._length=len(self._character[0])
        self._height=len(self._character)

class diagonal_laser2(destroyables):

    def __init__(self):
        self._character=design.diagonal_laser2
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

class bullet(destroyables):

    def __init__(self):
        self._character=design.bullet
        self._length=1
        self._height=1
        self._collided=0

    def getx(self):
        return self._xcoor
    def render(self,x,y):
        self._xcoor=x
        self._ycoor=y
        variables.scene.change(y,x,self._character)

    def destroy(self):
        variables.scene.change(self._ycoor,self._xcoor,' ')

    def collison(self,c):
        if self._xcoor > variables.board_length-200:
            variables.scene.updatebosslives()
            self._collided=1
            self.destroy()
            return
        if c=='|':
            y=self._ycoor
            while(variables.scene.getxy(y,self._xcoor)=="|"):
                variables.scene.change(y,self._xcoor," ")
                y=y-1
            variables.scene.change(y,self._xcoor," ")
            y=self._ycoor+1
            while(variables.scene.getxy(y,self._xcoor)=="|"):
                variables.scene.change(y,self._xcoor," ")
                y=y+1
            variables.scene.change(y,self._xcoor," ")
            variables.scene.updatescore(100)
            self._collided=1
            self.destroy()

        if c=='/':
            y=self._ycoor
            x=self._xcoor
            while(variables.scene.getxy(y,x)=="/"):
                variables.scene.change(y,x," ")
                y=y-1
                x=x+1
            variables.scene.change(y,x," ")
            y=self._ycoor+1
            x=self._xcoor-1
            while(variables.scene.getxy(y,x)=="/"):
                variables.scene.change(y,x," ")
                y=y+1
                x=x-1
            variables.scene.change(y,x," ")
            variables.scene.updatescore(100)
            self._collided=1
            self.destroy()

        if c=='\\':
            y=self._ycoor
            x=self._xcoor
            while(variables.scene.getxy(y,x)=="\\"):
                variables.scene.change(y,x," ")
                y=y+1
                x=x+1
            variables.scene.change(y,x," ")
            y=self._ycoor-1
            x=self._xcoor-1
            while(variables.scene.getxy(y,x)=="\\"):
                variables.scene.change(y,x," ")
                y=y-1
                x=x-1
            variables.scene.change(y,x," ")
            variables.scene.updatescore(100)
            self._collided=1
            self.destroy()

    def move(self):
        self.destroy()
        self._xcoor=self._xcoor+1
        if(variables.scene.getxy(self._ycoor,self._xcoor)==' '):
            self.render(self._xcoor,self._ycoor)
            return
        self.collison(variables.scene.getxy(self._ycoor,self._xcoor))

    def hascollided(self):
        return self._collided

class magnet(destroyables):
    def __init__(self):
        self._character=design.magnet
        self._length=len(self._character[0])
        self._height=len(self._character)

    def render(self,x,y):
        self._xcoor=x
        self._ycoor=y
        for i in range(self._height):
            for j in range(self._length):
                variables.scene.change(i+y-self._height,j+x,self._character[i][j])
        variables.magnetx=x

class iceball(destroyables):

    def __init__(self):
        self._character=design.snowball
        self._length=1
        self._height=1
        self._collided=0

    def getx(self):
        return self._xcoor

    def render(self,x,y):
        self._xcoor=x
        self._ycoor=y
        variables.scene.change(y,x,self._character)

    def destroy(self):
        variables.scene.change(self._ycoor,self._xcoor,' ')

    def collison(self):
        self._collided=1
        self.destroy()
        variables.scene.updatelives()

    def move(self):
        self.destroy()
        self._xcoor=self._xcoor-1
        if(variables.scene.getxy(self._ycoor,self._xcoor)==' '):
            self.render(self._xcoor,self._ycoor)
            return
        self.collison(variables.scene.getxy(self._ycoor,self._xcoor))

    def hascollided(self):
        return self._collided
