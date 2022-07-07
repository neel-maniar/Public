### GRRR Simplex tableaus stupid
import numpy as np
import copy

## Alternative way to input matrix
def initialiseMatrix():
    print("Enter your numbers rowwise: ")
    matrix=[]
    for i in range(R):
        a=[]
        for j in range(C):
            aInput=float( input("Enter number: ") )
            a.append(aInput)
        matrix.append(a)
    return(matrix)
#matrix=initialiseMatrix()

##Can just type in initial matrix
matrix=[[0,-1,-1,0,0],
        [1,1,4,1,0],
        [1,3,2,0,1]]
R=len(matrix)
C=len( matrix[0] )

## Main loop
while True:
    # check for c_j<0
    potentialColumn=[]
    for i in range(1,C):
        if matrix[0][i]<0:
            potentialColumn.append(i)

    # Gives user choice of j if there are multiple possible j    
    if len(potentialColumn)>1:
        print("Which j would you like to choose out of: ",potentialColumn)
        choosej=int( input() )
    if len(potentialColumn)==1:
        choosej=potentialColumn[0]
    if len(potentialColumn)==0:
        print("solution is optimal")
        break

    # Finds the smallest x_B/u_i, for positive u_i
    xOverU=-1
    potentialRow=[]
    for i in range(1,R):
        xOverUcontender=matrix[i][0]/matrix[i][choosej]
        if matrix[i][choosej]>0:
            if xOverU==-1:
                xOverU=xOverUcontender
                potentialRow.append(i)
            elif xOverU!=-1 and xOverUcontender<xOverU:
                potentialRow=[i]
                xOverU=xOverUcontender
            elif xOverU!=-1 and xOverUcontender==xOverU:
                potentialRow.append(i)

    # Gives user a choice of l    
    if len(potentialRow)>1:
        print("Which row would you like to choose out of: ",potentialRow)
        chooseRow=int( input() )
    if len(potentialRow)==1:
        chooseRow=potentialRow[0]
    if len(potentialRow)==0:
        print("The minimal cost is infinite")
        print(matrix)
        break

    #Finds out what to multiply each row by.
    multipliersList=[]
    for i in range(R):
        if i!=chooseRow:
            multipliersList.append(-matrix[i][choosej]/matrix[chooseRow][choosej])
        if i==chooseRow:
            multipliersList.append(1/matrix[i][choosej])

    # Executes multiplication
    for i in range(R):
        for j in range(C):
            if i!=chooseRow:
                matrix[i][j]+=matrix[chooseRow][j]*multipliersList[i]
    for j in range(C):
        matrix[chooseRow][j]*=multipliersList[chooseRow]

    print()

    # Displays multipliers
    print(np.round_(np.matrix(multipliersList),4))

    # Displays (j,l)
    print("j =",choosej," l =",chooseRow)
    
    # Displays new tableau
    matrixDisplay=copy.deepcopy(matrix)
    matrixDisplay=np.matrix(matrixDisplay)
    matrixDisplay=np.round_(matrixDisplay,4)
    print(matrixDisplay)