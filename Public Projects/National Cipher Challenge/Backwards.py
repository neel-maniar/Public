def backwards(cipher):
    cipher="ABC ".upper()
    myList=[i for i in cipher[::-1]]
    ciph=""
    for i in myList:
        ciph+=i
    cipher=ciph
    return cipher