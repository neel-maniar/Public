import os
from time import time
import numpy as np
import statistics
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns; sns.set_theme()
import sys
from pathlib import Path
import pandas as pd
from decimal import Decimal

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
version=5

for thing in range(len(platingList)):
    plating=platingList[thing]
    culture=cultureList[thing]
    divList=divListList[thing]
    for div in divList:
        dataList = np.array(getDataList(plating,culture,div) )
        channelList=dataList[:,1].astype(int)
        timeList=dataList[:,0]
        # # Look for thing that spikes the most
        counts = np.bincount(channelList)
        mode=np.argmax(counts)
        modeTimeList=timeList[channelList==mode]
        modeTimeInterval=np.diff(modeTimeList)
        originalMean=(statistics.mean(modeTimeInterval))
        arr=(modeTimeInterval < originalMean)
        fixedTimeInterval=(statistics.mean(modeTimeInterval[arr]))/10
        timeChannels=[[index for index,row in enumerate(dataList) if row[1]==channel] for channel in range(60)]
        for masterChannel in range(60): #change this back to 60
            print(f"{masterChannel}/59")
            timeListMasterChannel=[[index,row[0]] for index,row in enumerate(dataList) if row[1] == masterChannel]
            num1Und=[0 for i in range(60)]
            numTotal=[0 for i in range(60)]
            sum=0
            # timeListMasterChannel=timeChannels[masterChannel]
            if len(timeListMasterChannel)==0:
                print(f"No data for channel {masterChannel}")
            timeIntervals=[[] for i in range(60)]

            for index,masterTime in timeListMasterChannel:
                # E.g. index,masterTime=0,12.3
                channelTimeInterval=[]
                # E.g. [34,23,12,45,45]
                AppendedYet=[False for i in range(60)]
                count=index+1
                while count<len(dataList):
                    t=dataList[count][0]
                    channel=int(dataList[count][1])
                    if t-masterTime>=fixedTimeInterval:
                        break
                    if AppendedYet[channel]==False:
                        timeIntervals[channel].append(t-masterTime)
                        AppendedYet[channel]=True
                    channelTimeInterval.append(channel)
                    count+=1

                if len(channelTimeInterval)>0: 
                    pandating=pd.Series(channelTimeInterval)
                    freq=pandating.value_counts()
                    for i in range(60):
                        if i in freq:
                            if (freq[i])<=1:
                                num1Und[i]+=1
                        else:
                            num1Und[i]+=1
                else:
                    for i in range(60):
                        num1Und[i]+=1

            # Now we have the num1Und in its entirety after iterating through all timeMasterList

            cvListCoord=np.array([[-100.0 for i in range(8)] for j in range(8)])
            numDataCoord=np.zeros((8,8)).astype(str)
            numTimeIntervals=np.zeros((8,8)).astype(str)
            for index,value in enumerate(timeIntervals):
                x=numToCoord(index)[1]
                y=numToCoord(index)[0]
                if len(value)>1:
                    exp=statistics.mean(value)
                    var=statistics.variance(value)
                    cv=(var/exp**2)**0.5
                    cvListCoord[y][x]=cv
                    numTimeIntervals[y][x]=str(len(value))
                    numDataCoord[y][x]='\n'+str(int(num1Und[index]/len(timeListMasterChannel)*100))+'%'
            mask=np.zeros_like(cvListCoord)
            mask[cvListCoord==-100]=True

            ## Plot Heatmap
            fig, ax = plt.subplots()
            cvListArray = np.array(cvListCoord)
            cvListRounded=(np.around(cvListArray, decimals=3)).astype(str)
            annotation=np.core.defchararray.add(numTimeIntervals, numDataCoord)
            ax = sns.heatmap(cvListArray,annot=annotation,fmt='',vmin=0,vmax=2,mask=mask,robust=True)
            ax.set_title(f"Heat map of C_v of waiting times after master channel for a fixed time interval {'%.2E' % Decimal(str(fixedTimeInterval))}s after {masterChannel} in plating {plating}, culture {culture}, div {div}.",wrap=True)
            position=(numToCoord(masterChannel)[1],numToCoord(masterChannel)[0])
            ax.add_patch(Rectangle(position, 1, 1, fill=False, edgecolor='blue', lw=3))
            plt.savefig(f'{dirname}/Heatmaps/Heatmap{version}_{plating}_{culture}_{div}_{masterChannel}.eps', format='eps')
            # plt.show()
            plt.close('all')
        # texMaker(plating,culture,div,version)