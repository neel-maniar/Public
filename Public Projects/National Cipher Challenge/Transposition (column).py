import string
import math
ciph="kdIgb oimce idkot seeii huotn pteho mmswi heeoa taoue taebw niInc fnkll flnho unwtd mamtg maera ieanw ronko tsstn kemta rahdn heIpo nsiac oiaeh lntai lbhsh oesoh lhtka rttts aehhI vldTh tunau ehshe noceI aireh rvsrw thett tuaea eseid eeeem topeh eohfB eoodn pafto enect dvasi bpsti xtrrp hfost wiekh Idnpb chrls fidoa atwit urgsd nedao hhgsh iaoeo ricot sgnrg ktedr hanoh tsmao Tehtf morsi ngkhe phtat bmrtt ooeap ctdJt marcs eedad bnier nrhhm rkshg eodBf emahf oeocr ctdfc tvMsy rlneu ooklu nobks nnhhe snosd naenu ueknh noydd Isiwl hseei uibby hatdo ybaeo pAntT sftek atpwa neuoo plttt abtte etioh mrhuh cfsto aeaip otiVc olsgI asstt atyla oodsu ebple rlecs acles hsham ierth ocoen etatn eluhn ehtnw auaih eerje hsaea kshtw cslrh eohin euteI ldelo trele aiutm mesrr oleet setwi naerw aouhe aiawy dycsu tltgu eecni atdte whiks ldlre uoaeg iivsn noleI atorn uscen heuaa tcplr dwato Imath eengb rafal bhade phdgh tgees eniat chdsa dmept oiiku ceuii ereyd ttsun cetTs oieeg naetn sligi tepod legtI oiors rhaaf hgpuc doite tdplh nlell irhpo Scrie eerTo wahto roesi efedu eoanb ahwae Vnnkt oueaS cober seeht rseha rtsda ntmia ahute ebhmI lbnot eyatt ndnht uHoht leade osytl ylwut uoIoa cwmll eints eIoeu retlu ekycb Iuime fnhmi orehv piafe ostto rnhoi lsnne alacn fndof eIhhi cttrh hhltf teipd rTnes ethtp bwenr rpksr mmein tiioa loamr achti deeuw lanse pohhi lidtk achce ynaoh oswum tlond eelaa dmiLd hhrii rhhue tettv eycet aceeo syIhr tcdan orcuo iwvlt wtror Ibdbt ebgal iulrt bduns nswva talsn gfois dytvd tadlk lniwh etcsi kasle yrtda inmen eeacd nluIa hotga ityet erbyt crebc hsead nuIop nolwy daoek iceuw iauan otdaa efood ddhnh octle itehd rfbls adfeo cemla kMkeh Aaiai tmhet udren tiate tuacy adsso eHlai inald oahhA tluwe errre iysta aihko lhymh lelos strmi rnadt asbde dpwdn ennet ttuol wlhni vtoew tidtn ceoeo cfhno rtorh errdt oepmc ceacl heeil eeagn wydnm heaew dnece hngpe tietw wumnp oanee ihitt gsalt hgrhc evett anaaa rtrnl sdenc uagcc dktdo uloyt aucth otnse eaard tdvdr siafn smuey hceha asnke oeett acitn ktnfd nidto dvdee eaone fifim elahr ohnao iweii aatgd sldeI iweuo sncle etrea eaaea oarrt csdal nweet lehwr xeaue eefno ggatt idctt kinet htuss hnctt netot eoanc wrhts rutee ooanh oeehe dlnny tdwed feapw cpdet hnmab ngtyr atnbc anmpl feiet hhdtn obeio asmmn uotio rapre yider rmtbh anlhf timtl klhHa rnobs motfc eefna actfb feerc ysetr ktiAt bwtsf fawod ewyed nyvmm teela idnhn eunae Utnot vtnic hlwpa laato Ilrot stsdk aurrh ianre oroef sepho loyko ltkei rytoi mtoth hIgei rtboi tttre oehde n"
cipher=""
key=262
alpha=[i for i in string.ascii_letters]
plaintext=""
for i in ciph:
    if i in alpha:
        cipher+=i
print(cipher)
print(len(cipher))

plaintext=""
for i in range(0,key):
    count=i
    while count<len(cipher):
        plaintext+=cipher[count]
        count+=key
    #plaintext+="\n"
print(plaintext)
print(key)
key+=1