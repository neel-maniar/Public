import pygame
import math
import operator as op
from functools import reduce

## PyGame stuff
pygame.init()
display_width=700
display_height=700
display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Multibrot")
clock=pygame.time.Clock()

## Constant colours
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)

#Glowing blue colouring is 1, grey colourscheme is 2. 2 is better imho
colourScheme=1

## Variables (you can tweak these)
numIterate=100 #resolution!
xAxisLeft=-1.5
xAxisRight=1.5
power=2
bound=5
# Set xAxisLeft to -1.79 and xAxisRight to -1.74 and numIterate to 100 to see a smaller MandelBrot set! (It is indeed a fractal!)

## Scale the grid
def to_coordinates(x):
    # Move the origin to the centre of the screen    
    a=[x[0]-0.5*display_width,0.5*display_height-x[1]]
    # Scale the coordinates up
    xAxisSize=xAxisRight-xAxisLeft
    scaleFactor=(xAxisSize)/display_width
    a=[a[0]*scaleFactor,a[1]*scaleFactor]
    # Shift the x axis
    a=[a[0]+(xAxisRight-0.5*xAxisSize),a[1]]
    return a

## Complex number powers
def add(a,b):
    return([a[0]+b[0],a[1]+b[1]])

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def complexPower(complexNumber,power):
    x=complexNumber[0]
    y=complexNumber[1]
    real=0
    imaginary=0
    for i in range(power+1):
        if i%4==0:
            real+=ncr(power,i)*x**(power-i)*y**i
        if i%4==1:
            imaginary+=ncr(power,i)*x**(power-i)*y**i
        if i%4==2:
            real+=-ncr(power,i)*x**(power-i)*y**i
        if i%4==3:
            imaginary+=-ncr(power,i)*x**(power-i)*y**i
    return [real,imaginary]

def sqrdistance(a):
    return(a[0]**2+a[1]**2)

## Iterative function
def f(x,c):
    return(add(complexPower(x,power),c))

## Does it converge? If not, how long does it take to diverge?
def divergeTime(c):
    x=[0,0]
    for i in range(0,numIterate):
        x=f(x,c)
        if sqrdistance(x)>bound:
            return(i)
    return(-1)

## Display the fractal
display.fill(white)
for i in range(0,display_width):
    for j in range(0,display_height//2+1):

        # Colour the convergent pixels black
        if divergeTime(to_coordinates([i,j]))==-1:
            pygame.draw.rect(display,black,(i,j,1,1))
            pygame.draw.rect(display,black,(i,display_height-j,1,1))

        # Colour divergent pixels based on how quickly they diverge
        else:
            if 40<=255-5*(divergeTime(to_coordinates([i,j])))<256:
                colouring=round(255-4*(divergeTime(to_coordinates([i,j]))))
            else:
                colouring=40
            # Select colourscheme
            if colourScheme==1:
                drawColour=(255-colouring,255-colouring,255-0.5*colouring)
            elif colourScheme==2:
                drawColour=(colouring,colouring,colouring)
            pygame.draw.rect(display,drawColour,(i,j,1,1))
            pygame.draw.rect(display,drawColour,(i,display_height-j,1,1))
pygame.display.update()

## Main loop (to handle quitting the program)
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    clock.tick(10)

pygame.quit()
quit()