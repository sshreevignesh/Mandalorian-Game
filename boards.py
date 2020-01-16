import numpy as np
import variables
class board:
    def __init__(self,length,height):
        self.__matrix=np.empty((height,length), dtype='str')
        self.__matrix[:] = ' '
        self.__height=height
        self.__length=length
        self._score='0'
        self._lives='3'
        temp=list("LIVES: "+self._lives+"    Score: "+self._score)
        for i in range(len(temp)):
            self.__matrix[1][i]=temp[i]
        for i in range(self.__length):
            self.__matrix[0][i]='_'
            self.__matrix[2][i]='_'
            self.__matrix[height-1][i]='_'
            self.__matrix[height-2][i]='_'

    def showboard(self,x):
        temp=list("LIVES : "+self._lives+"  Score : "+self._score)
        for i in range(len(temp)):
            self.__matrix[1][i+x]=temp[i]
        #Setting the cursor to (0,0)
        print('\033[0;0H')
        for i in range(len(self.__matrix)):
            for j in range(x,x+variables.screenlength):
                print(self.__matrix[i][j],end = "")
            print(" ")

    def change(self,x,y,c):
        self.__matrix[x][y]=c

    def getxy(self,x,y):
        return self.__matrix[x][y]

    def updatelives(self):
        self._lives=str(int(self._lives)-1)

    def updatescore(self,points):
        self._score=str(int(self._score)+points)
