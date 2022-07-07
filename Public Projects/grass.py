import pygame
from random import random
import time
import matplotlib.pyplot as plt

## PyGame stuff
pygame.init()
display_width=1500 # Can tweak according to your screen size
display_height=1000
display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Minecraft Grass")

## Colours
brown=(146,108,77)
green=(94,157,52)

## Variables (these are things you can tweak!)
squareWidth=5
colour=(0,0,0)  # This is the colour of the lines and filled in boxes
backgroundColour=brown
colour=green
buttonWidth=50  # Size of buttons
p=0.005

## Round up
def roundUp(a,b):
    if a%b==0:
        return int(a/b)
    else:
        return int(a//b+1)

## How many squares?
width=roundUp(display_width,squareWidth)
height=roundUp(display_height,squareWidth)


## Matrix representing the screen
middleHeight=roundUp(height-1,2)
middleWidth=roundUp(width-1,2)
print(middleHeight)
print(middleWidth)
onOffMatrix = [[0 for i in range(width)] for j in range(height)]
onOffMatrix[roundUp(height-1,2)][roundUp(width-1,2)]=1

## Updates the matrix according to the rules
def nextStep(gameState):
    changes = [[0 for i in range(width)] for j in range(height)]
    gameWidth=len(gameState[0])
    gameHeight=len(gameState)
    for i in range(0,gameHeight):
        for j in range(0,gameWidth):
            if gameState[i][j]==1:
                for k in range(-5,6):
                    for l in range(-5,6):
                        if i+l<gameHeight and j+k<gameWidth and i+l>=0 and j+k>=0:
                            r=random()
                            if r<=p and gameState[i+l][j+k]==0:
                                changes[i+l][j+k]=1
                                gameState[i+l][j+k]=1
    # print("gameState: ",str(gameState),end="")
    # print("changes: ",changes)
    return (gameState, changes)

numChanges=[]
## Display matrix
def displayMatrix(changes):
    changesCount=0
    for i in range(height):
            for j in range(width):
                if changes[i][j]==1:
                    pygame.draw.rect(display,colour,(squareWidth*j,squareWidth*i,squareWidth,squareWidth))
                    changesCount+=1
    numChanges.append(changesCount)

## Main Loop

display.fill(brown)
pygame.draw.rect(display,colour,(squareWidth*middleWidth,squareWidth*middleHeight,squareWidth,squareWidth))
run=True
frameCount=0
timeOld=time.perf_counter()
timeLapse=[]
while run:
    ## Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ## Update
    onOffMatrix,changes=nextStep(onOffMatrix)
    displayMatrix(changes)

    pygame.display.update()
    pygame.time.delay(10)
    frameCount+=1

    timeNew=time.perf_counter()
    timeLapse.append(timeNew-timeOld)
    timeOld=timeNew

plt.plot(numChanges, timeLapse, 'ro')
plt.xlabel("number of changes in this update")
plt.ylabel("time taken to update")
plt.show()