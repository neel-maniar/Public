def linRegress(x,y):
    if len(x)!=len(y):
        return("ERROR - Lists must be of the same length")
    sumxsquared=sum(i*i for i in x)
    sumysquared=sum(i*i for i in y)
    sumx=sum(x)
    sumy=sum(y)
    n=len(x)
    sumxy=sum(x[i]*y[i] for i in range(n))
    denominatorx=(n*sumxsquared-sumx**2) #var_x*n^2
    denominatory=(n*sumysquared-sumy**2) #var_y*n^2
    intercept=(sumxsquared*sumy-sumx*sumxy)/denominatorx
    gradient=(n*sumxy-sumx*sumy)/denominatorx
    r=(n*sumxy-sumx*sumy)/(denominatorx*denominatory)**0.5 # gradient*sigma_x/sigma_y
    return(intercept,gradient,r)