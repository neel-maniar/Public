def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

numList=[233, 179, 109, 117, 31, 163, 89, 187, 191, 97]
for i in numList:
    if isPrime(i)==False:
        print(i)