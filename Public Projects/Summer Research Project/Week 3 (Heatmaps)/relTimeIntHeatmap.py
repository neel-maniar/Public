import re
import seaborn as sns; sns.set_theme()
import bz2
import os
from time import time
import requests
import numpy as np
import matplotlib.pyplot as plt
import statistics
from matplotlib.patches import Rectangle
import copy
import sys
from pathlib import Path
dirname = os.path.dirname(__file__)
grandParDir=(str(Path(__file__).parents[1]).replace(os.sep, '/'))
sys.path.insert(0, grandParDir)
from commonFunctions import *
np.seterr(divide='ignore', invalid='ignore')

# Measure how long the program takes to run

# Parameters
plating=1
culture=3
divList=[4]
version=2

for div in divList:
    dataList=getDataList(plating,culture,div)
    for masterChannel in range(60):
        print(f"{masterChannel}/59")
        timeListMasterChannel=[[index,row[0]] for index,row in enumerate(dataList) if row[1] == masterChannel]
        timeIntervals=[[] for i in range(60)]
        checkChannel=[i for i in range(60)]


        for index,masterTime in timeListMasterChannel:
            AppendedYet=[False for i in range(60)]
            DoneFlag=False
            count=index+1
            while count<len(dataList) and DoneFlag==False:
                data=dataList[count]
                channel=data[1]
                t=data[0]
                if AppendedYet[channel]==False:
                    timeIntervals[channel].append(t-masterTime)
                    AppendedYet[channel]=True
                DoneFlag=all([AppendedYet[i] for i in checkChannel])
                count+=1
            checkChannelCopy=copy.deepcopy(checkChannel)
            for channel in checkChannelCopy:
                if AppendedYet[channel]==False:
                    checkChannel.remove(channel)
                    


        cvListCoord=np.array([[-100.0 for i in range(8)] for j in range(8)])
        for index,value in enumerate(timeIntervals):
            x=numToCoord(index)[1]
            y=numToCoord(index)[0]
            if len(value)>1:
                exp=statistics.mean(value)
                var=statistics.variance(value)
                cv=(var/exp**2)**0.5
                cvListCoord[y][x]=cv
        mask=np.zeros_like(cvListCoord)
        mask[cvListCoord==-100]=True
        count=0
        numData=str(len(timeIntervals[masterChannel]))
        for entry in dataList:
            if entry[1]==14:
                count+=1
        # Plot Heatmap
        fig, ax = plt.subplots()
        cvListArray = np.array(cvListCoord)
        cvListRounded=np.around(cvListArray, decimals=3)
        ax = sns.heatmap(cvListArray,annot=cvListRounded,fmt='',vmin=0,vmax=2,mask=mask,robust=True)
        ax.set_title(f"Heat map of C_v of waiting times after master channel {masterChannel} in plating {plating}, culture {culture}, div {div}, with {numData} datapoints in the highlighted channel",wrap=True)
        position=(numToCoord(masterChannel)[1],numToCoord(masterChannel)[0])
        ax.add_patch(Rectangle(position, 1, 1, fill=False, edgecolor='blue', lw=3))
        plt.savefig(f'{dirname}/Heatmaps/Heatmap{version}_{plating}_{culture}_{div}_{masterChannel}.eps', format='eps')
        plt.close('all')

    texMaker(plating,culture,div,version)