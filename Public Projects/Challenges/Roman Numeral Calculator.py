#numeralDict is a dictionary which holds the value of each letter.
numeralDict={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

#repeatDict stores the minimum number of times a letter is repeated for the numeral to be invalid.
repeatDict={
    "I":5,
    "V":2,
    "X":5,
    "L":2,
    "C":5,
    "D":2    
}

#The order function returns True if the letters are in descending numerical order.
def order(inp):
    inpList = inp.split(".") #I have split the code into a list, separated by the decimal point          
    
    #Here I iterate through the integer, and then the decimal separately.
    for numeral in inpList:
        for i in range(1,len(numeral)):
            if numeralDict[numeral[i]]>numeralDict[numeral[i-1]]: #The reference to numeralDict is there to find the value of the numeral.
                return False #If at any point the number is larger than the previous one, the function stops and returns False.
    return True

def convertToArabic(inp):
    inpList = inp.split(".")
    #Similar to the order function, I split the input into the integer and decimal, this time assigning each to a variable.
    integer=inpList[0]
    if "." in inp:
        decimal=inpList[1]
    else:
        decimal=""
    total=0
    decimaltotal=0
    for i in range(0,len(integer)):
        total+=numeralDict[integer[i]] #This adds the numerals in the integer up.
    for i in range(0,len(decimal)):
        decimaltotal+=numeralDict[decimal[i]] #This adds the numerals in the decimals up.
    decimal=decimaltotal/10**len(str(decimaltotal)) #The decimal is divided by the correct power of ten in order to be the right value.
    total+=decimal
    return float(total) #It is then added to the integer total and returned (as a float, so that it does not cause datatypes to clash)

def convertToRoman(inp):
    Roman=""
    inpList = str(inp).split(".") #The input is split again.
    for number in inpList:
        number=int(number) #The input is a string, so the datatype needs to be changed for following calculations.
        for i in range(1,len(numeralDict)+1):
            LargestValue=list(numeralDict.values())[len(numeralDict)-i] #Iterates backwards through the values in the numeralDict.
            Quantity=(number//LargestValue)
            Letter=list(numeralDict.keys())[len(numeralDict)-i]
            Roman+=str(Letter)*Quantity #Adds the correct quantity of the appropriate letter.
            number-=LargestValue*Quantity 
        Roman+="." #Adds the decimal point before repeating the process with the decimal section.
    if int(inp)==float(inp):
        Roman=Roman[:-2] #If the input is a whole number, both of the final decimal points are taken away.
    else:
        Roman=Roman[:-1] #Even if it isn't, there is still a decimal point at the end which needs to be removed.
    return Roman

#Checks if any roman numerals have been repeated too many times.
def repeatCheck(inp):
    inpList=inp.split(".")
    for number in inpList:
        for i in repeatDict:
            if number.count(i)>=repeatDict[i]: #Counts the number of each letter in the input and compares with repeatDict.
                return False
    return True

def solveOrder(inp):
    inpList = inp.split(".") #I have split the code into a list, separated by the decimal point          
    numberList=[]
    sortedOrder=""
    #Here I iterate through the integer, and then the decimal separately.
    for numeral in inpList:
        for i in range(0,len(numeral)):
            numberList.append(numeralDict[numeral[i]]) #I make a list of all the values of each numeral,
        numberList.sort(reverse=True) #and sort it, 
        for i in numberList:
            sortedOrder+=(list(numeralDict.keys())[list(numeralDict.values()).index(i)])#and then convert these values back to numeral form.
        sortedOrder+="."
        numberList=[]
    sortedOrder=sortedOrder[:-1]
    return sortedOrder

#In the solveRepeat function, I essentially convert the roman numeral to arabic, and then convert it back.
def solveRepeat(inp):
    return convertToRoman(convertToArabic(inp)) 

#Function which combines previous functions to validate the user's numeral input
def validation(inp):
    while True: #Python's version of do until.
        ArabicInp = convertToArabic(inp)
        if ArabicInp<=4000: 
            if order(inp)!=True: #Informs the user and corrects issues to do with order
                print("The order of the Roman numeral is incorrect. Numerals need to be in descending order.")
                inp=solveOrder(inp)
                ArabicInp=convertToArabic(inp)
            if repeatCheck(inp)!=True: #Informs the user and corrects issues to do with unnecessary repeats
                print("Some of your numerals can be replaced by larger ones (e.g. VV is better written as X)")
                inp=solveRepeat(inp)
                ArabicInp=convertToArabic(inp)
            print(inp)
            print(ArabicInp)
            break
        else:
            print("Your numeral is above 4000.")
        inp=input("Please enter a valid roman numeral. ") #Error message is displayed before repeating the input.
    return(ArabicInp)

#Main Program
while True:
    num1=input("Enter first number: ")
    print(solveOrder(num1))
    ArabicNum1=validation(num1) #Arabic input stored for calculations.
    num2=input("Enter second number: ")
    ArabicNum2=validation(num2)

    operation=""
    while operation!="restart":
        operation=input("Enter operation (+ or -) ") #Asks user for operation.
        if operation=="+":
            break
        if operation =="-":
            if ArabicNum1-ArabicNum2>0:
                break
            elif ArabicNum1-ArabicNum2==0: #Ensures a zero answer is not returned, and notifies the user
                print("You have chosen to subtract and the resulting number is zero. Please enter a valid operation, or enter 'restart' to enter numbers again")
            else: #Ensures a negative answer is not returned, and notifies the user
                print("You have chosen to subtract and the resulting number is negative. Please enter a valid operation, or enter 'restart' to enter numbers again")
        elif operation != "restart":
            print("You did not enter '+' or '-'. Please enter a valid operation, or enter 'restart' to enter numbers again") #Ensures a valid operation is entered. User is notified if it isn't.
    if operation!="restart": #If restart is entered, the loop is repeated, allowing for the numerals to be inputted again.
        break

if operation=="+":
    answer=round(ArabicNum1+ArabicNum2,8) #Answer must be rounded, as python cannot store decimals exactly in binary point representation
    print(convertToRoman(answer)) #Roman numeral representation of answer printed
    print(answer) #Arabic number representation of answer printed
if operation=="-":
    answer=round(ArabicNum1-ArabicNum2,8) 
    print(convertToRoman(answer))
    print(answer)

