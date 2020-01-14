import numpy as np

class board:
    def __init__(self,length,height):
        self.matrix=np.empty((height,length), dtype='str')
        self.matrix[:] = ' '
        self.height=height
        self.length=length
        for i in range(self.length):
            self.matrix[0][i]='_'
            self.matrix[1][i]='_'
            self.matrix[height-1][i]='_'
            self.matrix[height-2][i]='_'

    def showboard(self,x):
        #Setting the cursor to (0,0)
        print('\033[0;0H')
        for i in range(len(self.matrix)):
            for j in range(x,x+170):
                print(self.matrix[i][j],end = "")
            print(" ")

    def change(self,x,y,c):
        self.matrix[x][y]=c

    def getxy(self,x,y):
        return self.matrix[x][y]
