primeFactor=[]
num=int(input("Enter num: "))
def factor(n):
    factorList=[]
    for i in range(1,n+1):
        if n%i==0:
           factorList.append(i)
    return factorList

for i in factor(num):
    if len(factor(i))==2:
        primeFactor.append(i)

print(primeFactor)

counter=0
counterList=[]
for i in primeFactor:
    numcopy=num
    while numcopy%i==0:
        counter+=1
        numcopy=numcopy/i
    counterList.append(counter)
    counter=0

for i in range(0,len(primeFactor)):
    if i+2 < len(primeFactor):
        print("%s to the power of %s, " % (primeFactor[i],counterList[i]),end="")
    elif i == len(primeFactor)-2:
        print("%s to the power of %s and " % (primeFactor[i],counterList[i]),end="")
    else:
        print("%s to the power of %s" % (primeFactor[i],counterList[i]),end="")
        