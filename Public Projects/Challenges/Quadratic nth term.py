def nth():
    typeOfSequence = 0
    seqList = [float(x) for x in input("Enter your sequence: ").split(",")]
    for x in range(len(seqList)-2):
        if seqList[x] - seqList[x+1] == seqList[x+1] - seqList[x+2]:
            typeOfSequence += 0
        else:
            typeOfSequence += 1 
    if typeOfSequence == 0:
        multiplier = seqList[1] - seqList[0]
        adder = seqList[0]-multiplier
        if adder < 0:
            nthTerm = "The nth term is %sn%s"%(float(multiplier),float(adder))
        else:  
            nthTerm = "The nth term is %sn+%s"%(float(multiplier),float(adder))
        return nthTerm
    if typeOfSequence>0:
        floaterSeq = []
        for x in range(len(seqList)-1):
            floaterSeq.append(seqList[x+1]-seqList[x])
        if len(floaterSeq)>2:
            for x in range(len(floaterSeq)-2):
                if floaterSeq[x] - floaterSeq[x+1] == floaterSeq[x+1] - floaterSeq[x+2]:
                    multiplySquare = (floaterSeq[1]-floaterSeq[0])/2
        else:
            multiplySquare = (floaterSeq[1]-floaterSeq[0])/2
        
        square=[]
        for x in range(len(seqList)):
            square.append(multiplySquare * (x+1)**2)
        difference = []
        for x in range(len(seqList)):
            difference.append(seqList[x]-square[x])
        multiplier = difference[1] - difference[0]
        adder = difference[0]-multiplier
        if multiplier>-1:
            if adder>-1:
                nthTerm = "The nth term is %sn^2+%sn+%s"%(float(multiplySquare),float(multiplier),float(adder))
            else:
                nthTerm = "The nth term is %sn^2+%sn%s"%(float(multiplySquare),float(multiplier),float(adder))
        else:
            if adder>-1:
                nthTerm = "The nth term is %sn^2%sn+%s"%(float(multiplySquare),float(multiplier),float(adder))
            else:
                nthTerm = "The nth term is %sn^2%sn%s"%(float(multiplySquare),float(multiplier),float(adder))
        return nthTerm
print(nth())