import numpy as np
import pandas as pd
num1Und=[0 for i in range(60)]
channelTimeInterval=[1,1,2,3,4,1,2,1,1]
pandating=pd.Series(channelTimeInterval)
freq=pandating.value_counts()
for i in range(60):
    if i in freq:
        if (freq[i])<=1:
            num1Und[i]+=1
    else:
        num1Und[i]+=1

print(num1Und)