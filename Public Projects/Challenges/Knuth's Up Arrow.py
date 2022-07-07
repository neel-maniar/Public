"""def combine(b,e,n):
    new=e
    for x in range(n):
        new = b**new
    return new
print(combine(2,4,1))"""

def combine(b,e,n):
    if n == 1:
        return (b**e)
    newb=b
    for x in range(e-1):
        newb = combine(b,newb,n-1)
    return newb
print(combine(2,3,3))

