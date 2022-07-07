import pygame
import math
import time
import os

## Constants
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGREEN = (0,125,0)
DARKBLUE =(21,76,121) 
BLUE = (33,150,193)
RED = (255,0,0)
FPS = 30

## Variables
speed=10
ratio=2
ratioList=[2,3,3.4,3.6,3.8,3.9]
#ratioList=[2,3]
mouse_colour=GREEN
cat_colour=RED
buttonWidth=50
guidelineFlag= False
buttonPressedFlag = False
deathCounter = 0
hitboxFlag=False

## PyGame stuff
pygame.init()
display_width=1000 # Can tweak according to your screen size
display_height=600
display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Cat and Mouse")
clock=pygame.time.Clock()
font1 = pygame.font.SysFont("monotypecorsiva",27)
font2 = pygame.font.SysFont("garamond",60)
img1=font1.render("The cat is currently "+str(ratio)+" times faster than the mouse",True,BLACK)
img2=font2.render("Level 1",True,BLACK)

## Assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
mouse_img = pygame.image.load(os.path.join(img_folder, 'mouse.png')).convert_alpha()
cat_img = pygame.image.load(os.path.join(img_folder, 'cat.png')).convert()
mouse_ratio=2.017
mouse_height=40
mouse_width=round(mouse_height*mouse_ratio)
mouse_img_rescaled = pygame.transform.scale(mouse_img,(mouse_width,mouse_height))
cat_ratio=2.418
cat_height=50
cat_width=round(cat_height*cat_ratio)
cat_img_rescaled =  pygame.transform.scale(cat_img,(cat_width,cat_height))

# Convenient to label the radius
radius = min(display_height,display_width)//2-100

def magnitude(vector):
    return( (vector[0]**2+vector[1]**2)**0.5 )

def angle(vector):
    if vector[0]==0:
        if vector[1]>0:
            return(math.pi/2)
        if vector[1]<0:
            return(-math.pi/2)
        else:
            return(0)
    if vector[0]>0:
        arctan=(math.atan(vector[1]/vector[0]))%(2*math.pi)
        return(arctan)
    if vector[0]<0:
        arctan=(math.atan(vector[1]/vector[0]))%(2*math.pi)
        return( (arctan+math.pi)%(2*math.pi) )

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mouse_img_rescaled 
        self.rect = self.image.get_rect()
        self.rect.height = 30
        self.rect.center = (display_width/2,display_height/2)
    def update(self):
        mouse_pos=pygame.mouse.get_pos()
        mouse_pressed=pygame.mouse.get_pressed()[0]
        posDiff=[mouse_pos[0]-self.rect.center[0],mouse_pos[1]-self.rect.center[1]]
        if magnitude(posDiff)>speed: #and mouse_pressed==True :
            direction=[ math.floor(speed*posDiff[0]/magnitude(posDiff)),math.floor( speed*posDiff[1]/magnitude(posDiff)) ]
            self.rect.x += direction[0]
            self.rect.y += direction[1]
        if 1<magnitude(posDiff)<=speed: #and mouse_pressed==True:
            direction=[math.floor(posDiff[0]),math.floor(posDiff[1])]
            self.rect.x += direction[0]
            self.rect.y += direction[1]
        self.coords=[self.rect.center[0]-display_width/2, self.rect.center[1]-display_height/2]
        self.angle=angle(self.coords)
    def reset(self):
        self.rect.center = (display_width/2,display_height/2)

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cat_img_rescaled
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (display_width/2+radius,display_height/2)
        self.angle=0
        self.angularSpeed=ratio*speed/radius
    def update(self):
        self.angularSpeed=ratio*speed/radius
        angleDiff= (mouse.angle-self.angle)%(2*math.pi)
        if self.angularSpeed<angleDiff <math.pi:
            self.angle+=self.angularSpeed
        if 0<angleDiff<=self.angularSpeed or 2*math.pi-self.angularSpeed<=angleDiff<2*math.pi:
            self.angle+=angleDiff
        if  2*math.pi-self.angularSpeed>angleDiff>math.pi:
            self.angle-=self.angularSpeed
        self.rect.center=( display_width/2+radius*math.cos(self.angle),display_height/2+radius*math.sin(self.angle) )
        self.angle=self.angle%(2*math.pi)

