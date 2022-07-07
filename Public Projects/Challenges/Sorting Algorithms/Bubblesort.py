unSorted = [3,2,0,1]
token=0
while True:
    for x in range(0,len(unSorted)):
        if x<len(unSorted)-1:
            if unSorted[x]>unSorted[x+1]:
                c=unSorted[x+1]
                unSorted[x+1]=unSorted[x]
                unSorted[x]=c
            else:
                token+=1
    if token==(len(unSorted))-1:
        break
    token=0
print(unSorted)
