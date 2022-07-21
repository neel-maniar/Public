import re
import bz2
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
import statistics
from time import time
start_time = time()

plating=6
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
channels=[[10],[25],[26],[49],[50],[51]] #[i for i in range(60)]

expMatrix=[]
varMatrix=[]
LambdaMatrix=[]
numDataMatrix=[]
channelList=[]
## Find intervals
for j in channels:
    print(f"Now looking at channel {j}")
    expList=[]
    LambdaList=[]
    varList=[]
    numDataList=[]
    badFlag=False
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
            # expList.append(exp)
            LambdaList.append(Lambda)
            varList.append(var)
            # numDataList.append(n)
            if (var**0.5)/(((n-1)/n)*Lambda)>0.1:
                badFlag=True
            
    # numDataMatrix.append(numDataList)
    # expMatrix.append(expList)
    if badFlag==False:
        LambdaMatrix.append(LambdaList)
        channelList.append(j[0])
    badFlag=False
    # varMatrix.append(varList)

# print(expMatrix)
# print("\n")
# print(LambdaMatrix)
# print("\n")
# print(varMatrix)


for i,channel in enumerate(LambdaMatrix):
    if len(xLabel)==len(channel):
        plt.plot(xLabel, channel, label = str(channelList[i]))
    print(i,len(xLabel),len(channel))

print(len(LambdaMatrix))


plt.xlabel('DIV')
# Set the y axis label of the current axis.
plt.ylabel('MLE Estimator of lambda')
# Set a title of the current axes.
plt.title(f'MLE Estimator of lambda over time for various channels in plating {plating}, culture {culture}',wrap=True)
# show a legend on the plot
plt.legend()
# save plot
dirname = os.path.dirname(__file__)
path=dirname+"/LambdaEstimatorPlots/Lambda"+str(plating)+str(culture)+".eps"
plt.savefig(path)
print("Process finished --- %s seconds ---" % (time() - start_time))
# Display a figure.
plt.show()