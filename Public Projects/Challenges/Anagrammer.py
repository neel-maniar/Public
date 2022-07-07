import string #Import the string dictionary so that alphabet can be inputted easily.
x=open("enable1.txt","r") #opens the file in the "read" mode, saving it to variable x.
enable1 = x.read() #enable1 is a string of all of the words in enable1.
enable1=enable1.split("\n") #creates a list, separating the words into a list, by each new line.
d = {}
e = {}
inpuT = ""

for a in string.ascii_lowercase: #For each character in the string ascii_lowercase, each character is added 
    d.update({a:0}) #to the dictionary d, in the format {a:0, b:0, etc}

e = d.copy()#create two more identical dictionaries
f = e.copy()
print("Enter 'break' to exit game")#how to stop the anagrammer
while inpuT!="break": #the while loop only runs as long as break isn't entered
    answer = []
    inpuT = input("Enter the scrambled word ")
    for i in inpuT:#adds 1 to each letter in the dictionary for each letter in the input.
        d.update({i:d[i]+1})
    for i in enable1: #Iterates through the list of words.
        for j in i: # the f dictionary is for the word in the enable1 list.
            f.update({j:f[j]+1})
        if f==d: #if the dictionaries are identical, the word in the enable1 list is added to answer.
            answer.append(i)
        f=e.copy() #clears d
    print(answer) #outputs the answer
    d=e.copy() #clears d
x.close() #closes the file at the end of the program
