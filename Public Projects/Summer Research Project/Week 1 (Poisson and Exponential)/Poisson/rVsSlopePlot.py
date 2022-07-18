import matplotlib.pyplot as plt
from math import log
import csv
import os
import numpy as np

plating=1
culture=3
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
    print((denominatorx*denominatory)**0.5)
    return(intercept,gradient,r)

logTime=[log(i) for i in timeIntervalList]
gradientList=[]
rList=[]
for i in data:
    print(len(logTime),len(i))
# for cvList in data:
#     logcv=[log(i) for i in cvList]
#     print(linRegress(logTime,logcv))
#     gradient=linRegress(logTime,logcv)[1]
#     r=linRegress(logTime,logcv)[2]
#     gradientList.append(gradient)
#     rList.append(r)

# plt.scatter(gradientList,rList)
# # plt.savefig('C:/Users/Neel/OneDrive/Documents/Summer Research Project/Figures/rVsSlopePlot'+str(plating)+str(culture)+str(div)+'.eps', format='eps')
# plt.show()

