import pygame
import copy
import numpy as np
import math

## PyGame stuff
n=7
pygame.init()
display_width=800 # Can tweak according to your screen size
display=pygame.display.set_mode((display_width,display_width))
pygame.display.set_caption("HilbertCurve")
squareWidth=display_width//(2**n)

InitialCurve=np.array([[-1,-1],[-1,1],[1,1],[1,-1]])

def rotateRight(listOfVecs):
    rotationMatrix=np.array(((0, 1),(-1, 0)))
    return(np.flip(np.transpose(np.matmul(rotationMatrix,np.transpose(listOfVecs))),axis=0))
    
def rotateLeft(listOfVecs):
    rotationMatrix=np.array(((0, -1),(1, 0)))
    return(np.flip(np.transpose(np.matmul(rotationMatrix,np.transpose(listOfVecs))),axis=0))

## Recurse

def Hilbert(listOfVecs):
    l=len(listOfVecs)
    g=int(l**0.5)

    translateLeftUp=(np.array([[-1,1]]*l))
    translateLeftDown=(np.array([[-1,-1]]*l))
    translateRightUp=(np.array([[1,1]]*l))
    translateRightDown=(np.array([[1,-1]]*l))
    temp=listOfVecs
    return(np.concatenate((rotateRight(temp)+translateLeftDown*g,temp+translateLeftUp*g,temp+translateRightUp*g,rotateLeft(temp)+translateRightDown*g)))

ScaledInitialCurve=InitialCurve
for i in range(n-2):
    ScaledInitialCurve=(Hilbert(ScaledInitialCurve))
ScaledInitialCurve=ScaledInitialCurve*squareWidth

## Constants


## Convert to pygame coordinates
def to_pygame(coords):
    return np.array([display_width//2,display_width//2])-(-coords[0],coords[1])

## Main Loop
t=0
size=4**(n-1)-1
run=True
blue = (0, 0, 255)
red = (255,0,0)

funs = [
    lambda x : x,
    lambda x : 1-x,
    lambda x : x**2,
    lambda x : min(1,2*x),
    lambda x : 4*x - (4*x)//1,
]

funs = [lambda x,f1=f1,f2=f2 : f1(f2(x)) for f1 in funs for f2 in funs]

funs2= []
for i in range(10):
    funs2.append(lambda x,j=i : print(j))

for fun in funs2:
    fun(0)

from random import choice
fr,fb,fg = choice(funs),choice(funs),choice(funs)

def interpolate(c,c2,t):
    return (int(fr(t)*255),int(fg(t)*255),int(fb(t)*255))

'''
def interpolate(colour1,colour2,t):
    colour=(
        (
            min(255,math.floor(t*colour1[0]+(1-t)*colour2[0])),
            math.floor(t*colour1[1]+(1-t)*colour2[1]),
            max(0,math.floor(t*colour1[2]+(1-t)*colour2[2]))
            )
        )
    return colour
'''


for i in range(size):
    t+=1
    print(interpolate(red,blue,t/size))
    pygame.draw.line(display, interpolate(red,blue,t/size), to_pygame(ScaledInitialCurve[i]),to_pygame(ScaledInitialCurve[i+1])) 
pygame.display.update()
while run:
    ## Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    