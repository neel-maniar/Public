import re
import bz2
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
import statistics
from timeit import default_timer as timer
start = timer()
plating=1
culture=3
## List of URLs for a particular day
bigURL="https://neurodatasharing.bme.gatech.edu/development-data/html/wget/daily.spont.dense.text."+str(plating)+"."+str(culture)+".0.list"
response = requests.get(bigURL)
dirname = os.path.dirname(__file__)
path = dirname+"/testfile"
open(path, "wb").write(response.content)
listOfFiles = [line.rstrip() for line in open(path)]
div=len(listOfFiles)
xLabel=[]
for line in listOfFiles:
    match = re.search('(\d+)(?=\s*\.spk\.txt\.bz2)', line)
    if match:
        xLabel.append(int(match.group(1)))
expList=[]
for URL in listOfFiles[0:div]:
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
    channels=[i for i in range(60)]
    ## Find intervals
    timeListSpecificChannel=[row[0] for row in dataList if row[1] in channels]
    timeIntervals=np.diff(timeListSpecificChannel)
    if len(timeIntervals)>0:
        # print("Maximum time between spikes:" ,max(timeIntervals))
        # print("Minimum time between spikes:", min(timeIntervals))

        ## Plot histogram
        # plt.hist(timeIntervals, bins = 100) 
        # plt.show()

        ## Find C_v:
        exp=statistics.mean(timeIntervals)
        expList.append(exp)
print(expList)