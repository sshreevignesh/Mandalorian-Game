# TODO Implement collision detection for the movements
# TODO make gravity accelerating

import variables
import design
import time
class person:
    # initialises the length,height and coordinates of the character
    def __init__(self,character):
        self.length=len(character[0])
        self.height=len(character)
        self.character=character

    def render(self,x,y):
        self.xcoor=x
        self.ycoor=y
        for i in range(self.height):
            for j in range(self.length):
                variables.scene.change(i+y-self.height,j+x,self.character[i][j])


class Mandalorian(person):

    def __init__(self):
        self.character=design.mandalorian
        self.length=len(self.character[0])
        self.height=len(self.character)

    def move(self,c):

        if c=='d':
            for i in range(self.height):
                for j in range(self.length):
                    variables.scene.change(i+self.ycoor-self.height,j+self.xcoor+1,self.character[i][j])
            for i in range(self.height):
                variables.scene.change(i+self.ycoor-self.height,self.xcoor,' ')
            self.xcoor=self.xcoor+1

        if c=='a':
            for i in range(self.height):
                for j in range(self.length):
                    variables.scene.change(i+self.ycoor-self.height,j+self.xcoor-1,self.character[i][j])
            for i in range(self.height):
                variables.scene.change(i+self.ycoor-self.height,self.xcoor+self.length-1,' ')
            self.xcoor=self.xcoor-1

        if c=='w':

            #collision detection with ceiling
            for j in range(self.length):
                if(variables.scene.getxy(self.ycoor-self.height-1,j+self.xcoor)!=' '):
                    return

            for i in range(self.height):
                for j in range(self.length):
                    variables.scene.change(i+self.ycoor-1-self.height,j+self.xcoor,self.character[i][j])
            for j in range(self.length):
                variables.scene.change(self.ycoor-1,self.xcoor+j,' ')
            self.ycoor=self.ycoor-1

    def gravity(self):

        if variables.count<4:
            return

        #collision detection with floor
        for j in range(self.length):
            if(variables.scene.getxy(self.ycoor,j+self.xcoor)!=' '):
                last_ground_touch=0
                return

        for i in range(self.height):
            for j in range(self.length):
                variables.scene.change(i+self.ycoor+1-self.height,j+self.xcoor,self.character[i][j])
        for j in range(self.length):
            variables.scene.change(self.ycoor-self.height,self.xcoor+j,' ')
        self.ycoor=self.ycoor+1
        variables.count=0
