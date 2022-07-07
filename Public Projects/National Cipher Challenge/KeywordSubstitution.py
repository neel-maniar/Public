import string
import operator

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

def backwards(cipher):
    myList=[i for i in cipher[::-1]]
    ciph=""
    for i in myList:
        ciph+=i
    cipher=ciph
    return cipher

cipher="XLLDY DXLLM IQXLF WHLTQ VXEEG CKKIP VZFOT MAYYD RGFYY DLRBQ PVIQH FTUVM PIKOY LBNEY GJECN SRMBA VBXYA NESHJ HBKYS DTMLO ZGZFC SAYBH JYFLB EIYAR XHKXI ETLLY SQYCP VXLXH RWVCI HFSXQ XOHXE IEUSO LRXFK DIQHN JZEFK YGNRY LHZKK JTCIY XGKLV DRYBM JEVCG CDBIB GOFDI NHBVG IRTNJ XEKHN KYIFM IKUGY UUZXS BXWRW KLBXR BXWUY DSXCF UJOLR MUJOX SHLVN EPMHR ORYKL VDMBX GVRXD HFFBX LHWIE SEGCK XIKXW JEVNR WESEE RUDOA RTBKC VSHGL BHPTY YOZYA CUXEQ XCKSR SMLFZ TMZHZ NEPMH ZRGGK YSVPG PSEKQ PXAES VYTTR LGGMU DYPNB XVRXD HYIOL NLIDD EBXCQ XIPYY YDIQK OFMJM LLVGS NKIAK QCANE YQCAN YQYMK BKBEC UIKOV SLMVB TEGCI LRYVY NDEFM YGYLC ANESC RBFZL ERLHZ NIPNN IERCO UYCRY DFRLI FMMJY VATMK XIETS DCIGM LRZHL TMVDE RLLVV PYFMV RXLHM ZCYAH ZPWXS UQVSZ YXPRR IPNMD KMJEC NCVCP IGBSH TGVRX DHFCK WQXLX XSAXB KPSLK YTXSA XFGSG LBLGO LRLCU OZCBB TKIZM BXSQL HCKKG GYCEE WGANI OLRXB NNRYP IYPSL HCKCI SJYYD IJUCK KTKHW ESIPT YJOLR WHRCA CBPCK ZGKSE KQWKY MOVYX LVRXR TBKBI FMUID YZTYU SVYXF TKOAT FPOLR MUYDX MGMZD MEGCU KIJLC DCMRT BKCTY ALVZR MBNRM MDBHL OLRWU VVHJN IYCCR KUGRG GAQWY ECWCI KIJVI ENRYG QFBMC ANWYW LHCKS FKTFR MMRBF FZHLT FRBYR EOTNI GKUMR XGPXV NMTBX ESEKX LJOZJ XMDOL RLYKK XQGUB VEZXB KXSGM OCYWL TECKF YDYVC SFPYJ YLRWH RKMQL OIXMF MCNOM JWFLY LQKYN YTQMC WYWSV ICOLR MUYDI TXCCO FMAQV CSFMH VOARX VKSPN LSCZI CWMZD YZWYZ PMLNH VOFCO UYIPY MCUXE WGUDB IEMUY DCYPY DKWCA NESWC MUKCG GOUCC IFMYK SRSHN JWMYM HVWIT HGTSZ YEMEK TCANJ SWGKW VRXDH NLYCY PUVOW WTGVG ITXCC OFGGY YDRGE LVLXY TXEOK YXBKV SPMHF MRYVY NPMRV CCPRM VLVRX PNZDY VDXMF VSRXL FWKLB BKOQM LYMKL WXBKD EFMXV CMJTY IOZYA FCKHL TNEOR GMHFM IFMMJ YVATN GEVCR UDBEU MUYDX YXLYD KLBLV RXYZY YDICL IKXYE XVVFE FLLVG SNKIA KQCAN WYPJT MVFMJ GCKCS AKYNY PFVOD KXYWY VMGSL NYQMK RWRWS JICUP SQWIY DIKPY EBYMM UYDWG XJFRC KMMFM XYXLX DELXN WYHLT NYQYM UYIKK LBHES AFMLF GWCBL FDGGO FCKXY ANNOM TRGJS XGMOS DLENI ILRYX GPVIP NMKCY KBNRR XBBUJ NRYXG UOXAX LIYGC ALZKJ WTFGY XQBBK NMYLC EOLUG IZDYJ HMVBE PHZVZ SFHNE SKCUH RMMLB FIOFL BMJOV EGITQ RGWHV ZQGXB KDERA ALYFC UNYQM KXWRO TRTBK DGCIM FBTCA NYDMU RFCKR GYQFX RGANZ GWCBG VXIEG CKRKG YSXBI LXYCL EPXXZ CRMVX VNRCI RVOZY ACUXE JEUYO XGAQE SVYEO GYTWE FRCVC OCEER CXVKY RCOUY CHMAN VWCKL MVVIF MYEYR KXFSY VNAMZ UVSMY YDSRG IZDYJ HMEGS PNIKX IQXLG YXQKY NYTEG CUKIJ KYYDS FMCNO XYBNF QILHN ESKCU IKOPZ TYIOA CPXEY GCLXE KWCBG VXIPN IWYWC VCMBI QVCKK QMEJZ NIFMH ZRXGP EIYAR XHKXI ETLLY TMEYM OHMMY CLECK YNOAR LLZPW EGCYD SUMXV FIGAW RIEJX XJSLR MUYDJ JXMPW XPHZD YGGWH ROPZT NZFIL BYYDC YEYUY XBXEI YAQXC CVECA NXXSK THFSW SYHFM KLBQF CJMRA VDEPM MIESL HCKEP MLFRX SGMUE BIRGC EKSRX FSKRC FUVLS RZHZB ECIJR OPGAQ EYMRB MFZLQ BNZBF CANXX MQBFR XMEKU DIPCO CKMID YYUXE YBLKC YYWHR IRYFL VQRGL YZVPY KYYRX GPHFS XATLF PXPHJ GEWEG CUVMS USCDG CYLVZ HLTBI OLBXS RVTQT BRSWQ NLUOV YXZVG XYANC VELXY SCEFK UNRWG DLLDS QLOIO LR".upper()
#cipher=backwards(cipher)
alpha = [i for i in string.ascii_uppercase]

dictionary={}
for i in string.ascii_uppercase:
  dictionary.update({i:0})

for i in cipher:
  if i in dictionary:
    dictionary[i]+=1

frequency="ETAOINSHRDLCUMWFGYPBVKJXQZ"
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

def findRepeats(ciph):
    newciph=""
    alpha=[i for i in string.ascii_uppercase]
    for i in ciph:
        if i in alpha:
            newciph+=i
    ciph=newciph
    repeat={}
    repList=[]
    for n in range(3,4):
        for i in range(0,len(ciph)-n+1):
            currentGroup=ciph[i:i+n]
            repList.append(currentGroup)
            if currentGroup not in repeat:
                repeat.update({currentGroup:1})
            else:
                repeat.update({currentGroup:repeat[currentGroup]+1})
    repeatx={}
    for i in repeat:
        if repeat[i]>6:
            repeatx.update({i:repeat[i]})
    repeat=repeatx.copy()
    sorted_x = sorted(repeat.items(),key=operator.itemgetter(1),reverse=True,)
    return sorted_x

print(findRepeats(cipher))
frequ=['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

plain=""
for i in cipher:
    if i in order:
        plain+=frequency[order.index(i)]
        plain+=" "
frequencyList=[]
for i in frequency:
    frequencyList.append(i)
print(plain)
print(order)