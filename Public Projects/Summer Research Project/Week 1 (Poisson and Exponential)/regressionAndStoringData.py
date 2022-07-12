from math import log
from scipy.stats import linregress
import matplotlib.pyplot as plt
timeIntervalList=[0.01,0.05,0.1,0.2,0.5,1,2,3,4,5,6,7,8,10,20,50,100,200,300,500,1000]
### DIV 4
## All Channels
# cvListAll=[2.8657302627623693,1.2719767968561546,0.904235145332319,0.6787633578580022,0.4748883639288479, 0.37153810453166675, 0.29799969233034757, 0.2705621766754984, 0.255348591940763, 0.24431146317620145, 0.2429015829375028, 0.2349738648969342, 0.23402996569322154, 0.22887122167097154,0.21324492806233608,0.2256801223961945, 0.2613832681288978, 0.20653767276729346,0.385004756924808,0.2662906699206589, 0.025211668871361146]  
# timeIntervalListTruncAll=timeIntervalList[:-3]
# cvListTruncAll=cvListAll[:-3]
## Channel 49
# cvList49=[26.957403606784364, 12.08751301726234, 8.51802059857181, 6.014340137283478, 3.8281594590154246, 2.7591765581609162, 1.933492999271456, 1.5646342893549754, 1.360141076252294, 1.2092752253654173, 1.106242958237548, 1.0542688797560935, 0.9505981305694015, 0.8703153054842362, 0.6105125705202891, 0.3542034337148495, 0.2960553226749692, 0.22518524974374585, 0.36305253798137915, 0.25987269756287523, 0.14782502241793033]
# timeIntervalListTrunc49=timeIntervalList[:-6]
# cvListTrunc49=cvList49[:-6]
# logTime=[log(i) for i in timeIntervalListTruncAll]
# logcv=[log(i) for i in cvListTruncAll] 


### DIV 25
## 49
cvList49=[8.44125289865985, 7.743909194786778, 7.376435508923703, 6.537648491436713, 4.603583938212427, 3.4238837980554138, 2.472365771789091, 2.0519004620476125, 1.745339996998628, 1.549040662004584, 1.37539410846223, 1.25596489526315, 1.144686481966751, 0.9693283416411905, 0.5904500893345843, 0.4080987144698418, 0.2819471319687429, 0.16526955326607223, 0.34818547133691974, 0.304313465918987, 0.2114139365887799]
# timeIntervalListTrunc49=timeIntervalList[2:-3]
# cvListTrunc49=cvList49[2:-3]

## All Channels
# 1000, 500, 300, 200, 100, 50, 20, 10, 8, 7, 6, 5, 4, 3 (backward) 
cvListAll=[10.386768317841995, 10.074308933607298, 9.48935118020666, 8.213558553903868, 5.677277317614066, 4.156994621906872, 2.9555159083412206, 2.40215985953031, 2.0201685043579785, 1.763697606629068, 1.5794346661893868, 1.415043425770129, 1.2901641651718292, 1.0825027245347392, 0.6513216877590741, 0.43366422300376734, 0.2926577828835096, 0.17322787532794676, 0.3504311058839833, 0.3136923919946656,0.21118851657764529]

logTime=[log(i) for i in timeIntervalList] 
logcv=[log(i) for i in cvListAll]
print(linregress(logTime[2:-3], logcv[2:-3]))
# plt.scatter(logTime,logcv)
# plt.xlabel("log(Delta)")
# plt.ylabel("log(C_v)")
# plt.title("Culture 1-3, Div 25, Channel 49")
# plt.savefig('C:/Users/Neel/OneDrive/Documents/Summer Research Project/Figures/Scatter4.eps', format='eps')
# plt.show()