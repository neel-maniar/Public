import pygame
import bz2
import os
import shutil
import requests
from bisect import bisect
import imageio.v2 as iio
from timeit import default_timer as timer
start = timer()

## Variables
speed=0.001 # the higher the number, the slower it is
flashDuration=100 # the higher the number, the slower it is
plating=1
culture=3
div=4

## Import Data from URL
URL = f"https://neurodatasharing.bme.gatech.edu/development-data/simple-text/daily/spont/dense/{plating}-{culture}-{div}.spk.txt.bz2"
response = requests.get(URL)
dirname = os.path.dirname(__file__)
path = dirname+"\\testbz2"
newPath = path.replace(os.sep, '/') # Replaces / with \ so it can be read with Python
open(newPath, "wb").write(response.content)

## Process data by reading it off as a string and converting to list
bz_file = bz2.BZ2File(newPath)
data = bz_file.read().decode('ascii')

dataList = [[float(line.split()[0]),int(line.split()[1])] for line in data.splitlines()] # Puts the data into a nice list
timeList=[i[0] for i in dataList]
numberList=[i[1] for i in dataList]
frequency=[[] for i in range(60)]
for i in dataList:
    frequency[i[1]].append(i[0])
## Quick checks on data
if timeList==sorted(timeList):
    print("The times are in ascending order")
if max(numberList)<=60 and min(numberList)>=1:
    print("All integers are between 1 and 60")

## PyGame stuff
pygame.init()
display_width=608 # Can tweak according to your screen size
display=pygame.display.set_mode((display_width,display_width))
pygame.display.set_caption("Time Series Visualisation")

## Variables
squareWidth=display_width//8  
edgeThickness=1 # Grid thickness

## Constants
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
width=8

## Grid mapping (electrode number to coordinates)
def numToCoord(num):
    rows=[6, 7, 5, 4, 7, 6, 7, 5, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 2, 0, 1, 0, 3, 2, 0, 1, 1, 0, 2, 3, 0, 1, 0, 2, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 5, 7, 6, 7, 4, 5, 7, 6, 0, 0, 7, 7, -1]
    cols=[3, 3, 3, 3, 2, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 1, 2, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 5, 6, 7, 6, 7, 5, 6, 7, 7, 6, 5, 7, 6, 7, 6, 5, 6, 5, 5, 4, 4, 4, 4, 0, 7, 0, 7, -1]
    return([rows[ num ],cols[ num ]])

## Draw grid
display.fill(white)
for i in range(width):
        for j in range(width):
            pygame.draw.rect(display, black,(squareWidth*i,squareWidth*j,squareWidth,squareWidth),edgeThickness)
for i in range(0,8,7):
    for j in range(0,8,7):
        pygame.draw.rect(display,black,(squareWidth*i+0.5*edgeThickness+1,squareWidth*j+0.5*edgeThickness+1,squareWidth-edgeThickness-1,squareWidth-edgeThickness-1))
pygame.display.update()

## Matrix representing the screen
onOffMatrix = [[0 for i in range(width)] for j in range(width)]

## Fading Colour
def fadingColour(t):
    colour=red
    fadedColour=[0,0,0]
    for i in range(0,3):
        fadedColour[i]=(colour[i]+(255-colour[i])*(t))
    fadedColour=[round(num) for num in fadedColour]
    return(tuple(fadedColour))

## Flash the colour on the screen
def flash(num,t):
    [i,j]=numToCoord(num)
    if 0<=t<=1:
        pygame.draw.rect(display,fadingColour(t),(squareWidth*j+0.5*edgeThickness+1,squareWidth*i+0.5*edgeThickness+1,squareWidth-edgeThickness-1,squareWidth-edgeThickness-1))
    if 1<t:
        pygame.draw.rect(display,white,(squareWidth*j+0.5*edgeThickness+1,squareWidth*i+0.5*edgeThickness+1,squareWidth-edgeThickness-1,squareWidth-edgeThickness-1))

## Create a folder called "images"
ipath=dirname+"\\images"
try: 
    os.mkdir(ipath) 
except OSError as error: 
    pass
folder = ipath.replace(os.sep, '/')

## Create a folder called "video"
vpath=(dirname+"/video").replace(os.sep, '/')
try: 
    os.mkdir(vpath) 
except OSError as error: 
    pass

## Main Loop
run=True
frameCount=0
flag=False
while run:
    ## Handle quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    currentTime=pygame.time.get_ticks()
    numFlashes=0
    ## Iterate through the list of times to see whether they should be flashed or not.
    for i,value in enumerate(frequency):
        scaledList=[i/speed for i in value]
        index=bisect(scaledList,currentTime)-1
        numFlashes+=index+1
        if len(value)>0 and 0<=index<len(value):
            timeOfActivation=scaledList[index]
            t=(currentTime-timeOfActivation)/flashDuration #Time since it flashed
            print(currentTime,timeOfActivation)
            if 0<=t<=2:
                flash(i,t)
    pygame.image.save(display,folder+"/image"+str(frameCount)+".jpeg") # save each frame as a jpeg
    pygame.display.update()
    frameCount+=1

## Convert images in the images folder to an mp4 video
vnewPath = (vpath+"\movie.mp4").replace(os.sep, '/')
number_files = len(os.listdir(folder))
with iio.get_writer(vnewPath, mode='I') as writer:
    for i in range(number_files):
        image = iio.imread(folder+"/image"+str(i)+".jpeg")
        writer.append_data(image)

## Delete images in images folder when done.
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


end = timer()
print("Time elapsed in program:",end - start)
print("Number of flashes rendered:",numFlashes)
print("Number of flashes on the day:", len(numberList))