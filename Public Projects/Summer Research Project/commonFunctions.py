import re
import bz2
import os
import requests
def getDataList(plating,culture,div):
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
    return([[float(line.split()[0]),int(line.split()[1])] for line in data.splitlines()])


def numToCoord(num):
    rows=[6, 7, 5, 4, 7, 6, 7, 5, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 2, 0, 1, 0, 3, 2, 0, 1, 1, 0, 2, 3, 0, 1, 0, 2, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 5, 7, 6, 7, 4, 5, 7, 6, 0, 0, 7, 7, -1]
    cols=[3, 3, 3, 3, 2, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 1, 2, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 5, 6, 7, 6, 7, 5, 6, 7, 7, 6, 5, 7, 6, 7, 6, 5, 6, 5, 5, 4, 4, 4, 4, 0, 7, 0, 7, -1]
    return([rows[ num ],cols[ num ]])

def coordToNum(r,c):
    conv = [ 60, 20, 18, 15, 14, 11, 9, 62, -1, -1, 23, 21, 19, 16, 13, 10, 8, 6, -1, -1, 25, 24, 22, 17, 12, 7, 5, 4, -1, -1, 28, 29, 27, 26, 3, 2, 0, 1, -1, -1, 31, 30, 32, 33, 56, 57, 59, 58, -1, -1, 34, 35, 37, 42, 47, 52, 54, 55, -1, -1, 36, 38, 40, 43, 46, 49, 51, 53, -1, -1, 61, 39, 41, 44, 45, 48, 50, 63, -1, -1 ]
    return(conv[10*c+r])

def texMaker(plating,culture,div,version):
    # Making a tex file to make the pdf
    changeMatrix=[[0 for i in range(8)] for j in range(8)]

    for i in range(64):
        changeMatrix[numToCoord(i)[0]][numToCoord(i)[1]]=i

    dirname = os.path.dirname(__file__)
    path = f"{dirname}/Week 3 (Heatmaps)/tex/heatmapTex{version}_{plating}_{culture}_{div}.tex"
    file=open(path, "a")
    file.write(
    r'''\documentclass{standalone}
\usepackage{graphicx}
\graphicspath{{./Heatmapfigs}}
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
                file.write(f"\includegraphics[width=.18\linewidth,height=.15\linewidth]{{Heatmap{version}_{plating}_{culture}_{div}_{changeMatrix[i][j]}.eps}} ")
            elif j==7:
                file.write(" ")
            else:
                file.write(f"\includegraphics[width=.18\linewidth,height=.15\linewidth]{{Heatmap{version}_{plating}_{culture}_{div}_{changeMatrix[i][j]}.eps}} & ")
        if i!=7:
            file.write("\\\\\n")

    file.write(
        r'''
\end{tabular}
\end{document}
        '''
    )
    file.close()