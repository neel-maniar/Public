import random
import pygame
import numpy as np

## Snakes and Ladders logic
numPlayers=2
players=[0 for i in range(numPlayers)]
playerColour=[]
for i in range(numPlayers):
    playerColour.append(list(np.random.choice(range(256), size=3)))
snakesNladders=[[99,-80],[81,-10],[53,-5],[2,2],[13,10],[54,20],[24,12],[45,-13]]


## PyGame stuff
pygame.init()
display_width=500 # Can tweak according to your screen size
display_height=display_width
display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snakes N Ladders")

## Colours
brown=(146,108,77)
green=(94,157,52)
red=(215,0,0)
lightGreen=(124,187,82)
lightRed=(245,30,30)

## Variables (these are things you can tweak!)
squareWidth=display_width/10
edgeThickness=1 # Grid thickness
gridColour=(0,0,0)  # This is the colour of the lines and filled in boxes
backgroundColour=brown
snakeColour=red
ladderColour=green
snakeEndColour=lightRed
ladderEndColour=lightGreen
buttonWidth=50  # Size of buttons

## Round up
def roundUp(a,b):
    if a%b==0:
        return int(a/b)
    else:
        return int(a//b+1)

## How many squares?
width=roundUp(display_width,squareWidth)
height=roundUp(display_height,squareWidth)

## Number to grid
def numberToGrid(n):
    i=n//10
    if i%2==0:
        j=n%10
    else:
        j=9-n%10
    return[i,j]

## Grid to Number
def gridToNumber(coord):
    i=coord[0]
    j=coord[1]
    if i%2==0:
        return 10*i+j
    else:
        return 10*i+9-j


## coords to gridCoords
def coordsToGridCoords(coords):
    i,j=coords
    return (int(squareWidth*(j+0.5)),int(squareWidth*((9-i)+0.5)))

## Draw Circle at specified coordinates
def drawCircle(number,colour):
    pygame.draw.circle(display,playerColour[colour],coordsToGridCoords(numberToGrid(number)),int(squareWidth/2-edgeThickness))

def startEndCoords(thing):
    # start squares for snakes and ladders
    gridNumberStart=numberToGrid(thing[0]-1)
    i=9-gridNumberStart[0]
    j=gridNumberStart[1]
    # end squares for snakes and ladders
    gridNumberEnd=numberToGrid(thing[0]+thing[1]-1)
    k=9-gridNumberEnd[0]
    l=gridNumberEnd[1]
    if thing[1]>0:
        snakeOrLadderColour=ladderColour
        snakeOrLadderEndColour=ladderEndColour
    else:
        snakeOrLadderColour=snakeColour
        snakeOrLadderEndColour=snakeEndColour
    return(i,j,k,l,snakeOrLadderColour,snakeOrLadderEndColour)

## Draw grid
def drawGrid():
    display.fill(backgroundColour)
    for i in range(width):
        for j in range(height):
            pygame.draw.rect(display, gridColour,(squareWidth*i,squareWidth*j,squareWidth,squareWidth),edgeThickness)


    for thing in snakesNladders:
        i,j,k,l,snakeOrLadderColour,snakeOrLadderEndColour=startEndCoords(thing)
        pygame.draw.rect(display,snakeOrLadderColour,(squareWidth*j+0.5*edgeThickness+1,squareWidth*i+0.5*edgeThickness+1,squareWidth-edgeThickness-1,squareWidth-edgeThickness-1))
        pygame.draw.rect(display,snakeOrLadderEndColour,(squareWidth*l+0.5*edgeThickness+1,squareWidth*k+0.5*edgeThickness+1,squareWidth-edgeThickness-1,squareWidth-edgeThickness-1))

    for thing in snakesNladders: 
        i,j,k,l,snakeOrLadderColour,snakeOrLadderEndColour=startEndCoords(thing)
        pygame.draw.line(display,snakeOrLadderColour,(squareWidth*(j+0.5)+0.5*edgeThickness+1,squareWidth*(i+0.5)+0.5*edgeThickness+1),(squareWidth*(l+0.5)+0.5*edgeThickness+1,squareWidth*(k+0.5)+0.5*edgeThickness+1),5)

pygame.display.update()

## Main loop
drawGrid()
run=True
spaceFlag=False
i=0
while run:
    ## Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice =random.randint(1,6)
                players[i]+=dice
                print("Player",i+1,"rolled a",dice,"and is now on square",players[i])
                for j in snakesNladders:
                    
                    
                    if players[i]==j[0]:
                        drawGrid()
                        for k in range(i+1,numPlayers):
                            drawCircle(players[k]-1,k)
                        for k in range(0,i+1):
                            drawCircle(players[k]-1,k)
                        pygame.display.update()
                        
                        players[i]+=j[1]
                        if j[1]<0:
                            print("Player",i+1,"landed on a snake square! They move down to square",players[i])
                        else:
                            print("Player",i+1,"landed on a ladder square! They move up to square",players[i])
                        
                        pygame.time.delay(200)
                        
                drawGrid()
                for k in range(i+1,numPlayers):
                    drawCircle(players[k]-1,k)
                for k in range(0,i+1):
                    drawCircle(players[k]-1,k)
                if max(players)>=100:
                    print("Good Game. Player",i+1,"won")
                    run = False
                i=(i+1)%numPlayers

    pygame.display.update() 