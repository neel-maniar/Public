import numpy as np
from time import time
import random
random.seed(10)
x = []
for i in range(0,500):
    l = random.randint(1,300)
    x.append(l)

y = []
for i in range(0,500):
    l = random.randint(1,300)
    y.append(l)

xArray=np.array(x)
yArray=np.array(y)

start_time = time()

def linRegress(x,y):
    if x.shape[0]!=y.shape[0]:
        return("ERROR - Lists must be of the same length")
    sumxsquared=np.sum(x**2)
    sumysquared=np.sum(y**2)
    sumx=np.sum(x)
    sumy=np.sum(y)
    n=x.shape[0]
    sumxy=np.dot(x,y)
    denominatorx=float(n*sumxsquared-sumx**2)
    denominatory=float(n*sumysquared-sumy**2)
    intercept=(sumxsquared*sumy-sumx*sumxy)/denominatorx
    gradient=(n*sumxy-sumx*sumy)/denominatorx
    r=(n*sumxy-sumx*sumy)/(denominatorx*denominatory)**0.5
    print(type(denominatorx))
    print((denominatorx*denominatory)**0.5)
    return(intercept,gradient,r)
    
print(linRegress(xArray,yArray))

print("Process finished --- %s seconds ---" % (time() - start_time))

start_time=time()

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

print(linRegress(x,y))
print("Process finished --- %s seconds ---" % (time() - start_time))