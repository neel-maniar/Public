import pygame
import random

pygame.init()

winw=1200
winh=700

win=pygame.display.set_mode((winw,winh))

pygame.display.set_caption("Snake Game")

x=0
y=50
width = 50
randx=0
randy=0
move=0
length = 1
oldlength=1
framecount=0
framecolour=0
decreasing = True
stripy = False
gradient = True
memory=[]
rectList=[[x,y]]

def text_objects(text,font):
    textsurface = font.render(text,True,(framecount,255,255))
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",100)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((winw/2),(winh/2))
    win.blit(textsurf,textrect)
    pygame.display.update()

def check(inpx,inpy):
    global move
    if move==-1:
        inpx-=width
        if inpx<0:
            inpx=winw-width
    if move==1 :
        inpx+=width
        if inpx==winw:
            inpx=0
    if move==-10:
        inpy-=width
        if inpy<0:
            inpy=winh-width
    if move==10:
        inpy+=width
        if inpy==winh:
            inpy=0
    if len(rectList)==1:
        return True
    if [inpx,inpy]!=rectList[1]:
        return True
    else:
        return False

run=True
while run:
    pygame.time.delay(0)

    oldlength=length

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        move=-1
    if keys[pygame.K_RIGHT]:
        move=1
    if keys[pygame.K_UP]:
        move=-10
    if keys[pygame.K_DOWN]:
        move=10   
    
    if framecount==20:
        if x==randx*width and y==randy*width:  
            while [randx*width,randy*width] in rectList: 
                randx=random.randint(0,(winw-width)//width)
                randy=random.randint(0,(winh-width)//width)
            length+=1

        if check(x,y)==True:
            if move==-1:
                x-=width
                if x<0:
                    x=winw-width
            if move==1 :
                x+=width
                if x==winw:
                    x=0
            if move==-10:
                y-=width
                if y<0:
                    y=winh-width
            if move==10:
                y+=width
                if y==winh:
                    y=0
            oldmove=move
        else:
            if oldmove==-1:
                x-=width
                if x<0:
                    x=winw-width
            if oldmove==1 :
                x+=width
                if x==winw:
                    x=0
            if oldmove==-10:
                y-=width
                if y<0:
                    y=winh-width
            if oldmove==10:
                y+=width
                if y==winh:
                    y=0
        rectList.insert(0,[x,y])
        if length==oldlength:
            del rectList[-1]

        if [x,y] in rectList[1:]:
            mytext="Length: " + str(length)
            message_display(mytext)
            pygame.time.delay(2000)
            run=False

        print(move)
        print(rectList)
        print()
        framecount=0

    if run==True:
        win.fill(0)
        pygame.draw.rect(win, (255-framecolour,framecolour,255-framecolour), (randx*width,randy*width,width,width))   
        if stripy==True:
            for i in range(1,length,2):
                pygame.draw.rect(win, (0.1345*framecolour,0.6*(255-framecolour),0.542*framecolour), (rectList[i][0],rectList[i][1],width,width))
            for i in range(0,length,2):
                pygame.draw.rect(win, (255-(0.1345*framecolour),0.6*(framecolour),255-(0.542*framecolour)), (rectList[i][0],rectList[i][1],width,width))
        if gradient==True:
            for i in range(0,length):
                pygame.draw.rect(win, (255-(255/length)*i,0,0), (rectList[i][0],rectList[i][1],width,width))
        pygame.display.update()
        if framecolour>=255:
            decreasing=True
        if framecolour<=0:
            decreasing=False
        if decreasing==True:
            framecolour=framecolour-0.1
        if decreasing==False:
            framecolour=framecolour+0.1
        
        framecount+=1


pygame.quit()
quit()