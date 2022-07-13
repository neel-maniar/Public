import re
import bz2
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
import statistics
from time import time
start_time = time()

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
# channels=[[10],[25],[26],[49],[50],[51],[i for i in range(60)]]
expMatrix=[]
varMatrix=[]
LambdaMatrix=[]
## Find intervals
for j in channels:
    expList=[]
    LambdaList=[]
    varList=[]
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
        # 10,25,26,49,50,51,All
        timeListSpecificChannel=[row[0] for row in dataList if row[1] in j]
        timeIntervals=np.diff(timeListSpecificChannel)
        if len(timeIntervals)>0:
            ## Find C_v:
            n=len(timeIntervals)
            exp=statistics.mean(timeIntervals)
            Lambda=1/exp
            var=Lambda**2*(n**2)/((n-1)**2*(n-2))
            expList.append(exp)
            LambdaList.append(Lambda)
            varList.append(var)
    expMatrix.append(expList)
    LambdaMatrix.append(LambdaList)
    varMatrix.append(varList)

print(expMatrix)
print("\n")
print(LambdaMatrix)
print("\n")
print(varMatrix)
print("Process finished --- %s seconds ---" % (time() - start_time))