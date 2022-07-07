f= open("enable1.txt","r")
x = f.read()
z = x.split("\n")
f.close()
def check(word):
    count=0
    for x in word:
        if "ei" in x and "cei" not in x or "cie" in x:
            count+=1
    return count

print(check(z))