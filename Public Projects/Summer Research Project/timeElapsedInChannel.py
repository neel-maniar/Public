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
cvMatrix=[]
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
cvList=[]
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
    for i in range(1,61):
        channels=[i]
        ## Find intervals
        timeListSpecificChannel=[row[0] for row in dataList if row[1] in channels]
        timeIntervals=np.diff(timeListSpecificChannel)
        if len(timeIntervals)>1:
            # print("Maximum time between spikes:" ,max(timeIntervals))
            # print("Minimum time between spikes:", min(timeIntervals))

            ## Plot histogram
            # plt.hist(timeIntervals, bins = 100) 
            # plt.show()

            ## Find C_v:
            exp=statistics.mean(timeIntervals)
            var=statistics.variance(timeIntervals)
            cvList.append((var/exp**2)**0.5)
            if i==49:
                print(exp)
    if len(cvList)>0:
        cvMatrix.append(cvList)
    cvList=[]
fig, ax1 = plt.subplots(figsize=(10, 6))
# Creating two axes
# add_axes([xmin,ymin,dx,dy])
fig.canvas.manager.set_window_title('Boxplot'+str(plating)+str(culture))
bp = ax1.boxplot(cvMatrix)
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
ax1.set(
    axisbelow=True,  # Hide the grid behind plot objects
    title='Boxplots of coefficient of variation of intervals between spikes in channels of Plating '+str(plating)+', Culture '+str(culture)+' vs time',
    xlabel='Days In Vitro',
    ylabel='C_v of channels',
)
start, end = ax1.get_ylim()
ax1.yaxis.set_ticks(np.arange(start, end, 1))
ax1.set_xticklabels(xLabel[0:div])
# plt.savefig('C:/Users/Neel/OneDrive/Documents/Summer Research Project/Figures/Boxplot'+str(plating)+str(culture)+'.eps', format='eps')

end = timer()
print("Time elapsed in program:",end - start)
plt.show()