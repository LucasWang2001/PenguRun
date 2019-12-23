#This game is meant to be a rage game, a game that induces anger in the player by being purposefully unfair or extremely difficult. There are no checkpoints, and the game is 
#almost impossible to complete (it has been done). Enjoy :)

from random import *
from tkinter import *
from math import *
from pprint import pprint
from pygame import *
root=Tk()
root.withdraw()
init()
font.init()
mixer.init()
snowFont=font.SysFont("Snowtop Caps",60) #death counter font
snowFont2=font.SysFont("Snowtop Caps",30) #menu buttons text
mixer.music.load('music//menumusic.mp3') #game music

RED  =(255,0,0) #tuple - a list that can not be changed!
GREEN=(0,255,0)
BLUE= (0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

size = width, height = 1215, 810
screen = display.set_mode(size)
myClock = time.Clock()



######################################-Variables-#########################################
X=0 #penguin X position
Y=1 #penguin Y position
VY=2 #penguin vertical Y position
ONGROUND=3
frame=0 #frame number of penguin sprite
sleepframe=0 #frame number of sleeping penguin sprite
respawnframe=0 #frame number of respawning penguin sprite
eggframe=0 #frame number of egg penguin sprite
yayframe=0 #frame number of cheering penguin sprite
frameDelay=8 #frame delay
respawnDelay=50 #respawn frame delay
blocklist=[] #list of all ice blocks in the maps
spikelist=[] #list of all the spikes in the maps
penguin=[44,200,0,True] #penguin X,Y
penguinrect=Rect(penguin[X],penguin[Y],40,45) #rectangle around the penguin model
respawnx=0 #respawn X location
respawny=0 #respawn Y location
respawn=False #respawn variable
jump=False #jump variable
stop=True #stop variable
left=False #left walk variable
right=False #right walk variable
duck=False #duck variable
face='right' #direction the penguin is facing (right or left)
buttons=[Rect(500,y*80+450,200,40) for y in range(4)] #menu buttons
vals=["game","instructions","credits"] #values for buttons
page = "intro" #starting page
levelNum=0 #level number list
endList=[] #end block list
deathCounter=0 #death counter
snowList=[] #snowflakes list
scrollX=0 #scroll variable
storyNum=0 #story counter
continueRect=Rect(400,400,135,45) #rectangle that continues from story to game

#######################################-Levels-##############################################
##  0 indicates no block
##  1 indicates an ice block
##  2 indicates a spike
##  3 indicates the end snowflake
##  5 indicates the penguin spawn/respawn position

level1=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
 [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0, 0, 0, 0],
 [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0],
 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0],
 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
 [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
 [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

level2=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 2,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 0, 2, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
 [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 1],
 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 2, 1, 0, 1],
 [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
 [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
 [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 1],
 [1, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1, 1],
 [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1]]

level3=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
 [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
 [5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level4=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0],
 [0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 1, 2, 0, 0],
 [5, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 3],
 [1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

level5=[[1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [5, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
 [1, 2, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 2, 0, 0, 1],
 [1, 0, 0, 2, 1, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 1, 1, 1, 0, 2, 1],
 [1, 0, 2, 0, 2, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 1, 1, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
 [1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 2, 0, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 2, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 1],
 [1, 0, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1, 1],
 [1, 0, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1]]

level6=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0],
 [0, 2, 0, 2, 1, 0, 2, 0, 2, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 0],
 [5, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 3],
 [1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

level7=[[0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
 [0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0],
 [5, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 2, 3],
 [1, 0, 0, 0, 0, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 1, 2, 2, 0, 0, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 1, 1 ,1, 1, 2, 2, 1, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1],
 [1, 0, 0, 2, 0, 1, 1, 1, 2, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 2, 0, 2, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1],
 [1, 0, 0, 1, 0, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

level8=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
 [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 1, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
 [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0],
 [0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [5, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

level9=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0],
 [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [5, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]]

levelslist=[level1,level2,level3,level4,level5,level6,level7, level8, level9] #list of levels
#####################-Loading/Transforming Images-########################
penguinSprite=image.load('penguin sprites\\stop.png') #penguin stop sprite
duckRight=image.load('penguin sprites\\duckright.png') #penguin duck right sprite
duckLeft=image.load('penguin sprites\\duckleft.png') #penguin duck left sprite

leftPics=[] #list for left walk sprites
for i in range(4):
    leftPics.append(image.load("penguin sprites\\leftwalk" + str(i+1) + ".png")) #penguin left walk sprites
    
rightPics=[] #list for right walk sprites
for i in range(4):
    rightPics.append(image.load("penguin sprites\\rightwalk" + str(i+1) + ".png")) #penguin right walk sprites
    
sleep=[] #list for sleeping sprites
for i in range(20):
    sleep.append(image.load("penguin sprites\\sleep" + str(i+1) + ".png")) #penguin sleeping sprites
    
snowblock=image.load("images/snowblock.png") #snowblock image
spike=image.load("images/spike.png") #spike image
iceblock=image.load("images/iceblock.png") #iceblock image
background=image.load("images/snowbackground.png") #background for the levels
spike=transform.scale(spike,(45,45)) #transforming spike
background=transform.scale(background,(1215,810)) #transforming background
instructions=image.load('images\\instructions.png') #instructions image
credits1=image.load('images\\credits.png') #credits image

egg=[] #list for egg sprites
for i in range(23):
    egg.append(image.load('penguin sprites\\egg'+str(i+1)+'.png')) #penguin egg sprites

yay=[] #list for celebration sprites
for i in range(12): 
    yay.append(image.load('penguin sprites\\dance'+str(i+1)+'.png')) #penguin celebration sprites
    
grey1=[] #list for grey penguin sprites
for i in range(4):
    grey1.append(image.load("images/greyrightwalk" + str(i+1) + ".png")) #grey penguin walking sprites
    
red1=[] #list for red penguin sprites
for i in range(4):
    red1.append(image.load("images/redrightwalk" + str(i+1) + ".png")) #red penguin walking sprites
    
orange1=[] #list for orange penguin sprites
for i in range(4):
    orange1.append(image.load("images/orangerightwalk" + str(i+1) + ".png")) #orange penguin walking sprites
    
yellow1=[] #list for yellow penguin sprites
for i in range(4):
    yellow1.append(image.load("images/yellowrightwalk" + str(i+1) + ".png")) #yellow penguin walking sprites
    
green1=[] #list for green penguin sprites
for i in range(4):
    green1.append(image.load("images/greenrightwalk" + str(i+1) + ".png")) #green penguin walking sprites
    
blue1=[] #list for blue penguin sprites
for i in range(4):
    blue1.append(image.load("images/bluerightwalk" + str(i+1) + ".png")) #blue penguin walking sprites
    
indigo1=[] #list for indigo penguin sprites
for i in range(4):
    indigo1.append(image.load("images/indigorightwalk" + str(i+1) + ".png")) #indigo penguin walking sprites
    
violet1=[] #list for violet penguin sprites
for i in range(4):
    violet1.append(image.load("images/violetrightwalk" + str(i+1) + ".png")) #violet penguin walking sprites
    
rainbow1=[] #list for red penguin sprites
for i in range(4):
    rainbow1.append(image.load("images/rainbowrightwalk" + str(i+1) + ".png")) #red penguin walking sprites

bc1=image.load('penguin sprites\\red1.png') #images for intro screen
bc2=image.load('penguin sprites\\blue1.png')
bc3=image.load('penguin sprites\\green1.png')
bc4=image.load('penguin sprites\\mint1.png')
bc5=image.load('penguin sprites\\yellow1.png')
bc6=image.load('penguin sprites\\purple1.png')
bc7=image.load('penguin sprites\\pink1.png')
bc8=image.load('penguin sprites\\orange1.png')
bc9=image.load('penguin sprites\\grey1.png')

end=image.load('images\\end.png') #end snowflake image

scrollingBackground=image.load("images/snowbackground.png").convert() #scrolling background
scrollingBackground=transform.scale(scrollingBackground,(1215,810)).convert() #transformed scrolling background

continuePic=image.load('images\\continue.png') #continue arrow image

title=image.load('images\\title.png')

storyList=[] #list for story images
for i in range(9):
    storyList.append(image.load('images\\story'+str(i+1)+'.png')) #story images

#end screen celebration penguins
blue=[]
for i in range(4):
    blue.append(image.load("images\\blue" + str(i+1) + ".png"))
red=[]
for i in range(4):
    red.append(image.load("images\\red" + str(i+1) + ".png"))
green=[]
for i in range(4):
    green.append(image.load("images\\green" + str(i+1) + ".png"))
eating=[]
for i in range (4):
    eating.append(image.load("images\\eating" + str(i+1) + ".png"))
xred=[]
for i in range (4):
    xred.append(image.load("images\\xred" + str(i+1) + ".png"))
xblue=[]
for i in range (4):
    xblue.append(image.load("images\\xblue" + str(i+1) + ".png"))
xgreen=[]
for i in range (4):
    xgreen.append(image.load("images\\xgreen" + str(i+1) + ".png"))
ygreen=[]
for i in range (4):
    ygreen.append(image.load("images\\ygreen" + str(i+1) + ".png"))
red1right=[]
for i in range(4):
    red1right.append(image.load("images/red1rightwalk" + str(i+1) + ".png"))
orange1right=[]
for i in range(4):
    orange1right.append(image.load("images/orange1rightwalk" + str(i+1) + ".png"))
yellow1right=[]
for i in range(4):
    yellow1right.append(image.load("images/yellow1rightwalk" + str(i+1) + ".png"))
green1right=[]
for i in range(4):
    green1right.append(image.load("images/green1rightwalk" + str(i+1) + ".png"))
blue1left=[]
for i in range(4):
    blue1left.append(image.load("images/blue1rightwalk" + str(i+1) + ".png"))
indigo1left=[]
for i in range(4):
    indigo1left.append(image.load("images/indigo1rightwalk" + str(i+1) + ".png"))
violet1left=[]
for i in range(4):
    violet1left.append(image.load("images/violet1rightwalk" + str(i+1) + ".png"))
rainbow1left=[]
for i in range(4):
    rainbow1left.append(image.load("images/rainbow1rightwalk" + str(i+1) + ".png"))

########################-Functions-#########################
def gamefunction(level): #calling all the functions to change the levels each time
    global penguin, blocklist,spikelist
    blocklist=[]
    spikelist=[]
    drawrect(level)
    penguinspawn(level)
    move(penguin)
    interact(penguinrect,blocklist)
    drawScene(penguin,level)
    
    
def drawrect(level): #takes in a level as parameter
    global endList, blocklist,spikelist, penguinrect,X,Y #our global variables
    blockcounter=0 #amount of blocks
    spikecounter=0 #amount of spikes
    endcounter=0 #number of end gates
    
    for y in range(len(level)):#rows
        for x in range(len(level[y])):#columns
            if level[y][x]==1: #1's are normal blocks
                blockcounter+=1
                for i in range(blockcounter): #creating rectangles for every normal block
                    blocklist.append(Rect(x*45,y*45,43,45))
            elif level[y][x]==2: #2's are spikes
                spikecounter+=1
                for i in range(spikecounter): #creating rectangles for every spike
                    spikelist.append(Rect(x*45,y*45,40,40))
            elif level[y][x]==3: #3's are the end gates
                endcounter+=1
                for i in range(endcounter):
                    endList.append(Rect(x*45,y*45,45,45))

                                              
def drawScene(penguins,level):
    global respawn,frame,jump,right,left,stop,duck,penguin,X,Y,penguinrect,bullets,frameDelay, respawnframe, respawnpics, face, levelNum #our global variables
    screen.fill(WHITE)
    screen.blit(background,(0,0))
    
    if checkspikes(penguin[X],penguin[Y]): #if penguin collides with a spike
        respawn=True #we're respawning him
        
    if penguin[Y]==855: #if penguin falls off screen
        respawn=True #we're respawning him
        
    if respawn: #if he's respawning
        if respawnframe==9: #frame delay
            screen.blit(respawnpics[respawnframe],(respawnx,respawny))#blit this
        respawn=False
        
    if stop: #if not moving
        jump=False
        left=False
        right=False
        duck=False
        
        if respawn==False: #if he's not dead and respawning
            screen.blit(penguinSprite,(penguin[X],penguin[Y]))
            
    if jump: #if jumping
        if respawn==False: #if he's not dead and respawning
            screen.blit(penguinSprite,(penguin[X],penguin[Y]))
    if left: #if moving to left
        if respawn==False: #if he's not dead and respawning
            screen.blit(leftPics[frame],(penguin[X],penguin[Y]))
    if right: #if moving to right
        if respawn==False: #if he's not dead and respawning
            screen.blit(rightPics[frame],(penguin[X],penguin[Y]))
    if duck: #if ducking
        if respawn==False: #if he's not dead and respawning
            if face=='left':
                screen.blit(duckLeft,(penguin[X],penguin[Y]))
            else:
                screen.blit(duckRight,(penguin[X],penguin[Y]))
    
    for y in range(len(level)): #now we're bliting the blocks in the level
        for x in range(len(level[y])):
            if level[y][x]==1: #normal block
                screen.blit(iceblock,(x*45,y*45))
            elif level[y][x]==2: #floating spikes
                screen.blit(spike,(x*45,y*45))
            elif level[y][x]==3:
                screen.blit(end,(x*45,y*45))

        
    display.flip()

def move(penguin):
    keys=key.get_pressed()
    global deathCounter, levelNum,left,right,stop,jump,duck,penguinrect,respawnx,respawny, face, storyNum, page #global variables
    
    if checkspikes(penguin[X],penguin[Y])==True: #if contact with spike
        penguin[X]=respawnx #resetting variables if he touches spike and dies
        penguin[Y]=respawny
        deathCounter+=1 #death counter +1
        
    if penguin[Y]==855:
        penguin[X]=respawnx #resetting variables if he falls off map and dies
        penguin[Y]=respawny
        deathCounter+=1 #death counter +1
        
    if keys[K_LEFT] and penguin[X]>0 and not checkwalls(penguin[X]-7,penguin[Y]): #moving left and checking if penguinrect collides with wall a step before, and if there's no collision, then move
        left=True
        right=False
        stop=False
        jump=False
        duck=False
        face='left'
        penguin[X]-=8 #moving penguin 8 pixels to the left
        
    if keys[K_RIGHT] and penguin[X]<1170 and not checkwalls(penguin[X]+7,penguin[Y]):#moving right and checking if penguinrect collides with wall a step before, and if there's no collision, then move
        right=True
        left=False
        stop=False
        jump=False
        duck=False
        face='right'
        penguin[X]+=8 #moving penguin 8 pixels to the right
        
    if keys[K_UP] and penguin[ONGROUND]: #jumping only if he's on ground
        jump=True
        stop=False
        right=False
        left=False
        duck=False
        penguin[ONGROUND]=False
        penguin[VY]=-16 #moving penguin 16 pixels up
        
    if keys[K_DOWN] and penguin[ONGROUND]==False:
        if penguin[VY]<0:
            penguin[VY]=0
        penguin[VY]=penguin[VY]*1.5
        penguin[Y]+=(penguin[VY]*1.5) #accelerating the penguin's falling if crouch is pressed
        
    if keys[K_DOWN] and penguin[ONGROUND]: #ducking only if he's on ground
        duck=True
        jump=False
        stop=False
        right=False
        left=False
        
    if not checkwalls(penguin[X],penguin[Y]-7): #checking if top of penguin doesn't collide with block, then move y coordinate
        penguin[Y]+=penguin[VY]
        
    elif checkwalls(penguin[X],penguin[Y]-45): #checking if top of penguin collides, then freeze y coordinate 
        penguin[Y]=penguin[Y]
        
        if penguin[VY]>0: #so penguin doesn't go into the block, only changing y coordinate as he falls down
            penguin[Y]=penguin[Y]+penguin[VY]
        penguin[VY]+=.9 #gravity
        
    if penguin[Y]>=855: #setting a barrier on bottom of map
        penguin[Y]=855
        penguin[VY]=0
        penguin[ONGROUND]=False
        
    if checkEnd(penguin[X],penguin[Y]): #if penguin collides with end gate
        levelNum+=1
        if levelNum==9:
            page='end'
        elif levelNum<((len(levelslist))-1): #so no list error
            storyNum+=1 #story moves up one
            page='story' #sets page to story
            for y in range(len(levelslist[levelNum])): #finding spawn point of next level
                for x in range(len(levelslist[levelNum][y])):
                    if (levelslist[levelNum])[y][x]==5:
                        penguin[X]=x*45 #spawning penguin there so it doesn't continuously increase the level
                        penguin[Y]=y*45
        
    penguin[VY]+=.9 #gravity
    penguinrect=Rect(penguin[X],penguin[Y],40,45)#resetting penguinrect points after all the input from user 

def checkwalls(x,y): #takes in coordinates to check
    global blocklist
    penguinRect=Rect(x+2,y,40,45)
    return penguinRect.collidelist(blocklist) >=0 #returns true or false, true if they collide and false if they don't

def checkspikes(x,y): #takes in coordinates to check
    global spikelist
    penguinRect=Rect(x,y,40,45)
    return penguinRect.collidelist(spikelist) >=0 #returns true or false, true if they collide and false if they don't

def checkEnd(x,y):
    global endList, story, storyNum
    penguinRect=Rect(x,y,40,45)
    return penguinRect.collidelist(endList)>=0
    
  
def interact(playerrect,somelist): #only for top of blocks
    global penguinrect,blocklist,spikelist
    for i in blocklist: #for every block on map
        if penguinrect.colliderect(i): #if penguin collides with the block
            if penguin[VY]>0 and penguinrect.move(0,-45).colliderect(i)==False: #if penguin is falling and collides with the bottom of the block
                penguin[ONGROUND]=True #he's on a platform
                penguin[VY] = 0 #penguin doesn't fall anymore
                penguin[Y] = i.y - 45 #changing the y coordinate so he stays on the top of the block
                
def penguinspawn(level): #spawning the penguin
    global respawnx, respawny,penguinrect,X,Y
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x]==5: #5 is the location where the penguin spawns in the 2d list
                penguin=[x*45,y*45,0,True] #setting variables 
                respawnx=x*45-1
                respawny=y*45

for i in range (150):
    x=randint(0,1215)
    y=randint(0,810)
    snowList.append([x,y]) #appending coordinates into a snow list

                
#######################MENU#################################
def menu():
    global frame, frameDelay, buttons, vals, page, scrollingBackground, scrollX, myClock, grey1, red1, orange1, yellow1, green1, blue1, indigo1, violet1, rainbow1
    mpos=mouse.get_pos()
    mb=mouse.get_pressed()
    
    screen.fill(WHITE)
    
    original_scrollX = scrollX % scrollingBackground.get_rect().width #dividing x by the width of the bk image and returning the remainder
    screen.blit(scrollingBackground, (original_scrollX - scrollingBackground.get_rect().width, 0)) #deducting the width of the background so the reletive position is on the x and not blit back
    
    if original_scrollX <width:                                      #so when it reaches the end of the bk, it blit backs to the front
        screen.blit(scrollingBackground, (original_scrollX,0))                      #just blits another background image at the end of the last image
        myClock.tick(120)
        
    scrollX -=1

    #snow
    for i in range(len(snowList)):
        draw.circle(screen,WHITE,snowList[i],2) #drawing snow
        snowList[i][1]+=2 #making it fall
        if snowList[i][1]>810: #if it falls out of the screen, respawn it somewhere up top again
            y=randint(-50,-10)
            snowList[i][1]=y
            x=randint(0,1215)
            snowList[i][0]=x

    #walking penguins
    screen.blit(grey1[frame],(45,704))
    screen.blit(red1[frame],(180,704))
    screen.blit(orange1[frame],(315,704))
    screen.blit(yellow1[frame],(450,704))
    screen.blit(green1[frame],(585,704))
    screen.blit(blue1[frame],( 720,704))
    screen.blit(indigo1[frame],(855,704))
    screen.blit(violet1[frame],(990,704))
    screen.blit(rainbow1[frame],(1125,704))

    #frame delay
    frameDelay-=1                         
    if frameDelay==0:                     
        frameDelay=10
        frame+=1
        if frame==4:
            frame=0
            
    for j,k in zip(buttons,vals):
        draw.rect(screen,(44,113,160),j) #draw rectangle at button location
        
        if j.collidepoint(mpos): #if mouse collides with button
            draw.rect(screen,(0,196,107),j,4) #draw outline at button
            if mb[0]==1: #if clicked
                page=k #sets page to k (play, instructions, credits)
                if page=='game': #if page is game
                    page='story' #set page to story
        else:
            draw.rect(screen,(255,255,255),j,4) #outlines in white
            
    playText=snowFont2.render("Play",True,WHITE) #text for play button
    instrText=snowFont2.render("Instructions",True,WHITE) #text for instructions button
    credText=snowFont2.render("Credits",True,WHITE) #text for credits button
    screen.blit(playText,(568,450))
    screen.blit(instrText,(505,530))
    screen.blit(credText,(546,610))
    
    screen.blit(title,(290,200)) #game title
    
    display.flip()

##################################################3
running=True
mixer.music.play(-1) #plays music
while running:
    for evt in event.get():                # checks all events that happen
        if evt.type == QUIT:
            if page=='menu': #quits program if page is in menu
                running = False
                
            elif page=='intro': #quits program if page is in intro
                running=False
                
            elif page=='instructions': #returns to menu if page is in instructions
                page='menu'
                
            elif page=='credits': #returns to menu if page is in credits
                page='menu'
                
            elif page=='game': #quits program if page is in game
                running=False
                
            elif page=='story': #quits program if page is in story
                running=False

            elif page=='end':
                running=False
                
        if evt.type==KEYUP:
            stop=True
            
    if page=='intro': 
        screen.fill((255,255,255)) #fills with white

        #random coordinates on the screen
        randcord1=[randint(0,1216),randint(0,811)]
        randcord2=[randint(0,1216),randint(0,811)]
        randcord3=[randint(0,1216),randint(0,811)]
        randcord4=[randint(0,1216),randint(0,811)]
        randcord5=[randint(0,1216),randint(0,811)]
        randcord6=[randint(0,1216),randint(0,811)]
        randcord7=[randint(0,1216),randint(0,811)]
        randcord8=[randint(0,1216),randint(0,811)]
        randcord9=[randint(0,1216),randint(0,811)]
        for i in range(1): #blits colored penguin randomly all over the screen
            screen.blit(bc1,randcord1)
            screen.blit(bc2,randcord2)
            screen.blit(bc3,randcord3)
            screen.blit(bc4,randcord4)
            screen.blit(bc5,randcord5)
            screen.blit(bc6,randcord6)
            screen.blit(bc7,randcord7)
            screen.blit(bc8,randcord8)
            screen.blit(bc9,randcord9)
        
        screen.blit(egg[eggframe],(456,350)) #blits a hatching penguin in the middle of the screen

        #frame delay
        frameDelay-=1
        if frameDelay==0:                     
            frameDelay=16
            eggframe+=1
            if eggframe==23:
                page='menu' #once the penguin is done hatching page is set to menu
                
    elif page=='menu':
        menu() #runs menu function
        
    elif page=='instructions':
        screen.blit(instructions,(0,0)) #blits the instructions on the screen
        screen.blit(sleep[sleepframe],(540,650)) #blits a sleeping penguin on the screen

        #frame delay
        frameDelay-=1
        if frameDelay==0:                     
            frameDelay=10
            sleepframe+=1
            if sleepframe==20:
                sleepframe=0

        #snow
        for i in range(len(snowList)):
            draw.circle(screen,WHITE,snowList[i],2)
            snowList[i][1]+=4
            if snowList[i][1]>810:
                y=randint(-50,-10)
                snowList[i][1]=y
                x=randint(0,1215)
                snowList[i][0]=x
                
        display.flip()
        
    elif page=='credits':
        screen.blit(credits1,(0,0)) #blits credits on screen
        screen.blit(yay[yayframe],(540,650)) #blits celebrating penguin on screen

        #snow
        for i in range(len(snowList)):
            draw.circle(screen,WHITE,snowList[i],2)
            snowList[i][1]+=4
            if snowList[i][1]>810:
                y=randint(-50,-10)
                snowList[i][1]=y
                x=randint(0,1215)
                snowList[i][0]=x

        #frame delay
        frameDelay-=1
        respawnDelay-=0.2
        if frameDelay==0:                     
            frameDelay=6
            yayframe+=1
            if yayframe==12:
                yayframe=0
        display.flip()
        
    elif page=='game':
        #snow
        for i in range(len(snowList)):
            draw.circle(screen,WHITE,snowList[i],2)
            snowList[i][1]+=4
            if snowList[i][1]>810:
                y=randint(-50,-10)
                snowList[i][1]=y
                x=randint(0,1215)
                snowList[i][0]=x

        #calls game functions
        if levelNum<9:
            gamefunction(levelslist[levelNum])

        #frame delay
        frameDelay-=1
        respawnDelay-=0.2
        if frameDelay==0:                     
            frameDelay=8
            frame+=1
            if frame==4:
                frame=0
        
        deathText=snowFont.render(str(deathCounter),True,WHITE) #death counter text
        screen.blit(deathText,(1075,25)) #blits death counter
        
    elif page=='story':
        mx,my=mouse.get_pos() #mouse position
        mb=mouse.get_pressed() #if mouse is clicked
        screen.fill(WHITE) #fill screen with white
        screen.blit(storyList[storyNum],(0,0)) #blitting the story
        draw.rect(screen, (191,248,255), continueRect) #draws the rectangle for the continue arrow
        draw.rect(screen,BLACK,continueRect,2) #outlines continue arrow
        screen.blit(continuePic,(1080,765)) #blits picture of an arrow

        if continueRect.collidepoint(mx,my):
            draw.rect(screen, (104,239,255), continueRect,2) #draws a rectangle around the arrow if its hovered over
            
        if continueRect.collidepoint(mx,my) and mb[0]==1:
            draw.rect(screen, (7,176,255), continueRect,2) #draws a rectangle around the arrow if its clicked
            page='game' #changes page to game

        #snow
        for i in range(len(snowList)):
            draw.circle(screen,WHITE,snowList[i],2)
            snowList[i][1]+=4
            if snowList[i][1]>810:
                y=randint(-50,-10)
                snowList[i][1]=y
                x=randint(0,1215)
                snowList[i][0]=x
                
        display.flip()
        
    elif page=='end':
        congrats=image.load("images/xCongrats.png")

        #blitting all the penguins and fireworks
        screen.blit(background,(0,0))
        screen.blit(congrats,(375,100))
        screen.blit(red[frame],(100,100))
        screen.blit(xred[frame],(850,225))
        screen.blit(green[frame],(550,300))
        screen.blit(blue[frame],(1000,100))
        screen.blit(xblue[frame],(250,225))
        screen.blit(xgreen[frame],(350,50))
        screen.blit(ygreen[frame],(750,50))
        screen.blit(eating[frame],(590,705))
        screen.blit(red1right[frame],(14,704))
        screen.blit(orange1right[frame],(154,704))
        screen.blit(yellow1right[frame],(294,704))
        screen.blit(green1right[frame],(434,704))
        screen.blit(blue1left[frame],( 736,704))
        screen.blit(indigo1left[frame],(876,704))
        screen.blit(violet1left[frame],(1016,704))
        screen.blit(rainbow1left[frame],(1156,704))

        #snow
        for i in range(len(snowList)):
            draw.circle(screen,WHITE,snowList[i],2)
            snowList[i][1]+=4
            if snowList[i][1]>810:
                y=randint(-50,-10)
                snowList[i][1]=y
                x=randint(0,1215)
                snowList[i][0]=x

        #frame delay
        frameDelay-=1                         
        if frameDelay==0:                     
            frameDelay=3
            frame+=1
            if frame==4:
                frame=0

        display.flip()
    
    myClock.tick(60) #caps frames at 60
    display.flip()
    
quit()
