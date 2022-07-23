import copy
dataList=[
    [1,1],
    [2,2],
    [3,3],
    [4,1],
    [5,2],
    [6,3],
    [7,1],
    [8,2],
    [9,3]
]
for masterChannel in range(60):
    print(f"{masterChannel}/59")
    timeListMasterChannel=[[index,row[0]] for index,row in enumerate(dataList) if row[1] == masterChannel]
    timeIntervals=[[] for i in range(60)]
    checkChannel=[i for i in range(60)]
    for index,masterTime in timeListMasterChannel:
        AppendedYet=[False for i in range(60)]
        DoneFlag=False
        count=index+1
        while count<len(dataList) and DoneFlag==False:
            data=dataList[count]
            channel=data[1]
            t=data[0]
            if AppendedYet[channel]==False:
                timeIntervals[channel].append(t-masterTime)
                AppendedYet[channel]=True
            DoneFlag=all([AppendedYet[i] for i in checkChannel])
            print([AppendedYet[i] for i in checkChannel])
            count+=1
        checkChannelCopy=copy.deepcopy(checkChannel)
        for channel in checkChannelCopy:
            if AppendedYet[channel]==False:
                checkChannel.remove(channel)
        print("lo")
    print(timeIntervals)    