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
from scipy.stats import skew

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
        skewness=skew(modeTimeInterval)
        originalMean=(statistics.mean(modeTimeInterval))
        arr=(modeTimeInterval < originalMean)
        fixedTimeInterval=(statistics.mean(modeTimeInterval[arr]))/10
        print(fixedTimeInterval,statistics.median(modeTimeInterval)/10)
