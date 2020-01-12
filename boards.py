import numpy as np

class board:
    def __init__(self,length,height):
        self.matrix=np.empty((height,length), dtype='str')
        self.matrix[:] = '.'

    def showboard(self,x):
        for i in range(len(self.matrix)):
            for j in range(x,x+170):
                print(self.matrix[i][j],end = "")
            print(" ")

    def change(self,x,y,c):
        self.matrix[x][y]=c

    def getxy(self,x,y):
        return self.matrix[x][y]
