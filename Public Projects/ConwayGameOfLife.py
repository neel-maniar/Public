import pygame
import copy

## PyGame stuff
pygame.init()
display_width=1000 # Can tweak according to your screen size
display_height=600
display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("ConwayGameOfLife")
clock=pygame.time.Clock()

## Variables (these are things you can tweak!)
updateTime=100  # For the "play button", how fast do you want it to animate?
squareWidth=50  
edgeThickness=1 # Grid thickness
colour=(0,0,0)  # This is the colour of the lines and filled in boxes
backgroundColour=(255,255,255)
buttonWidth=50  # Size of buttons

## Constants
red=(255,0,0)
green=(0,255,0)
orange=(255,165,0)
white=(255,255,255)
lightBlue=(173,216,230)

## Round up
def roundUp(a,b):
    if a%b==0:
        return int(a/b)
    else:
        return int(a//b+1)

## How many squares?
width=roundUp(display_width,squareWidth)
height=roundUp(display_height,squareWidth)

## Draw grid
display.fill(backgroundColour)
for i in range(width):
        for j in range(height):
            pygame.draw.rect(display, colour,(squareWidth*i,squareWidth*j,squareWidth,squareWidth),edgeThickness)
pygame.display.update()

stopButtonStartingPos=          display_width-(10+buttonWidth)
playButtonStartingPos=          display_width-2*(10+buttonWidth)
forwardButtonStartingPos=       display_width-3*(10+buttonWidth)
backwardButtonStartingPos=      display_width-4*(10+buttonWidth)
clearButtonStartingPos=         display_width-5*(10+buttonWidth)

## Draw buttons
def drawButtons(pause=False):
    unit=buttonWidth//4
    sixthUnit=buttonWidth//6

    # Stop Button
    stopButtonPos=(stopButtonStartingPos,10,buttonWidth,buttonWidth)
    pygame.draw.rect(display,red,stopButtonPos)
    pygame.draw.rect(display,white,(stopButtonPos[0]+unit,stopButtonPos[1]+unit,buttonWidth//2+1,buttonWidth//2+1))
    
    # Play Button
    playButtonPos=(playButtonStartingPos,10,buttonWidth,buttonWidth)
    pygame.draw.rect(display,green,playButtonPos)
    trianglePoints=[[1,1],[3,2],[1,3]]
    triangleCoords=[(playButtonPos[0]+i[0]*unit,playButtonPos[1]+i[1]*unit) for i in trianglePoints]    
    
    # Forward Button
    forwardButtonPos=(forwardButtonStartingPos,10,buttonWidth,buttonWidth)
    pygame.draw.rect(display,orange,forwardButtonPos)
    arrowPoints=[(2,1),(3,2),(2,3),(2,2.5),(1,2.5),(1,1.5),(2,1.5)]
    arrowCoords=[(round(forwardButtonPos[0]+i[0]*unit),round(forwardButtonPos[1]+i[1]*unit)) for i in arrowPoints]
    pygame.draw.polygon(display,white,arrowCoords)

    # Backward Button
    backwardButtonPos=(backwardButtonStartingPos,10,buttonWidth,buttonWidth)
    pygame.draw.rect(display,orange,backwardButtonPos)
    backArrowPoints=[(4-i[0],4-i[1]) for i in arrowPoints]
    backArrowCoords=[(round(backwardButtonPos[0]+i[0]*unit),round(backwardButtonPos[1]+i[1]*unit)) for i in backArrowPoints]
    pygame.draw.polygon(display,white,backArrowCoords)

    # Clear Button
    clearButtonPos=(clearButtonStartingPos,10,buttonWidth,buttonWidth)
    pygame.draw.rect(display,lightBlue,clearButtonPos)
    pygame.draw.circle(display,white,(clearButtonPos[0]+buttonWidth//2,clearButtonPos[1]+buttonWidth//2),buttonWidth//3,buttonWidth//6)

    # Pause Button
    if pause==False:
        pygame.draw.polygon(display,white,triangleCoords)
    if pause==True:
        pygame.draw.rect(display,white,(playButtonPos[0]+unit,playButtonPos[1]+unit,sixthUnit,2*unit))
        pygame.draw.rect(display,white,(playButtonPos[0]+unit+2*sixthUnit,playButtonPos[1]+unit,sixthUnit,2*unit))
    
## Matrix representing the screen
onOffMatrix = [[0 for i in range(width)] for j in range(height)]
originalPosition=onOffMatrix
onOffMatrixCopy=copy.deepcopy(onOffMatrix)
history=[onOffMatrixCopy]

## Updates the matrix according to the rules
def nextStep(gameState):
    gameWidth=len(gameState[0])
    gameHeight=len(gameState)
    newGameState=[[0 for i in range(gameWidth)] for j in range(gameHeight)]
    # Pad with zeroes
    zeroRow=[0 for i in range(gameWidth+2)]
    for i in range(gameHeight):
        gameState[i].insert(0,0)
        gameState[i].append(0)
    gameState.insert(0,zeroRow)
    gameState.append(zeroRow)

    for i in range(1,gameHeight+1):
        for j in range(1,gameWidth+1):
            # Sum of neighbouring cells
            neighbourSum=-gameState[i][j]
            for k in range(-1,2):
                for l in range(-1,2):
                    neighbourSum+=gameState[i+l][j+k]
            # Applying rules
            if gameState[i][j]==1 and (neighbourSum<2 or neighbourSum>3):
                newGameState[i-1][j-1]=0
            elif gameState[i][j]==0 and neighbourSum==3:
                newGameState[i-1][j-1]=1
            else:
                newGameState[i-1][j-1]=gameState[i][j]
    newGameStateCopy=copy.deepcopy(newGameState)
    history.append(newGameStateCopy)
    return newGameState

## Display matrix
def displayMatrix():
    for i in range(height):
            for j in range(width):
                if onOffMatrix[i][j]==1:
                    ColourOrBackground=colour
                else:
                    ColourOrBackground=backgroundColour
                pygame.draw.rect(display,ColourOrBackground,(squareWidth*j+0.5*edgeThickness+1,squareWidth*i+0.5*edgeThickness+1,squareWidth-edgeThickness-1,squareWidth-edgeThickness-1))

## Main Loop
playFlag=False
stopFlag=False
run=True
firstTimePlay=False
forwardFlag=False
backwardFlag=False
clearFlag=False
frameCount=0
while run:
    nextStepFlag=False
    previousStepFlag=False
    ## Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        ## Mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            
            ## Button Clicks
            if stopButtonStartingPos<=pos[0]<=stopButtonStartingPos+buttonWidth and 10<=pos[1]<=10+buttonWidth:
                playFlag=False
                stopFlag=True
            elif playButtonStartingPos<=pos[0]<=playButtonStartingPos+buttonWidth and 10<=pos[1]<=10+buttonWidth:
                if playFlag==False:
                    playFlag=True
                else:
                    playFlag=False
            elif forwardButtonStartingPos<=pos[0]<=forwardButtonStartingPos+buttonWidth and 10<=pos[1]<=10+buttonWidth:
                forwardFlag=True
            elif backwardButtonStartingPos<=pos[0]<=backwardButtonStartingPos+buttonWidth and 10<=pos[1]<=10+buttonWidth:
                backwardFlag=True
            elif clearButtonStartingPos<=pos[0]<=clearButtonStartingPos+buttonWidth and 10<=pos[1]<=10+buttonWidth:
                clearFlag=True
            else:    
                posx=pos[0]//squareWidth
                posy=pos[1]//squareWidth
                onOffMatrix[posy][posx]=1-onOffMatrix[posy][posx]
                if onOffMatrix[posy][posx]==1:
                    ColourOrBackground=colour
                else:
                    ColourOrBackground=backgroundColour
                pygame.draw.rect(display,ColourOrBackground,(squareWidth*posx+0.5*edgeThickness+1,squareWidth*posy+0.5*edgeThickness+1,squareWidth-edgeThickness-1,squareWidth-edgeThickness-1))
                
    ## Autoplay button
    if playFlag==True and frameCount%updateTime==0:
        # Store the first position, before play is pressed for the first time.
        if firstTimePlay==False:
            originalPosition=copy.deepcopy(onOffMatrix)
        firstTimePlay=True
        onOffMatrix=nextStep(onOffMatrix)
        displayMatrix()
    
    ## Stop button
    if stopFlag==True:
        onOffMatrix=copy.deepcopy(originalPosition)
        displayMatrix()
        stopFlag=False
        firstTimePlay=False

    ## Forward Button
    if forwardFlag==True:
        if firstTimePlay==False:
            originalPosition=copy.deepcopy(onOffMatrix)
            history.append(originalPosition)
        firstTimePlay=True
        onOffMatrix=copy.deepcopy(nextStep(onOffMatrix))
        displayMatrix()
        forwardFlag=False
    
    ## Backward Button
    if backwardFlag==True:
        if len(history)>0:
            history.pop()
            onOffMatrix=copy.deepcopy(history[-1])
        displayMatrix()
        backwardFlag=False

    ## Clear Button
    if clearFlag==True:
        onOffMatrix = [[0 for i in range(width)] for j in range(height)]
        displayMatrix()
        originalPosition=onOffMatrix
        onOffMatrixCopy=copy.deepcopy(onOffMatrix)
        history=[onOffMatrixCopy]
        clearFlag=False

    ## Display Buttons
    if playFlag==True:
        drawButtons(True)
    else:
        drawButtons()

    pygame.display.update()
    pygame.time.delay(0)
    frameCount+=1