def linRegress(x,y):
    if len(x)!=len(y):
        return("ERROR - Lists must be of the same length")
    sumxsquared=sum(i*i for i in x)
    sumx=sum(x)
    sumy=sum(y)
    n=len(x)
    sumxy=sum(x[i]*y[i] for i in range(n))
    denominator=(n*sumxsquared-sumx**2)
    intercept=(sumxsquared*sumy-sumx*sumxy)/denominator
    gradient=(-sumx*sumy+n*sumxy)/denominator
    return(intercept,gradient)