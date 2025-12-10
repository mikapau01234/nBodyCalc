from operator import truediv

print("start")

print("importing thingos")
from math import *
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

print("importing done")

#global system parameters
debugMode = False
#file params
mainDir = os.path.dirname(__file__)
posHistoryPath = os.path.join(mainDir, "posHistory")





#physical constants
#Gravity constant
G = 0.00000000006674

#classes
class classPlanet:
    def __init__(self, id, mass, posX, posY, velocityX, velocityY):
        self.id = id
        self.mass = mass
        self.posX = posX
        self.historyPosX = [posX]
        self.posY = posY
        self.historyPosY = [posY]
        self.velocityX = velocityX
        self.velocityY = velocityY

#define planets


p0 = classPlanet(0, 1000000, 0, 0, 0, 0)

p1 = classPlanet(1, 1, 5000, 0, 0, 0.0001)

p2 = classPlanet(2, 1, -5000, 0, 0, -0.00005)

p3 = classPlanet(3, 10, -2000, 6000, 0.001, -0.001)

#tupple of planets
p = (p0,p1,p2,p3)


#initiating file structure
print("initiating file structure")

if os.path.exists(posHistoryPath) == False:
    os.mkdir(posHistoryPath)

for planet in p:
    planetPath = os.path.join(mainDir, posHistoryPath, str(planet.id))
    if os.path.exists(planetPath) == False:
        os.mkdir(planetPath)
    else:
        shutil.rmtree(planetPath)
        os.mkdir(planetPath)







#def functions
#Calculate Fg
def gravityForce(p1,p2,G):
    deltaPosX = p1.posX - p2.posX
    deltaPosY = p1.posY - p2.posY
    
    r = sqrt(deltaPosX**2+deltaPosY**2)
    
    rVektor = (deltaPosX,deltaPosY)
    rUnitVektor = (rVektor[0]/r*-1,rVektor[1]/r*-1)

    Fg = ((G*p1.mass*p2.mass*rUnitVektor[0])/r**2,(G*p1.mass*p2.mass*rUnitVektor[1])/r**2)
    return(Fg)


def velocityStep(p,G):
    #calculate velocity change based on gravity
    #do for all things in planet list
    debugPrint("start velocityStep")
    for x in p:
        index = p.index(x)
        debugPrint(index)
        y=0
        debugPrint("current planet: "+str(index))
        #do for every other planet
        while y<len(p):
            if y!=index:
                #DO STUFF HERE WITH THE OTHER PLANETS
                FgTupple = gravityForce(x,p[y],G)
                debugPrint(FgTupple)
                x.velocityX = x.velocityX + FgTupple[0]
                x.velocityY = x.velocityY + FgTupple[1]
            else:
                debugPrint("skip planet ["+str(y)+"] Reason: same Planet")
            y=y+1
            debugPrint("step "+str(y))
        debugPrint("planet "+str(index)+" done")
    debugPrint("end velocityStep")
    return(p)


def positionStep(p):
    #calculate position change based on velocity
    debugPrint("start positionStep")
    #do for everything in the planet list
    for x in p:
        planetNum = p.index(x)

        debugPrint("start planet ["+str(planetNum)+"]")
        x.posX = x.posX + x.velocityX
        x.posY = x.posY + x.velocityY

        #add position to history
        x.historyPosX.append(x.posX)
        x.historyPosY.append(x.posY)
        
        debugPrint("posX "+str(x.posX))
        debugPrint("posY "+str(x.posY))
        debugPrint("end planet ["+str(p.index(x))+"]")
    debugPrint("end positionStep")
    return(p)

def saveStep(p,count):
    if count % 1000 == True:
        for planet in p:
            saveLocation = os.path.join(mainDir, posHistoryPath,str(planet.id),str(count))
            print(f"saved to: {saveLocation}")
            coords = [planet.posX, planet.posY]
            savetofile(repr(coords),saveLocation)





#MAIN IS HERE THIS DOES EVERYTHING DONT FUCK IT UP PEOPLE

def main(tCount,p):
    y=0
    while y<tCount:
        print(y)
        
        velocityStep(p,G)
        positionStep(p)
        saveStep(p,y)
        y=y+1

#clear up print clutter during use
def debugPrint(x):
    global debugMode
    if debugMode == True:
        print(x)

def savetofile(elements,file):
    with open(str(file)+".txt", "a") as file:
        for element in elements:
            file.write(str(element))


#ask for debug mode


if input("debug mode? (y/n)") =="y":
    debugMode = True



main(int(input("How many cycles?")),p)

for x in p:
    debugPrint("Planet ["+str(p.index(x))+"]")
    debugPrint(vars(x))



input('Press RETURN to finish')

