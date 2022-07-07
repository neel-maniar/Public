user_input = [int(x) for x in input("Enter your sequence!").split(",")]
newList=[]
history = []
counter = 0
while counter<1000 and sum(user_input) != 0 and str(user_input) not in history[:len(history)-1]:
    for x in range(len(user_input)):
        if x+1<len(user_input):
            newList.append(abs(user_input[x]-user_input[x+1]))
        else:
            newList.append(abs(user_input[x]-user_input[0]))
    print(newList)
    user_input = newList
    history.append(str(newList))
    newList = []
    counter += 1
print ("%s steps" % (counter+1))