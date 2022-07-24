import re
import bz2
import os
from time import time
import requests
import numpy as np
import matplotlib.pyplot as plt
import statistics
from matplotlib.patches import Rectangle
import copy

# Measure how long the program takes to run
start_time = time()

# Parameters
plating=2
culture=2
divList=[4,35]

for div in divList:
    ## List of URLs for a particular day
    listsURL="https://neurodatasharing.bme.gatech.edu/development-data/html/wget/daily.spont.dense.text."+str(plating)+"."+str(culture)+".0.list"
    # Get it from the internet
    response = requests.get(listsURL)
    # Put it in a file
    dirname = os.path.dirname(__file__)
    path = dirname+"/listOfURLs"
    open(path, "wb").write(response.content)
    listOfURLs = [line.rstrip() for line in open(path)]
    listOfDivs=[]
    # Find the divs for which data is available, by regex
    for line in listOfURLs:
        match = re.search('(\d+)(?=\s*\.spk\.txt\.bz2)', line)
        if match:
            listOfDivs.append(int(match.group(1)))

    # Which div?
    try:
        listIndex=listOfDivs.index(div)
    except:
        print("There was no data recorded for plating "+str(plating)+", culture "+str(culture)+" on div "+str(div))
        quit()

    URL=listOfURLs[listIndex]
    ## Import Data from URL
    response = requests.get(URL)
    dirname = os.path.dirname(__file__)
    path = dirname+"\\testbz2"
    newPath = path.replace(os.sep, '/')
    open(newPath, "wb").write(response.content)

    ## Process data by reading it off as a string and converting to list
    bz_file = bz2.BZ2File(newPath)
    data = bz_file.read().decode('ascii')
    dataList = [[float(line.split()[0]),int(line.split()[1])] for line in data.splitlines()]
    for masterChannel in range(60):
        print(f"{masterChannel}/59")
        timeListMasterChannel=[[index,row[0]] for index,row in enumerate(dataList) if row[1] == masterChannel]
        timeIntervals=[[] for i in range(60)]
        checkChannel=[i for i in range(60)]
        for index,masterTime in timeListMasterChannel:
            tic=time()
            AppendedYet=[False for i in range(60)]
            DoneFlag=False
            count=index+1
            while count<len(dataList) and DoneFlag==False:
                data=dataList[count]
                channel=data[1]
                t=data[0]
                if AppendedYet[channel]==False:
                    timeIntervals[channel].append(t-masterTime)
                    AppendedYet[channel]=True
                DoneFlag=all([AppendedYet[i] for i in checkChannel])
                count+=1
            checkChannelCopy=copy.deepcopy(checkChannel)
            for channel in checkChannelCopy:
                if AppendedYet[channel]==False:
                    checkChannel.remove(channel)
            # print(f"{index}/{timeListMasterChannel[-1]} took ----- {time()-tic} ----- seconds to run")
        
        def numToCoord(num):
            rows=[6, 7, 5, 4, 7, 6, 7, 5, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 2, 0, 1, 0, 3, 2, 0, 1, 1, 0, 2, 3, 0, 1, 0, 2, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 5, 7, 6, 7, 4, 5, 7, 6, 0, 0, 7, 7, -1]
            cols=[3, 3, 3, 3, 2, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 1, 2, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 5, 6, 7, 6, 7, 5, 6, 7, 7, 6, 5, 7, 6, 7, 6, 5, 6, 5, 5, 4, 4, 4, 4, 0, 7, 0, 7, -1]
            return([rows[ num ],cols[ num ]])
        cvListCoord=np.array([[-100.0 for i in range(8)] for j in range(8)])
        numData=[[0 for i in range(8)] for j in range(8)]
        for index,value in enumerate(timeIntervals):
            x=numToCoord(index)[1]
            y=numToCoord(index)[0]
            if len(value)>1:
                exp=statistics.mean(value)
                var=statistics.variance(value)
                cv=(var/exp**2)**0.5
                cvListCoord[y][x]=cv
            numData[y][x]=str(len(value))
        mask=np.zeros_like(cvListCoord)
        mask[cvListCoord==-100]=True
        numData=np.array(numData)
        count=0
        for entry in dataList:
            if entry[1]==14:
                count+=1
        # Plot Heatmap
        import numpy as np; np.random.seed(0)
        import seaborn as sns; sns.set_theme()
        uniform_data = np.array(cvListCoord)
        ax = sns.heatmap(uniform_data,annot=cvListCoord,fmt='',vmin=0,vmax=2,mask=mask,robust=True)
        ax.set_title(f"Heat map of C_v of waiting times after master channel {masterChannel} in plating {plating}, culture {culture}, div {div}",wrap=True)
        position=(numToCoord(masterChannel)[1],numToCoord(masterChannel)[0])
        ax.add_patch(Rectangle(position, 1, 1, fill=False, edgecolor='blue', lw=3))
        dirname = os.path.dirname(__file__)
        plt.savefig(f'{dirname}/Heatmaps/Heatmap2_{plating}{culture}{div}{masterChannel}.eps', format='eps')
        plt.clf()
#     print(f"Figures produced for div {div}!")

    # Making a tex file to make the pdf
    changeMatrix=[[0 for i in range(8)] for j in range(8)]

    for i in range(64):
        changeMatrix[numToCoord(i)[0]][numToCoord(i)[1]]=i

    dirname = os.path.dirname(__file__)
    path = f"{dirname}/tex/heatmapTex2_{plating}{culture}{div}.tex"
    file=open(path, "a")
    file.write(
    r'''\documentclass{standalone}
\usepackage{graphicx}
\graphicspath{{../HeatMapFigs}}
\begin{document}
\renewcommand{\arraystretch}{0}
\setlength{\tabcolsep}{0pt}
\begin{tabular}{ *8{c} }
'''
    )

    for i in range(8):
        for j in range(8):
            if j==0 and (i==0 or i==7):
                file.write(" & ")
            elif j==7 and not (i==0 or i==7):
                file.write(f"\includegraphics[width=.18\linewidth,height=.15\linewidth]{{Heatmap2_{plating}{culture}{div}{changeMatrix[i][j]}.eps}} ")
            elif j==7:
                file.write(" ")
            else:
                file.write(f"\includegraphics[width=.18\linewidth,height=.15\linewidth]{{Heatmap2_{plating}{culture}{div}{changeMatrix[i][j]}.eps}} & ")
        if i!=7:
            file.write("\\\\\n")

    file.write(
        r'''
\end{tabular}
\end{document}
        '''
    )
    file.close()
print(f"{os.path.basename(__file__)} took ----- {time()-start_time} ----- seconds to run")