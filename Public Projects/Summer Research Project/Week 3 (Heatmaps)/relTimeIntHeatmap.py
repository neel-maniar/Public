from doctest import master
import re
import bz2
import os
from time import time
import requests
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math

# Measure how long the program takes to run
start_time = time()

# Parameters
plating=1
culture=1
div=13
masterChannel=49

## List of URLs for a particular day
listsURL="https://neurodatasharing.bme.gatech.edu/development-data/html/wget/daily.spont.dense.text."+str(plating)+"."+str(culture)+".0.list"
# Get it from the internet
response = requests.get(listsURL)
# Put it in a file
dirname = os.path.dirname(__file__)
path = dirname+"/listOfURLs"
open(path, "wb").write(response.content)
listOfURLs = [line.rstrip() for line in open(path)]
listOfDivs=[]
# Find the divs for which data is available, by regex
for line in listOfURLs:
    match = re.search('(\d+)(?=\s*\.spk\.txt\.bz2)', line)
    if match:
        listOfDivs.append(int(match.group(1)))

# Which div?
try:
    listIndex=listOfDivs.index(div)
except:
    print("There was no data recorded for plating "+str(plating)+", culture "+str(culture)+" on div "+str(div))
    quit()

URL=listOfURLs[listIndex]
## Import Data from URL
response = requests.get(URL)
dirname = os.path.dirname(__file__)
path = dirname+"\\testbz2"
newPath = path.replace(os.sep, '/')
open(newPath, "wb").write(response.content)

## Process data by reading it off as a string and converting to list
bz_file = bz2.BZ2File(newPath)
data = bz_file.read().decode('ascii')
dataList = [[float(line.split()[0]),int(line.split()[1])] for line in data.splitlines()]
timeListMasterChannel=[row[0] for row in dataList if row[1] == masterChannel]

timeIntervals=[[] for i in range(60)]
AppendedYet=[True for i in range(60)]
currMasterTime=0
prevMasterTime=0
for entry in dataList:
    t=entry[0]
    channel=entry[1]
    if channel==masterChannel:
        currMasterTime=t
        AppendedYet=[False for i in range(60)]
    if AppendedYet[channel]==False:
        if channel!=masterChannel:
            timeIntervals[entry[1]].append(entry[0]-currMasterTime)
            AppendedYet[entry[1]]=True
        else:
            if prevMasterTime!=0:
                timeIntervals[masterChannel].append(currMasterTime-prevMasterTime)
            prevMasterTime=currMasterTime

cvList=[]
for i in timeIntervals:
    if len(i)>1:
        exp=statistics.mean(timeIntervals)
        var=statistics.variance(timeIntervals)
        cv=(var/exp**2)**0.5
        cvList+=lenTimeIntervals*[cv]

# if lenTimeIntervals>1:
#     exp=statistics.mean(timeIntervals)
#     var=statistics.variance(timeIntervals)
#     cv=(var/exp**2)**0.5
#     cvList+=lenTimeIntervals*[cv]

# if len(timeIntervals)>1000: # Change 1000 to 1 if you don't want to filter out c_vs with fewer data points
# ## Find C_v:
#     exp=statistics.mean(timeIntervals)
#     var=statistics.variance(timeIntervals)
#     cvList.append((var/exp**2)**0.5)
# #     if i==49:
# #         print(exp)
# if len(cvList)>0:
#     cvMatrix.append(cvList)
# else:
#     print(URL)
# cvList=[]
print("Process finished --- %s seconds ---" % (time() - start_time))