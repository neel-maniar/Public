import re
import bz2
import os
import requests
import matplotlib.pyplot as plt
from time import time
from collections import Counter

# Measure how long the program takes to run
start_time = time()

# Parameters
plating=1
culture=3
div=25
channels=[[i] for i in range(5)] # Which channels do we want to monitor?

# Which values of delta do we want to try?
timeIntervalList=[0.01,0.05,0.1,0.2,0.5,1,2,3,4,5,6,7,8,10,20,50,100,200,300,500,1000]


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
    plt.title("Number of spikes in time bins of size "+str(timeInterval)+" in all channels, channel 1-3, div 4")
    # plt.savefig('C:/Users/Neel/OneDrive/Documents/Summer Research Project/Figures/BarChart'+str(timeInterval)+'.eps', format='eps')
    plt.cla()


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
    ## Find intervals
    timeListSpecificChannel=[row[0] for row in dataList if row[1] in channel]
    if len(timeListSpecificChannel)>0:
        for timeInterval in timeIntervalList:
            timeListFloored=[i//timeInterval for i in timeListSpecificChannel]
            most_common,num_most_common = Counter(timeListFloored).most_common(1)[0] # 4, 6 times
            frequencies=[0 for i in range(num_most_common+1)]
            numOccurences=[i for i in range(num_most_common+1)]
            maxInTimeList=int(timeListFloored[-1])
            frequencyTable=[[i,timeListFloored.count(i)] for i in range(maxInTimeList+1)]
            for i in range(num_most_common+1):
                for k in frequencyTable:
                    if k[1]==i:
                        frequencies[i]+=1
            if sum(frequencies)>1:
                exp=sum([index*value for index,value in enumerate(frequencies)])/sum(frequencies)
                var=sum([value*(index-exp)**2 for index,value in enumerate(frequencies)])/(sum(frequencies)-1)
                cv=(var/exp**2)**0.5
                cvList.append(cv)
            # barChart(numOccurences, frequencies, timeInterval)
        # Add to text file
        cvMatrix.append(cvList)
        path=dirname+"/cvList.txt"
        text_file = open(path, "a")
        text_file.write(str(cvList))
        text_file.write("\n")
        text_file.close()
        cvList=[]

#close file
print("Process finished --- %s seconds ---" % (time() - start_time))
print(cvMatrix)