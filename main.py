print("start")

print("importing thingos")
from math import *
import matplotlib.pyplot as plt
import numpy as np

print("importing done")

#global system parameters
debugMode = False



#physical constants
#Gravity constant
G = 0.00000000006674

#classes
class Planet:
    def __init__(self, mass, posX, posY, velocityX, velocityY):
        self.mass = mass
        self.posX = posX
        self.historyPosX = [posX]
        self.posY = posY
        self.historyPosY = [posY]
        self.velocityX = velocityX
        self.velocityY = velocityY

#define planets


p0 = Planet(1000000,0,0,0,0)

p1 = Planet(1,5000,0,0,0.0001)

p2 = Planet(1,-5000,0,0,-0.00005)

p3 = Planet(10,-2000,6000,0.001,-0.001)

#tupple of planets
p = (p0,p1,p2,p3)

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

def main(tCount,p):
    y=0
    while y<tCount:
        print(y)
        
        p = velocityStep(p,G)
        p = positionStep(p)
        y=y+1

#clear up print clutter during use
def debugPrint(x):
    global debugMode
    if debugMode == True:
        print(x)

#ask for debug mode


if input("debug mode? (y/n)") =="y":
    debugMode = True

    



main(int(input("How many cycles?")),p)

for x in p:
    debugPrint("Planet ["+str(p.index(x))+"]")
    debugPrint(vars(x))



#decide plot size
plt.xlim(-10000, 10000)
plt.ylim(-10000, 10000)
#plot pos history
plt.plot(p0.historyPosX[::10],p0.historyPosY[::10],"b",p1.historyPosX[::10],p1.historyPosY[::10],"r")
plt.plot(p2.historyPosX[::10],p2.historyPosY[::10],"k")
plt.plot(p3.historyPosX[::10],p3.historyPosY[::10],"m")
#plot current pos
plt.plot(p0.posX,p0.posY,".b",p1.posX,p1.posY,".r")
plt.plot(p2.posX,p2.posY,".k")
plt.plot(p3.posX,p3.posY,".m")


plt.show()


input('Press RETURN to finish')

