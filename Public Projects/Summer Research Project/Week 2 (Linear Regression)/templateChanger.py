import os
path=r"C:\Users\Neel\My Python Coding\Public\Public Projects\Summer Research Project\Week 2 (Linear Regression)\template.txt"
newPath = path.replace(os.sep, '/')
f=open(newPath,"r")
k=f.read()
print(k)