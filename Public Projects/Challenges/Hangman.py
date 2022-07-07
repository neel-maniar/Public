import math
lives = int(input("How many lives?"))
comp=str(input("Enter the string: "))
comp=comp.lower()
new=["*"]*len(comp)
token=0
history=[]
print("\n"*70)
print(new)
while True:
    usr=str(input("Enter: "))
    if usr not in history:
        for x in range(0,len(comp)):
            if comp[x]==usr:
                new[x]=usr
            else:
                token+=1
        print(new)
        if token==len(comp):
            lives-=1
        token=0
        history.append(usr)
        print("You have %s lives left" % (lives))
        if "*" not in new or lives==0:
            break
    else:
        print("You have already used",usr)
if "*" not in new:
    print("Well done")
else:
    print("Unlucky")
    print("The word was", comp)

