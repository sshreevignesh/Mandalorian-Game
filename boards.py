import numpy as np
import variables
import time
class board:
    def __init__(self,length,height):
        self.__matrix=np.empty((height,length), dtype='str')
        self.__matrix[:] = ' '
        self.__height=height
        self.__length=length
        self._score='0'
        self._lives='3'
        self._bosslives=100
        self._start_time=int(round(time.time()))
        temp=list("LIVES: "+self._lives+"    Score: "+self._score + "     Boss Lives : "+ str(self._bosslives) + "     Time Remaining :" +str(200-int(round(time.time()))+self._start_time)+"   ")
        for i in range(len(temp)):
            self.__matrix[1][i]=temp[i]
        for i in range(self.__length):
            self.__matrix[0][i]='_'
            self.__matrix[2][i]='_'
            self.__matrix[height-1][i]='_'
            self.__matrix[height-2][i]='_'

    def showboard(self,x):
        if 200-int(round(time.time()))+self._start_time < 0:
            quit()
        temp=list("LIVES : "+self._lives+"   Score: "+self._score + "     Boss Lives : "+ str(self._bosslives) + "     Time Remaining :"+str(200-int(round(time.time()))+self._start_time)+"   ")
        for i in range(len(temp)):
            self.__matrix[1][i+x]=temp[i]
        #Setting the cursor to (0,0)
        print('\033[0;0H')
        for i in range(len(self.__matrix)):
            for j in range(x,x+variables.screenlength):
                ch='\x1b[6;30;42m'+self.__matrix[i][j]+'\x1b[0m'
                if self.__matrix[i][j]=='$':
                    ch='\x1b[6;30;43m'+self.__matrix[i][j]+'\x1b[0m'
                print(ch,end = "")
            print(" ")

    def change(self,x,y,c):
            self.__matrix[x][y]=c

    def getxy(self,x,y):
        return self.__matrix[x][y]

    def updatelives(self):
        self._lives=str(int(self._lives)-1)

    def updatescore(self,points):
        self._score=str(int(self._score)+points)

    def getlives(self):
        return self._lives

    def getbosslives(self):
        return self._bosslives

    def updatebosslives(self):
        self._bosslives=self._bosslives-1
