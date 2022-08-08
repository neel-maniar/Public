import os
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns; sns.set_theme()
import sys
from pathlib import Path
from scipy.stats.distributions import chi2
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
version=7

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
        totDataList=np.array(t)
        phat=[i/sumT for i in t]
        chiSquared=[0 for i in range(64)]
        for masterChannel in range(60):
            expected=[t[masterChannel]*i for i in phat]
            masterIndices=np.array((channelList==masterChannel).nonzero()[0]).T
            pointsList=np.zeros(64).astype(int) #pointsList is the observed o_i
            for index in masterIndices:
                if index+1<len(dataList):
                    pointsList[int(dataList[index+1][1])]+=1
            chiSquared[masterChannel]=np.nansum(np.array([(o-e)**2/e for o,e in zip(pointsList,expected)]))
        chiSquaredMatrix=np.zeros((8,8))
        for r in range(8):
            for c in range(8):
                chiSquaredMatrix[r][c]=chiSquared[coordToNum(r,c)]
        chiSquaredRounded=(np.around(chiSquaredMatrix, decimals=1)).astype(str)
        # Plot Heatmap
        pValMatrix=chi2.cdf(chiSquaredMatrix, df=59)
        mask=1-np.zeros_like(chiSquaredMatrix)
        mask[np.nonzero(chiSquaredMatrix)]=False
        fig, ax = plt.subplots()
        ax = sns.heatmap(pValMatrix,annot=chiSquaredRounded,fmt='',robust=True,vmin=0,vmax=1,mask=mask)
        ax.set_title(f"p-value of first occurence data in plating {plating}, culture {culture}, div {div}",wrap=True)
        position=(numToCoord(masterChannel)[1],numToCoord(masterChannel)[0])
        ax.add_patch(Rectangle(position, 1, 1, fill=False, edgecolor='blue', lw=3))
        plt.savefig(f'{dirname}/Heatmaps/Heatmap{version}_{plating}_{culture}_{div}_{masterChannel}.eps', format='eps')
        # plt.show()
        plt.close('all')
        print(f"Figures produced for div {div}!")
        # texMaker(plating,culture,div,version)

print(f"{os.path.basename(__file__)} took ----- {time()-start_time} ----- seconds to run")