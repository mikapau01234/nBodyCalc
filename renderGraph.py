

#importing stuffs
print("importing thingies")
import os
import matplotlib.pyplot as plt

#file params
mainDir = os.path.dirname(__file__)
posHistoryPath = os.path.join(mainDir, "posHistory")

p0=[]
p1=[]
p2=[]
p3=[]


p=(p0,p1,p2,p3)



def readfromfile(file):
    with open(str(file)) as file:
        out = file.readlines()
        print(f"out: {out}")
    return(out)



for x in p:
    index = eval("p"+str(p.index(x)))
    for file in os.listdir(os.path.join(posHistoryPath,str(p.index(x)))):
        index=readfromfile(os.path.join(posHistoryPath,str(p.index(x)),file))
    print(f"planet: {index}")
print(p0)

input("press RETURN to finish")