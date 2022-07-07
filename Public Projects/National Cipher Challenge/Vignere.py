import string
inp="hqmpr gxclw jlmbn ljeel rkmzq qqocm lbkqq ffrgi vyiko qkzrv mgkxy iounu svtuh p".upper()

alpha=[i for i in string.ascii_uppercase]
cipher=""
frequency="ETAOINSHRDLCUMWFGYPBVKJXQZ"
for i in inp:
    if i in alpha:
        cipher+=i

def findRepeats(ciph):
    repeat={}
    repList=[]
    for n in range(3,6):
        for i in range(0,len(ciph)-n+1):
            currentGroup=ciph[i:i+n]
            if currentGroup in repList:
                repeat.update({currentGroup:len(repList)-(repList.index(currentGroup))})
            repList.append(currentGroup)
    return repeat

def factorDict(repD):
    valueDict={}
    for n in list(repD.values()):
        for i in range(2,n+1):
            if n%i==0:
                if i not in valueDict:
                    valueDict.update({i:1})
                else:
                    valueDict[i]+=1
    return valueDict
    for key,value in valueDict.items():
        if value == max(list(valueDict.values())):
            return key 

def frequencyAnalysis(cipher):
    def BubbleSort(unSorted):
        token=0
        while True:
            for x in range(0,len(unSorted)):
                if x<len(unSorted)-1:
                    if unSorted[x]<unSorted[x+1]:
                        c=unSorted[x+1]
                        unSorted[x+1]=unSorted[x]
                        unSorted[x]=c
                    else:
                        token+=1
            if token==(len(unSorted))-1:
                break
            token=0
        return unSorted

    key=[]
    dictionary={}
    for i in string.ascii_uppercase:
        dictionary.update({i:0})

    for i in cipher:
        if i in dictionary:
            dictionary[i]+=1

    order=[]
    val=list(dictionary.values())
    sortedVal=BubbleSort(val)
    for i in range(0,26):
        key=list(dictionary.keys())[list(dictionary.values()).index(sortedVal[i])]
        value=sortedVal[i]
        if key not in order:
            order.append(key)
        else:
            del dictionary[key]
            order.append(list(dictionary.keys())[list(dictionary.values()).index(sortedVal[i])])
            #order.append([list(dictionary.keys())[list(dictionary.values()).index(sortedVal[i])],list(dictionary.values()).index(sortedVal[i])])
            dictionary.update({key:value})
    return order

def caesar(cipher,shift):
    plain=""
    for i in cipher:
        if i in alpha:
            if alpha.index(i)+shift<26:
                plain+=alpha[alpha.index(i)+shift]
            else:
                plain+=alpha[alpha.index(i)-26+shift]
        else:
            plain+=" "
    return(plain)


"""2: 538, 3: 526, 6: 507, 9: 146, 18: 142, 113: 5, 226: 5, 339: 5, 678: 5, 1017: 1, 2034: 1, 19: 25, 38: 22, 57: 22, 114: 21, 5: 137, 10: 131, 15: 128, 30: 126, 73: 13, 146: 12, 219: 12, 365: 2, 438: 11, 730: 1, 1095: 2, 2190: 1, 4: 296, 8: 137, 1"""
mainKey=6

def splicer(ciph,n):
    myString=""
    #key=factorDict(findRepeats(ciph))
    key=mainKey
    for i in range(0,int(len(ciph)/key)+1):
        if len(ciph)>key*i+n:
            myString+=(ciph[key*i+n])
    return myString

#print(factorDict(findRepeats(cipher)))
key=""
#for i in range(0,factorDict(findRepeats(cipher))):
for i in range(0,mainKey):
    print(frequencyAnalysis(splicer(cipher,i)))
    a=frequencyAnalysis(splicer(cipher,i))[0]
    key+=alpha[int(alpha.index(a)-alpha.index("E"))]
print(key)

key="TURKEY"
almost=[]
for i in range(0,len(key)):
    almost.append(caesar(splicer(cipher,i),26-alpha.index(key[i])))

  
plaintext=""

for j in range(0,len(almost[len(almost)-1])+1):
    for i in range(0,len(almost)):
        if len(almost[i])>j:
            plaintext+=almost[i][j]
print(plaintext[::-1])
print(len(cipher))