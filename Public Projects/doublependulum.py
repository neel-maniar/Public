import pygame
import math
pygame.init()
display_width=800
display_height=600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green=(0,255,0)
length_1=200
length_2=200
angleDeg=90
angleDeg_2=90
angle_1=angleDeg/180*math.pi
angle_2=angleDeg_2/180*math.pi
g=.981
angularAcceleration_1=0
angularVelocity_1=0
angularAcceleration_2=0
angularVelocity_2=0
pivotx=0.5*display_width
pivoty=0.5*display_height-200
m_1=2
m_2=1

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Double Pendulum")
clock=pygame.time.Clock()

velocity=0
run=True
while run:
    gameDisplay.fill(white)
    x=round(pivotx+length_1*math.sin(angle_1))
    y=round(pivoty+length_1*math.cos(angle_1))
    x_2=round(pivotx+length_1*math.sin(angle_1)+length_2*math.sin(angle_2))
    y_2=round(pivoty+length_1*math.cos(angle_1)+length_2*math.cos(angle_2))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
    pygame.draw.line(gameDisplay,red,(pivotx,pivoty),(x,y),3)
    pygame.draw.line(gameDisplay,red,(x,y),(x_2,y_2),3)
    pygame.draw.circle(gameDisplay,red,(x,y),20)
    pygame.draw.circle(gameDisplay,red,(x_2,y_2),20) 
    numerator_1=-g*(2*m_1+m_2)*math.sin(angle_1)-m_2*g*math.sin(angle_1-2*angle_2)-2*math.sin(angle_1-angle_2)*m_2*(angularVelocity_2**2*length_2+angularVelocity_1**2*length_1*math.cos(angle_1-angle_2))
    angularAcceleration_1=(numerator_1)/(length_1*(2*m_1+m_2-m_2*math.cos(2*angle_1-2*angle_2)))
    angularAcceleration_2=(2*math.sin(angle_1-angle_2)*(angularVelocity_1**2*length_1*(m_1+m_2)+g*(m_1+m_2)*math.cos(angle_1)+angularVelocity_2**2*length_2*m_2*math.cos(angle_1-angle_2)))/(length_2*(2*m_1+m_2-m_2*math.cos(2*angle_1-2*angle_2)))
    angularVelocity_2+=angularAcceleration_2
    angle_2+=angularVelocity_2
    angularVelocity_1+=angularAcceleration_1
    angle_1+=angularVelocity_1
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()