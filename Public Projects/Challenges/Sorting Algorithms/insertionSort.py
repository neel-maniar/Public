print("Enter a list of numbers, parsed by a space. Press enter when you are done.")
userInput=input()
current=""
userList=[]
for i in userInput:
    if i==" ":
        userList.append(int(current))
        current=""
    else:
        current=current + i
if userInput[-1]!=" ":
    userList.append(int(current))
    current=""

sortedList=[userList[0]]
for i in userList[1:]:
    j=0
    while i>sortedList[j]:  
        j+=1
        if j>=len(sortedList):
            break
    sortedList.insert(j,i) 
print(sortedList)