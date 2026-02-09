

#importing stuffs
print("importing thingies")
import os
import matplotlib.pyplot as plt

#file params
mainDir = os.path.dirname(__file__)
posHistoryPath = os.path.join(mainDir, "posHistory")

class classPlanet:
    def __init__(self, number):
        self.historyPosY= []
        self.historyPosX= []
        self.number = number

p0 = classPlanet(0)
p1 = classPlanet(1)
p2 = classPlanet(2)
p3 = classPlanet(3)



p=(p0,p1,p2,p3)


def readfromfile(file):
    with open(str(file)) as file:
        out = file.read
        file.close()
    return(out)


for planet in p:
    posLogPath = os.path.join(posHistoryPath, str(planet.number))
    logs = os.listdir(posLogPath)
    print(f"logs: {logs}")

    for log in logs:
        cordList = readfromfile(os.path.join(posLogPath, log))
        print(repr(cordList))
        for cordCouple in cordList:
            planet.historyPosX = cordCouple[0]
            planet.historyPosY = cordCouple[1]


'''
for x in p:
    print(vars(x))
#decide plot size
plt.xlim(-10000, 10000)
plt.ylim(-10000, 10000)
#plot stuff
plt.plot(p0.historyPosX,p0.historyPosY,"b",p1.historyPosX,p1.historyPosY,"r",p2.historyPosX,p2.historyPosY,"k",p3.historyPosX,p3.historyPosY,"m",)


#show plot
plt.show()
'''