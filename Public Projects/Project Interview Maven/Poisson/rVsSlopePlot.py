import matplotlib.pyplot as plt
from math import log
import csv
import os
import numpy as np

plating=1
culture=1
div=4

dirname = os.path.dirname(__file__)
datafile=dirname+"/cvLists/cvList"+str(plating)+str(culture)+str(div)+".csv"

# CSVData = open(datafile)
# data = np.loadtxt(CSVData, delimiter=",")

data = [[float(j) for j in i] for i in list(csv.reader(open(datafile)))]

timeIntervalList=[0.01,0.05,0.1,0.2,0.5,1,2,3,4,5,6,7,8,10,20,50,100,200,300,500,1000]

def linRegress(x,y):
    if len(x)!=len(y):
        return("ERROR - Lists must be of the same length")
    sumxsquared=sum(i*i for i in x)
    sumysquared=sum(i*i for i in y)
    sumx=sum(x)
    sumy=sum(y)
    n=len(x)
    sumxy=sum(x[i]*y[i] for i in range(n))
    denominatorx=(n*sumxsquared-sumx**2)
    denominatory=(n*sumysquared-sumy**2)
    intercept=(sumxsquared*sumy-sumx*sumxy)/denominatorx
    gradient=(n*sumxy-sumx*sumy)/denominatorx
    r=(n*sumxy-sumx*sumy)/(denominatorx*denominatory)**0.5 
    return(intercept,gradient,r)

logTime=[log(i) for i in timeIntervalList]
gradientList=[]
rList=[]
for cvList in data:
    logcv=[log(i) for i in cvList]
    gradient=linRegress(logTime,logcv)[1]
    r=linRegress(logTime,logcv)[2]
    gradientList.append(gradient)
    rList.append(r)

title=f"R-value vs gradient for log(C_v) vs log(Delta) in each channel of plating {plating}, culture {culture}, div {div}"
plt.scatter(gradientList,rList)
plt.title(title,wrap=True)
plt.xlabel("Gradient")
plt.ylabel("R-value")
# plt.savefig(f'C:/Users/Neel/OneDrive/Documents/Summer Research Project/Figures/rVsSlopePlot{plating}{culture}{div}.eps', format='eps')
plt.show()

