import re
import bz2
import os
from time import time
import requests
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
start_time = time()
platingList=[1,1,2,2,3,3,6,6]
cultureList=[1,3,2,4,4,5,1,3]
# platingList=[6,6]
# cultureList=[1,3]

# platingList=[1,2,2,3,3,6,6]
# cultureList=[3,2,4,4,5,1,3]
# Change the title and the filename and the code!
dataTreatment="None" # number (below which we want to ignore data. Write 1 if want to leave data untreated), or "Weighted"
for i in range(len(platingList)):
    plating=platingList[i]
    culture=cultureList[i]
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
        for i in range(60):
            channels=[i]
            ## Find intervals
            timeListSpecificChannel=[row[0] for row in dataList if row[1] in channels]
            timeIntervals=np.diff(timeListSpecificChannel)
            lenTimeIntervals=len(timeIntervals)

            if dataTreatment=="Weighted":
                if lenTimeIntervals>1:
                    exp=statistics.mean(timeIntervals)
                    var=statistics.variance(timeIntervals)
                    cv=(var/exp**2)**0.5
                    cvList+=lenTimeIntervals*[cv]
            else:
                if len(timeIntervals)>dataTreatment: # Change 1000 to 1 if you don't want to filter out c_vs with fewer data points
                    exp=statistics.mean(timeIntervals)
                    var=statistics.variance(timeIntervals)
                    cvList.append((var/exp**2)**0.5)

        if len(cvList)>0:
            cvMatrix.append(cvList)
        else:
            print(URL)
        cvList=[]
    ## Boxplots
    fig, ax = plt.subplots(figsize=(10, 6))
    # Creating two axes

    fig.canvas.manager.set_window_title('Boxplot'+str(plating)+str(culture))
    bp = ax.boxplot(cvMatrix)
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
    ax.set(
        axisbelow=True,  # Hide the grid behind plot objects
        title='Boxplots of c_v of intervals between spikes in channels of Plating '+str(plating)+', Culture '+str(culture)+' vs time, omitting <1000 datapoints',
        xlabel='Days In Vitro',
        ylabel='C_v of channels',
    )
    start, end = ax.get_ylim()
    ax.yaxis.set_ticks(np.arange(math.floor(start), math.ceil(end), 1))
    ax.set_xticklabels(xLabel[0:len(cvMatrix)])

    ## Adding legend
    textstr = '\n'.join((
        'Orange line is median',
        'Box is lower and upper quartiles',
        'Whiskers are extremal datapoints which are',
        'within 1.5*IQR of the upper/lower quartiles' ,
    ))

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # place a text box in upper left in axes coords
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)

    if dataTreatment==1:
        treatmentText="Untreated"
    elif isinstance(dataTreatment, int):
        treatmentText="Omitted"+str(dataTreatment)
    else:
        treatmentText=dataTreatment

    # plt.savefig('C:/Users/Neel/OneDrive/Documents/Summer Research Project/Figures/Boxplot'+treatmentText+str(plating)+str(culture)+'.eps', format='eps')

print("Process finished --- %s seconds ---" % (time() - start_time))
plt.show()