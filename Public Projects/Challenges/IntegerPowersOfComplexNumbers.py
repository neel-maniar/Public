import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def complexPower(complexNumber,power):
    x=complexNumber[0]
    y=complexNumber[1]
    real=0
    imaginary=0
    for i in range(power+1):
        if i%4==0:
            real+=ncr(power,i)*x**(power-i)*y**i
        if i%4==1:
            imaginary+=ncr(power,i)*x**(power-i)*y**i
        if i%4==2:
            real+=-ncr(power,i)*x**(power-i)*y**i
        if i%4==3:
            imaginary+=-ncr(power,i)*x**(power-i)*y**i
    return [real,imaginary]



