import os
from time import time
import numpy as np
import statistics
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns; sns.set_theme()
import sys
from pathlib import Path
import copy
dirname = os.path.dirname(__file__)
grandParDir=(str(Path(__file__).parents[1]).replace(os.sep, '/'))
sys.path.insert(0, grandParDir)
from commonFunctions import *
np.seterr(divide='ignore', invalid='ignore')

# Measure how long the program takes to run
start_time=time()

# Parameters
# platingList=[1,2,3,6]
# cultureList=[3,2,4,1]
# divListList=[[4,13,25],[4,19,35],[7,20,31],[4,19,34]]
platingList=[1]
cultureList=[3]
divListList=[[4]]
version=5

for thing in range(len(platingList)):
    plating=platingList[thing]
    culture=cultureList[thing]
    divList=divListList[thing]
    for div in divList:
        dataList=np.array(getDataList(plating,culture,div) )
        channelList=dataList[:,1].astype(int)
        timeList=dataList[:,0]
        # Look for thing that spikes the most
        counts = np.bincount(channelList)
        mode=np.argmax(counts)
        print(mode)
        modeTimeList=timeList[channelList==mode]
        modeTimeInterval=np.diff(modeTimeList)
        fixedTimeInterval=statistics.mean(modeTimeInterval)/4

        for masterChannel in range(60): #change this back to 60
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
                    channel=int(data[1])
                    t=data[0]
                    if t-masterTime>=fixedTimeInterval:
                        break
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
            numDataCoord=np.zeros((8,8)).astype(str)
            for index,value in enumerate(timeIntervals):
                x=numToCoord(index)[1]
                y=numToCoord(index)[0]
                if len(value)>1:
                    exp=statistics.mean(value)
                    var=statistics.variance(value)
                    cv=(var/exp**2)**0.5
                    cvListCoord[y][x]=cv
                    numDataCoord[y][x]='\n'+str(len(value))
            mask=np.zeros_like(cvListCoord)
            mask[cvListCoord==-100]=True

            # Plot Heatmap
            fig, ax = plt.subplots()
            cvListArray = np.array(cvListCoord)
            cvListRounded=(np.around(cvListArray, decimals=3)).astype(str)
            annotation=np.core.defchararray.add(cvListRounded, numDataCoord)
            ax = sns.heatmap(cvListArray,annot=annotation,fmt='',vmin=0,vmax=2,mask=mask,robust=True)
            ax.set_title(f"Heat map of C_v of waiting times after master channel for a fixed time interval {fixedTimeInterval}s after {masterChannel} in plating {plating}, culture {culture}, div {div}.",wrap=True)
            position=(numToCoord(masterChannel)[1],numToCoord(masterChannel)[0])
            ax.add_patch(Rectangle(position, 1, 1, fill=False, edgecolor='blue', lw=3))
            plt.savefig(f'{dirname}/Heatmaps/Heatmap{version}_{plating}_{culture}_{div}_{masterChannel}.eps', format='eps')

        texMaker(plating,culture,div,version)

print(f"{os.path.basename(__file__)} took ----- {time()-start_time} ----- seconds to run")