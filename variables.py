import numpy as np
import boards
#board length and height
board_length=300
board_height=40
# scene will be the board we use for the current game
scene= boards.board(board_length,board_height)
#lives will store the remaining lives
lives=3
#count will store the number of iterations withot pressing w (for gravity)
count = 0
#stores the number of iterations of continuous free fall
last_ground_touch=0
screenpos=0
