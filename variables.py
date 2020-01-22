import numpy as np
import boards
import time

#board length and height
board_length=3000
board_height=40

# scene will be the board we use for the current game
scene= boards.board(board_length,board_height)

#screenlength will store the length that will be shown to the user at any given time
screenlength=170

#stores the number of iterations of continuous free fall
last_ground_touch=0

#stores the position of the screen
screenpos=0

#stores the list of bullets on screen
bullet_list=[]

#stores the list of iceballs
iceball_list=[]

#stores the health of boss
boss_health=100

#stores whether boost is on or not
boost=0

#stores position of the magnet
magnetx=0
