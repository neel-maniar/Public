def Fibonacci(n):
    sequence = [1,1]
    for x in range(n-2):
        new = sequence[x]+sequence[x+1]
        sequence.append(new)
    return sequence

print(Fibonacci(3))