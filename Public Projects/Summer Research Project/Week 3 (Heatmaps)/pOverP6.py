import os
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns; sns.set_theme()
import sys
from pathlib import Path
dirname = os.path.dirname(__file__)
grandParDir=(str(Path(__file__).parents[1]).replace(os.sep, '/'))
sys.path.insert(0, grandParDir)
from commonFunctions import *
np.seterr(divide='ignore', invalid='ignore')

# Measure how long the program takes to run
start_time=time()

# Parameters
platingList=[1,2,3,6]
cultureList=[3,2,4,1]
divListList=[[4,13,25],[4,19,35],[7,20,31],[4,19,34]]
platingList=[1]
cultureList=[3]
divListList=[[25]]
version=6

for thing in range(len(platingList)):
    plating=platingList[thing]
    culture=cultureList[thing]
    divList=divListList[thing]
    for div in divList:
        dataList=np.array(getDataList(plating,culture,div) )
        sumT=len(dataList)
        channelList=dataList[:,1].astype(int)
        timeChannels=[[index for index,row in enumerate(dataList) if row[1]==channel] for channel in range(64)]
        t=[len(i) for i in timeChannels]
        phat=[i/sumT for i in t]
        for masterChannel in range(23,24):
            masterIndices=np.array((channelList==masterChannel).nonzero()[0]).T
            totDataList=np.zeros(64).astype(int)
            pointsList=np.zeros(64).astype(int)
            unique, counts = np.unique(channelList, return_counts=True)
            for i,val in enumerate(unique):
                totDataList[val]=counts[i]
            unique, counts = np.unique(channelList, return_counts=True)
            for index in masterIndices:
                if index+1<len(dataList):
                    pointsList[int(dataList[index+1][1])]+=1
            ptilde=[i/t[masterChannel] for i in pointsList]

            totDataMatrix=np.zeros((8,8)).astype(int)
            pMatrix=np.zeros((8,8))
            for r in range(8):
                for c in range(8):
                    pMatrix[r][c]=ptilde[coordToNum(r,c)]/phat[coordToNum(r,c)]
                    totDataMatrix[r][c]=totDataList[coordToNum(r,c)]
            pMatrixRounded=(np.around(pMatrix, decimals=3)).astype(str)
            # Plot Heatmap
            fig, ax = plt.subplots()
            ax = sns.heatmap(pMatrix,annot=totDataMatrix,fmt='',robust=True, vmin=0, vmax=2.5)
            ax.set_title(f"Observed/expected probabilities of a channel spiking after {masterChannel} in plating {plating}, culture {culture}, div {div}",wrap=True)
            position=(numToCoord(masterChannel)[1],numToCoord(masterChannel)[0])
            ax.add_patch(Rectangle(position, 1, 1, fill=False, edgecolor='blue', lw=3))
            # plt.savefig(f'{dirname}/Heatmaps/Heatmap{version}_{plating}_{culture}_{div}_{masterChannel}.eps', format='eps')
            plt.show()
            plt.close('all')
        print(f"Figures produced for div {div}!")
        # texMaker(plating,culture,div,version)

print(f"{os.path.basename(__file__)} took ----- {time()-start_time} ----- seconds to run")