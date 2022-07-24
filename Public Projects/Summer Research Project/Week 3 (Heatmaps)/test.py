import os

def numToCoord(num):
    rows=[6, 7, 5, 4, 7, 6, 7, 5, 6, 6, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 2, 0, 1, 0, 3, 2, 0, 1, 1, 0, 2, 3, 0, 1, 0, 2, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 5, 7, 6, 7, 4, 5, 7, 6, 0, 0, 7, 7, -1]
    cols=[3, 3, 3, 3, 2, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 1, 2, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 5, 6, 7, 6, 7, 5, 6, 7, 7, 6, 5, 7, 6, 7, 6, 5, 6, 5, 5, 4, 4, 4, 4, 0, 7, 0, 7, -1]
    return([rows[ num ],cols[ num ]])

plating=2
culture=2
div=14

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
\graphicspath{{./Figures/}}
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