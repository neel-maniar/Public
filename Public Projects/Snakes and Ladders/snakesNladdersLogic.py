import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import random

numPlayers=100
players=[0 for i in range(numPlayers)]
snakesNladders=[[99,-80],[81,-10],[53,-5],[2,2],[13,10],[54,20],[24,12],[45,-13]]
frequencyVec=[0 for i in range(100)]

def numberToGrid(n):
    i=n//10
    if i%2==0:
        j=n%10
    else:
        j=9-n%10
    return[i,j]

def vecToGrid(vec):
    frequencyGrid=[[0 for i in range(10)] for i in range(10)]
    for i in range(10):
        for j in range(10):
            k=numberToGrid(10*i+j)[0]
            l=numberToGrid(10*i+j)[1]
            frequencyGrid[9-k][l]=vec[10*i+j]
    return (frequencyGrid)

run=True
while run:
    for i in range(numPlayers):
        dice =random.randint(1,6)
        players[i]+=dice
        if players[i]>100:
            # print("Player", i+1, "won!")
            run=False
            break
        elif players[i]==100:
            # print("Player", i+1, "won!")
            run=False
            frequencyVec[players[i]-1]+=1
            break
        else:
            frequencyVec[players[i]-1]+=1
        for j in snakesNladders:
            if players[i]==j[0]:                
                players[i]+=j[1]
                frequencyVec[players[i]-1]+=1
                # if j[1]<0:
                #     print("Player",i+1,"landed on a snake square! They move down to square",players[i])
                # else:
                #     print("Player",i+1,"landed on a ladder square! They move up to square",players[i])
        
frequencyGrid=vecToGrid(frequencyVec)
ax = sns.heatmap(frequencyGrid, linewidth=0.5)
plt.show()