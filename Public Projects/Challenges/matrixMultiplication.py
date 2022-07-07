import time
import numpy
def matrixMult(A,B):
    A_size=(len(A),len(A[0]))
    B_size=(len(B),len(B[0]))
    if A_size[1]!=B_size[0]:
        return("Dimensionally incorrect")
    result=[[0 for i in range(B_size[1])] for j in range(A_size[0])]
    for a in range(A_size[0]):
        for b in range(B_size[1]):
            current=0
            for i in range(A_size[1]):
                current+=A[a][i]*B[i][b]
            result[a][b]=current
    return(result)

size=2
t0=time.time()            
matrixMult(numpy.random.random((size,size)),numpy.random.random((size,size)))
timePassed=time.time()-t0
print(timePassed)

#size=10
#t0=time.time()            
#matrixMult(numpy.random.random((size,size)),numpy.random.random((size,size)))
#timePassed10=time.time()-t0
#print(timePassed10)
#
#size=100
#t0=time.time()            
#matrixMult(numpy.random.random((size,size)),numpy.random.random((size,size)))
#timePassed100=time.time()-t0
#print(timePassed100)
#
#size=200
#t0=time.time()            
#matrixMult(numpy.random.random((size,size)),numpy.random.random((size,size)))
#timePassed200=time.time()-t0
#print(timePassed200)
#print()
#print(timePassed100/timePassed10)
#print(timePassed200/timePassed100)