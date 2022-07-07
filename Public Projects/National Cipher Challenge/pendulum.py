import pygame
import math
pygame.init()
display_width=600
display_height=600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
length=200
angleDeg=170
angle=angleDeg/180*math.pi
g=.0981
angularAcceleration=0
angularVelocity=0
pivotx=0.5*display_width
pivoty=0.5*display_height
mass=1
energy=0.5*mass*angularVelocity**2*length**2+mass*g*length*math.cos(angle)

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pendulum")
clock=pygame.time.Clock()

velocity=0
run=True
while run:
    gameDisplay.fill(white)
    x=round(pivotx+length*math.sin(angle))
    y=round(pivoty+length*math.cos(angle))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
    pygame.draw.line(gameDisplay,red,(pivotx,pivoty),(x,y),3)
    pygame.draw.circle(gameDisplay,red,(x,y),20) 
    angularAcceleration=-g*math.sin(angle)/length
    angularVelocity+=angularAcceleration
    angle+=angularVelocity
    pygame.display.update()
    clock.tick(120)

pygame.quit()
quit()