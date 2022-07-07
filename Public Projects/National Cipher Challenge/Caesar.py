import string

dictionary={}
for i in string.ascii_uppercase:
  dictionary.update({i:0})
shift=1
alpha = [i for i in string.ascii_uppercase]

cipher="ZPV BSF TBGF OPX".upper()

for i in cipher:
  if i in dictionary:
    dictionary[i]+=1

val=list(dictionary.values())
highest=val[0]
for i in range(1,len(val)):
    if val[i]>highest:
        highest=val[i]

frequency="ETAOINSHRDLCUMWFGYPBVKJXQZ"
satisfied=""
counter=0

while satisfied.lower()!="yes":

    shift=26-(list(dictionary.values()).index(highest)-list(dictionary.keys()).index(frequency[counter]))%26

    plain=""
    for i in cipher:
        if i in alpha:
            if alpha.index(i)+shift<26:
                plain+=alpha[alpha.index(i)+shift]
            else:
                plain+=alpha[alpha.index(i)-26+shift]
        else:
            plain+=" "
    print(plain)
    satisfied=input("\nAre you satisfied? ")

    counter+=1