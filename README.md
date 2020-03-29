A terminal based arcade game in Python3 heavily inspired by Jetpack Joyride (without using any external libraries other than numpy and colorama)

## Introduction:
Din is a mandalorian living in the post-empire era. He is one of the last remaining members of his clan
in the galaxy and is currently on a mission for the Guild. He needs to rescue The Child, who strikingly
resembles Master Yoda, a legendary Jedi grandmaster. But there are lots of enemies and obstacles in
his way, trying to prevent Din from saving Baby Yoda. Din is wearing classic mandalorian armour and
has a jetpack as well as a blaster with unlimited bullets. You’ve got to help him fight his way through
and rescue Baby Yoda.


The objective of the game is to collect as many coins as possible, fight the obstacles on the way, defeat
the boss enemy and rescue Baby Yoda. 

## For playing the game
```
git clone https://github.com/sshreevignesh/Mandalorian-Game.git
cd Mandalorian-Game/
python3 main.py
```
## Instructions for the game:

### Controls:
1) w to activate jetpack
2) a,d to move left and right
3) f for enabling/disabling speed boost (makes the game faster/slower)
4) g for shield (takes time to recharge)

### Scoring Rules:
1) 10 points per coin collected
2) 100 points per laser destroyed
3) 5000 points for killing boss

### Others:
1)Collison of bullet with coin will destroy the coin to dicourage the user from using a lot of bullets
2)When the mando collides with a laser, and has more than one life Remaining, he will respawn 10 blocks later

## Files 
* boards.py  - Contains the class and functions for the board
* design.py  - Contains the design for characters
* objects.py - Contains the class and functions for characters and objects
* getch.py and input.py - Contain code to get keypresses
* main.py - main file for the game

