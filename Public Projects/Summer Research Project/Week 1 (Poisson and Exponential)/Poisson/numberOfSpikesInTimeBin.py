import re
import bz2
import os
import requests
import matplotlib.pyplot as plt
from time import time
from collections import Counter
import numpy

# Measure how long the program takes to run
start_time = time()

# Parameters
plating=2
culture=4
divList=[19,35]
channels=[[i] for i in range(60)] # Which channels do we want to monitor?

# Which values of delta do we want to try?
# timeIntervalList=[0.01,0.05,0.1,0.2,0.5,1,2,3,4,5,6,7,8,10,20,50,100,200,300,500,1000]
timeIntervalList=[2,5,10,50,100]

## List of URLs for a particular day
bigURL="https://neurodatasharing.bme.gatech.edu/development-data/html/wget/daily.spont.dense.text."+str(plating)+"."+str(culture)+".0.list"
# Get it from the internet
response = requests.get(bigURL)
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

def barChart(numOccurences, frequencies, timeInterval):
    plt.bar(numOccurences,frequencies)
    plt.xlabel("N_"+str(timeInterval))
    plt.ylabel("Frequency")
    plt.title(f"Number of spikes in time bins of size {timeInterval} in all channels, plating {plating}, channel {channel}, div {div}",wrap=True)
    # plt.savefig(f'C:/Users/Neel/OneDrive/Documents/Summer Research Project/Figures/BarChart{plating}{channel}{div}{timeInterval}.eps', format='eps')
    plt.show()
    plt.cla()

for div in divList:
    # Which div?
    try:
        listIndex=listOfDivs.index(div)
    except:
        print("There was no data recorded for plating "+str(plating)+", culture "+str(culture)+" on div "+str(div))
        quit()

    URL=listOfURLs[listIndex]
    ## Import Data from URL for the selected div
    response = requests.get(URL)
    dirname = os.path.dirname(__file__)
    path = dirname+"/databz2"
    newPath = path.replace(os.sep, '/')
    open(newPath, "wb").write(response.content)

    ## Process data by reading it off as a string and converting to list
    bz_file = bz2.BZ2File(newPath)
    data = bz_file.read().decode('ascii')
    dataList = [[float(line.split()[0]),int(line.split()[1])] for line in data.splitlines()]
    cvMatrix=[]
    cvList=[]
    for channel in channels:
        timeListSpecificChannel=[row[0] for row in dataList if row[1] in channel] # Isolate items in the time series which we care about.
        if len(timeListSpecificChannel)>1:
            for timeInterval in timeIntervalList:
                timeListFloored=[i//timeInterval for i in timeListSpecificChannel] # Calculate the bin which the spikes fall in
                most_common,num_most_common = Counter(timeListFloored).most_common(1)[0] # Find the highest number of spikes in a given bin 
                frequencies=[0 for i in range(num_most_common+1)] # frequencies[i]=Number of times something a bin had "i" many spikes in it.
                numOccurences=[i for i in range(num_most_common+1)] # x-axis for the graph
                maxInTimeList=int(timeListFloored[-1])
                frequencyTable=[[i,timeListFloored.count(i)] for i in range(maxInTimeList+1)] # Frequency table of number of spikes in time bin "i"
                # Convert frequency table to frequencies list (losing information on which particular time bins had x number of spikes)
                for i in range(num_most_common+1):
                    for k in frequencyTable:
                        if k[1]==i:
                            frequencies[i]+=1
                exp=sum([index*value for index,value in enumerate(frequencies)])/sum(frequencies)
                var=sum([value*(index-exp)**2 for index,value in enumerate(frequencies)])/(sum(frequencies)-1)
                cv=(var/exp**2)**0.5
                cvList.append(cv)
                barChart(numOccurences, frequencies, timeInterval)
            cvMatrix.append(cvList)
            cvList=[]
    cvMatrix = numpy.asarray(cvMatrix)
    dirname = os.path.dirname(__file__)
    path=dirname+"/cvLists/cvList"+str(plating)+str(culture)+str(div)+".csv"
    numpy.savetxt(path, cvMatrix, delimiter=",")
print("Process finished --- %s seconds ---" % (time() - start_time))
