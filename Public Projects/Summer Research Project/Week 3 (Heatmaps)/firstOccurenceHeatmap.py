import os
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns; sns.set_theme()
import sys
sys.path.insert(0, 'C:/Users/Neel/My Python Coding/Public/Public Projects/Summer Research Project')
from commonFunctions import *
np.seterr(divide='ignore', invalid='ignore')

# Measure how long the program takes to run


# Parameters
plating=1
culture=3
divList=[4,13,25]
version=3

for div in divList:
    dataList=np.array(getDataList(plating,culture,div) )
    channelList=dataList[:,1].astype(int)
    for masterChannel in range(60):
        masterIndices=np.array((channelList==masterChannel).nonzero()[0]).T
        totDataList=np.zeros(64).astype(int)
        pointsList=np.zeros(64).astype(int)
        unique, counts = np.unique(channelList, return_counts=True)
        for i,val in enumerate(unique):
            totDataList[val]=counts[i]
        for index in masterIndices:
            if index+1<len(dataList):
                pointsList[int(dataList[index+1][1])]+=1
        propList=(pointsList/totDataList)

        totDataMatrix=np.zeros((8,8)).astype(int)
        propMatrix=np.zeros((8,8))
        for r in range(8):
            for c in range(8):
                propMatrix[r][c]=propList[coordToNum(r,c)]
                totDataMatrix[r][c]=totDataList[coordToNum(r,c)]
        mask=np.zeros_like(propMatrix)
        mask[np.isnan(propMatrix)]=True
        # Plot Heatmap
        fig, ax = plt.subplots()
        start_time = time()
        ax = sns.heatmap(propMatrix,annot=totDataMatrix,fmt='',mask=mask,robust=True)
        print(f"{masterChannel}/59",time()-start_time)
        ax.set_title(f"",wrap=True)
        position=(numToCoord(masterChannel)[1],numToCoord(masterChannel)[0])
        ax.add_patch(Rectangle(position, 1, 1, fill=False, edgecolor='blue', lw=3))
        dirname = os.path.dirname(__file__)
        plt.savefig(f'{dirname}/Heatmaps/Heatmap{version}_{plating}_{culture}_{div}_{masterChannel}.eps', format='eps')
    print(f"Figures produced for div {div}!")
    texMaker(plating,culture,div,version)

print(f"{os.path.basename(__file__)} took ----- {time()-start_time} ----- seconds to run")