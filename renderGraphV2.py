import matplotlib.colors

#importing stuffs
print("importing thingies")
import os
import matplotlib.pyplot as plt
import csv

#file params
mainDir = os.path.dirname(__file__)


cycleList=[]
colourList=[]

class classPlanet:
    def __init__(self, number):
        self.historyPosY= []
        self.historyPosX= []
        self.number = number

with open("output.csv", "r") as outputCSV:
    data = csv.reader(outputCSV)
    for row in data:
        row = row[0].split(";")
        cycleList.append(row)
print(cycleList)

#get planet amount, Dontnut :D 🍩
planetAmount = (len(cycleList[0])-1)/4
print(f"planetAmount: {planetAmount}")

#convert coordinate format from list of ticks with planets to list of planets with ticks
counter=0
planetList=[]
while counter < planetAmount:
    planetList.append(classPlanet(counter))
    #get all positions
    historyPosX = []
    historyPosY = []
    planetColumnNumber = (counter)*4 + 1
    for row in cycleList[1:]:
        historyPosX.append(float(row[planetColumnNumber]))
        historyPosY.append(float(row[planetColumnNumber+1]))
    planetList[counter].historyPosX = historyPosX
    planetList[counter].historyPosY = historyPosY
    counter=counter+1

for planet in planetList:
    print(f"planetNumber: {planet.number}")
    print(f"posXHis: {planet.historyPosX}")
    print(f"posYHis: {planet.historyPosY}")



#decide plot size
#plt.xlim(-500000, 500000)
#plt.ylim(-500000, 500000)

for colour in matplotlib.colors.BASE_COLORS:
    colourList.append(colour)
colourList.remove("w")
for colourNr, planet in enumerate(planetList):
    plt.plot(planet.historyPosX,planet.historyPosY,colourList[colourNr],marker=".", markevery=[-1])
#show plot
plt.show()
