plaintext = "WE ARE DISCOVERED. FLEE AT ONCE"
x = 9
y = 3

def capAlpha(plaintext):
    return ("".join(x.upper() for x in plaintext if x.isalpha()==True))

def matrix(plaintext,x,y):
    cap = capAlpha(plaintext)
    cap+="X"*(x*y-len(cap))
    a = []
    for i in range(y):
        a.append(cap[x*i:x*(i+1)])
    return a[1][1]

def encipher():
    return matrix(plaintext,x,y)

print(encipher())
    






