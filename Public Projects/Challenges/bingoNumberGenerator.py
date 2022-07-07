import random
numberList=[]
while len(numberList)<90:
    currentNumber=random.randint(1,90)
    if currentNumber not in numberList:
        numberList.append(currentNumber)

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *

root = Tk()
#random_number = random.randint(0,16777215)
#hex_number = str(hex(random_number))
#hex_number ='#'+ hex_number[2:]

var = StringVar()
label = Label(root, textvariable = var, font = ("Courier",300), fg="#123456") #relief = RAISED

counter=0
display=""

def answer():
    global counter
    global var
    global label

    var.set(numberList[counter])
    label.pack()
    #mb.showinfo("Next Number", numberList[counter])
    counter=counter+1


def callback():
    global display
    temp = numberList[0:counter]
    temp.sort()
    for i in range(0,counter):
        display+=" "+str(temp[i])
    mb.showinfo("Previous Numbers List", display)
    display=""

tk.Button(text='Next Number', font = ("Courier",30), fg="DarkGreen", bg="lightblue", command=answer).pack(fill=tk.X,ipadx=200,ipady=55,padx=10,pady=10)
tk.Button(text='Previous Numbers List', font = ("Courier",30), fg="Red", bg="lightblue",command=callback).pack(fill=tk.X,ipadx=200,ipady=55,padx=10,pady=10)

tk.mainloop()

