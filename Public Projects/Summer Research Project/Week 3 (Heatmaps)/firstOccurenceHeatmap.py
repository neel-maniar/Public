import os
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import sys
sys.path.insert(0, 'C:/Users/Neel/My Python Coding/Public/Public Projects/Summer Research Project')
from commonFunctions import *

# Measure how long the program takes to run
start_time = time()


# Parameters
plating=3
culture=4
divList=[20]
version=3

for div in divList:
    dataList=np.array(getDataList(plating,culture,div) )
    dataList=np.array([[1,1],[2,2],[3,3],[4,1],[5,1]])
    masterChannel=1
    print(f"{masterChannel}/59")
    masterIndices=np.array((dataList[:,1]==masterChannel).nonzero()[0]).T
    totDataList=np.zeros(64)
    pointsList=np.zeros(64)
    unique, counts = np.unique(dataList[:,1], return_counts=True)
    for i,val in enumerate(unique):
        totDataList[val]=counts[i]
    for index in masterIndices:
        if index+1<len(dataList):
            pointsList[dataList[index+1][1]]+=1
    propList=(pointsList/totDataList)

    totDataMatrix=np.zeros((8,8)).astype(int)
    propMatrix=np.zeros((8,8))
    for r in range(8):
        for c in range(8):
            propMatrix[r][c]=propList[coordToNum(r,c)]
            totDataMatrix[r][c]=totDataList[coordToNum(r,c)]
    mask=np.zeros_like(propMatrix)
    mask[np.isnan(propMatrix)]=True
    print(mask)
    # Plot Heatmap
    import seaborn as sns; sns.set_theme()
    ax = sns.heatmap(propMatrix,annot=totDataMatrix,fmt='',mask=mask,robust=True)
    ax.set_title(f"",wrap=True)
    position=(numToCoord(masterChannel)[1],numToCoord(masterChannel)[0])
    ax.add_patch(Rectangle(position, 1, 1, fill=False, edgecolor='blue', lw=3))
    dirname = os.path.dirname(__file__)
    plt.savefig(f'{dirname}/Heatmaps/Heatmap{version}_{plating}_{culture}_{div}_{masterChannel}.eps', format='eps')
print(f"Figures produced for div {div}!")
texMaker(plating,culture,div,version)

print(f"{os.path.basename(__file__)} took ----- {time()-start_time} ----- seconds to run")