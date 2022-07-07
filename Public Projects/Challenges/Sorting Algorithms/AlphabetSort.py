import string
MyFile=open("AlphabetTest","r")
x=MyFile.readlines()
print(x)
MyFile.close()
newX=[]
alpha=[i for i in string.ascii_lowercase]
for i in x:
    word=i[:len(i)-1]
    n=4
    tot=0.0
    for char in word:
        ind=alpha.index(char)+1
        tot+=ind*10**n
        n-=2
    newX.append([tot,word])
def BubbleSort(twoDimensions):
    unSorted=[i for i[0] in twoDimensions]
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
BubbleSort(newX)
print(newX)
    

