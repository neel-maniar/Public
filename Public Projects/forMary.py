import pygame
import math
import numpy as np

## User Variables
# Colours
backgroundColour=(255,255,255) # White

# Display dimensions
display_height=600 # Can tweak according to your screen size
display_width=display_height*2

# test commit

# Number of "nodes"
height=150 # 150
width=height*2
squareWidth=math.ceil(display_height/height)

# S (currently just random)
S=np.random.random_integers(1, 1000, (height,width))
print(S)

## PyGame stuff
pygame.init()
display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slime Visualisation")

## Ind2Sub (can't think of a neater way of doing this unfortunately)
def ind2sub(sz,ind):
    height=sz[0]
    width=sz[1]
    if ind>height*width:
        return "error, index too high"
    if ind%height==0:
        r=height
    else:
        r=ind%height
    c=math.ceil(ind/height)
    return [r,c]

def colour(i,j):
    cl=math.floor(255-S[i][j]/1000*255)
    return((cl,cl,cl))

## Populate display with squares
display.fill(backgroundColour)
for i in range(height):
        for j in range(width):
            pygame.draw.rect(display, colour(i,j),(squareWidth*j,squareWidth*i,squareWidth,squareWidth))
pygame.display.update()

## Main Loop to keep the page up until you close it
run=True
while run:
    ## Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

