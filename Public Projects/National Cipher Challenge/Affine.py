import string
cipher="FTNPTQP RDF TGOBTLFKX HPPQ IYDI B FYTLKM HQTR DGTLI MTLVKDF GKDJH GLI B RDF KPSI RTQMPCBQV RYDI YP YDM IT MT RBIY IYP FYDMTR DCJYBOP. B STLQM FTNP ICDJPF TS YBN BQ GTFITQ QPRFWDWPC JKBWWBQVF SCTN IYP WPCBTM. IYP FITCBPF FITWWPM BQ 1873, DCTLQM IYP MDIP TS IYP KPIIPCF GPIRPPQ OBJITCBD DQM FBC JYDCKPF, FT B DFFLNP YP CPILCQPM IT PQVKDQM IYPQ, GLI B JTLKMQ’I SBQM DQX CPJTCM TS YBN BQ IYP BNNBVCDIBTQ SBKPF DQM IYPCP RDF QTIYBQV BQ IYP TSSBJBDK CPJTCM IT FLVVPFI IYDI YP NPI RBIY FBC JYDCKPF, KPI DKTQP RBIY YPC NDEPFIX. IYP ICDBK YDM VTQP JTKM DQM B NBVYI YDOP NTOPM TQ DI IYDI WTBQI, GLI IYPQ B VTI IYP IYBCM PNDBK. IYBF IBNP BI RDF D HPXRTCM JBWYPC DQM BI ITTH D KBIIKP KTQVPC IT GCPDH, IYTLVY IYP RTCM FICLJILCP YPKWPM D KTI. BI JTQSBCNPM POPCXIYBQV B YDM VLPFFPM FT SDC DGTLI GKDJH, DQM CDBFPM D RYTKP KTDM TS QPR ZLPFIBTQF! BI DKFT FLVVPFIPM IYDI B NBVYI SBQM DQFRPCF BQ IYP FYDMTR DCJYBOP, GLI SBCFI B YDM IT SBVLCP TLI RYPCP BI RDF, DQM YTR B JTLKM VPI BQ. B FIBKK JDQ’I GPKBPOP BI, GLI IYP DQFRPC JDNP SCTN D VTTVKP FPDCJY. B RDF KTTHBQV STC D KTJDIBTQ IYDI RTLKM YDOP WCTOBMPM GKDJH RBIY JTOPC STC D FICPDN TS OBFBITCF, WCPSPCDGKX BQ D JPQICDK KTQMTQ KTJDIBTQ, DQM RBIY SDJBKBIBPF STC FPJLCP FITCDVP TS TSSBJBDK CPJTCMF, DQM BI FYTLKM YDOP GPPQ TWPQPM BQ 1873 TC 1874. B FPDCJYPM STC “GKDJH, KTQMTQ, 1874” DQM B KBHPM RYDI B STLQM. DQM IYDI BF RYX B STLQM NXFPKS KXBQV TQ IYP CTTS TS IYP QTCNDQ FYDR GLBKMBQVF BQ IYP NBMMKP TS IYP QBVYI DQM BQ WTLCBQV CDBQ! B YDM IT SBVLCP TLI D RDX TS VPIIBQV BQFBMP TQP TS IYP NTFI FPJLCP KTJDIBTQF BQ PQVKDQM!".upper()
frequency="ETAOINSHRDLCUMWFGYPBVKJXQZ"
inverseDict={
    1:1,
    3:9,
    5:21,
    7:15,
    9:3,
    11:19,
    15:7,
    17:23,
    19:11,
    21:5,
    23:17,
    25:25
}
def frequencyAnalysis(cipher):
    def BubbleSort(unSorted):
        token=0
        while True:
            for x in range(0,len(unSorted)):
                if x<len(unSorted)-1:
                    if unSorted[x]<unSorted[x+1]:
                        c=unSorted[x+1]
                        unSorted[x+1]=unSorted[x]
                        unSorted[x]=c
                    else:
                        token+=1
            if token==(len(unSorted))-1:
                break
            token=0
        return unSorted

    key=[]
    dictionary={}
    for i in string.ascii_uppercase:
        dictionary.update({i:0})

    for i in cipher:
        if i in dictionary:
            dictionary[i]+=1

    order=[]
    val=list(dictionary.values())
    sortedVal=BubbleSort(val)
    for i in range(0,26):
        key=list(dictionary.keys())[list(dictionary.values()).index(sortedVal[i])]
        value=sortedVal[i]
        if key not in order:
            order.append(key)
        else:
            del dictionary[key]
            order.append(list(dictionary.keys())[list(dictionary.values()).index(sortedVal[i])])
            dictionary.update({key:value})
    return order
order=frequencyAnalysis(cipher)
alpha=[i for i in string.ascii_uppercase]
multiplier1=alpha.index(frequency[0])
multiplier2=alpha.index(frequency[1])
rh1=alpha.index(order[0])
rh2=alpha.index(order[1])
if multiplier2>multiplier1:
    multiplier3=multiplier2-multiplier1
    rh3=(rh2-rh1)%26
else:
    multiplier3=multiplier1-multiplier2
    rh3=(rh1-rh2)%26
aprime=inverseDict[multiplier3]
a=(rh3*aprime)%26
b=rh1-(multiplier1*a)
key=[]
for i in range(0,26):
    key.append((a*i+b)%26)
plain=""
for i in cipher:
    if i in alpha:
        plain+=alpha[key.index(alpha.index(i))]
    else:
        plain+=i
print(plain)