class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((buttonWidth, buttonWidth))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topright=(display_width-10,10)
    def update(self):
        global guidelineFlag
        global buttonPressedFlag
        pygame.draw.circle(display,BLACK,self.rect.center,math.floor(0.3*buttonWidth),1)
        pygame.draw.circle(display,BLACK,self.rect.center,math.floor(0.4*buttonWidth),1)
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and buttonPressedFlag==False:
            if self.rect.collidepoint(x, y):
                if guidelineFlag==False:
                    guidelineFlag=True
                else:
                    guidelineFlag=False
            buttonPressedFlag=True
        if event.type == pygame.MOUSEBUTTONUP and buttonPressedFlag==True:
            buttonPressedFlag=False
        if guidelineFlag==True:
            pygame.draw.circle(display,BLACK,(display_width//2,display_height//2),round(radius/ratio),1)
            if (radius-(math.pi*radius/ratio)) > 0:
                pygame.draw.circle(display,BLACK,(display_width//2,display_height//2),round(radius-(math.pi*radius/ratio)),1)
            pygame.draw.rect(display,BLACK,(mouse.rect.center[0]-3,mouse.rect.center[1]-3,6,6))
            pygame.draw.rect(display,BLACK,(cat.rect.center[0]-3,cat.rect.center[1]-3,6,6))
        
def win_condition(mouseCoords,catAngle):
    angleDiff=(catAngle-angle(mouseCoords))%(2*math.pi)
    if magnitude(mouseCoords)>=radius:
        if 0<=angleDiff<cat.angularSpeed or 2*math.pi-cat.angularSpeed<angleDiff<=2*math.pi:
            return(-1)
        else:
            return(1)
    else:
        return(0)

all_sprites = pygame.sprite.Group()
mouse = Mouse()
cat=Cat()
button=Button()
all_sprites.add(mouse,cat,button)
min(display_height,display_width)//2-10
deathImage = font1.render("Deaths:"+str(deathCounter),True,BLACK)
i=1
t0=time.time()
# Game loop
running = True
started = False
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    if started == False:
        display.fill(DARKGREEN)
        img1=font1.render("Can you escape without getting caught? Press anywhere to start.",True,BLACK)
        img1rect=img1.get_rect()
        img1rect.center=(display_width//2,display_height//2+40)
        display.blit(img1,img1rect)
        img2=font2.render("Cat and Mouse Game",True,BLACK)
        img2rect=img2.get_rect()
        img2rect.center=(display_width//2,display_height//2)
        display.blit(img2,img2rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            started = True

    else:
        # Draw / render
        display.fill(DARKGREEN)
        pygame.draw.circle(display,BLUE,(display_width//2,display_height//2),radius)
        pygame.draw.rect(display,BLACK,(display_width//2-1,display_height//2-1,2,2))
    #    if clearButtonStartingPos<=pos[0]<=clearButtonStartingPos+buttonWidth and 10<=pos[1]<=10+buttonWidth:
        all_sprites.draw(display)
        all_sprites.update()
        if win_condition(mouse.coords,cat.angle)==1:
            mouse.reset()
            if i==len(ratioList):
                bigText=font2.render("You win!",True,BLACK)
                timeText=font1.render("Final Time: "+str(timePassed),True,BLACK)
                deathText=font1.render("Deaths: "+str(deathCounter),True,BLACK)
                bigTextrect = bigText.get_rect()
                timeTextrect = timeText.get_rect()
                deathTextrect = deathText.get_rect()
                bigTextrect.center=((display_width//2,display_height//2))
                timeTextrect.center = (display_width//2,display_height//2+50)
                deathTextrect.center = (display_width//2,display_height//2+75)
                display.blit(bigText,bigTextrect)
                display.blit(timeText,timeTextrect)
                display.blit(deathText,deathTextrect)
                pygame.display.flip()
                pygame.time.delay(5000)
                break
            else:
                display.fill(DARKGREEN)
                img2=font2.render("Level "+str(i+1),True,BLACK)
                img2rect=img2.get_rect()
                img2rect.center=(display_width//2,display_height//2)
                display.blit(img2,img2rect)
                pygame.display.flip()
                pygame.time.delay(1000)
                ratio=ratioList[i]
                img1=font1.render("The cat is now "+str(ratioList[i])+" times faster than the mouse",True,BLACK)
                img2=font2.render("Level "+str(i+1),True,BLACK)
                i+=1
        elif win_condition(mouse.coords,cat.angle)==-1:
            mouse.reset()
            deathCounter+=1
            deathImage = font1.render("Deaths:"+str(deathCounter),True,BLACK)
        timePassed=round(time.time()-t0,2)
        timeImage=font1.render("Time: "+str(timePassed),True,BLACK)
        display.blit(img1, (20, 65))
        display.blit(img2, (20, 10))
        display.blit(deathImage,(display_width-buttonWidth-150,15))
        display.blit(timeImage,(display_width-buttonWidth-300,15))
    #    drawButton()
        # *after* drawing everything, flip the display
    pygame.display.flip()
pygame.quit()