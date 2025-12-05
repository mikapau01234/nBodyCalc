print("start")

print("importing thingos")
from math import *
import matplotlib.pyplot as plt
import numpy as np

print("importing done")

#physical constants
#Gravity constant
G = 1

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


p0 = Planet(1,1,1,0,0)

p1 = Planet(1,-1,-1,0,0)

p2 = Planet(1,1,-1,0,0)

p3 = Planet(1,-1,1,0,0)

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
    print("start velocityStep")
    for x in p:
        index = p.index(x)
        print(index)
        y=0
        print("current planet: "+str(index))
        #do for every other planet
        while y<len(p):
            if y!=index:
                #DO STUFF HERE WITH THE OTHER PLANETS
                FgTupple = gravityForce(x,p[y],G)
                print(FgTupple)
                x.velocityX = x.velocityX + FgTupple[0]
                x.velocityY = x.velocityY + FgTupple[1]
            else:
                print("skip planet ["+str(y)+"] Reason: same Planet")
            y=y+1
            print("step "+str(y))
        print("planet "+str(index)+" done")
    print("end velocityStep")
    return(p)


def positionStep(p):
    #calculate position change based on velocity
    print("start positionStep")
    #do for everything in the planet list
    for x in p:
        planetNum = p.index(x)

        print("start planet ["+str(planetNum)+"]")
        x.posX = x.posX + x.velocityX
        x.posY = x.posY + x.velocityY

        #add position to history
        x.historyPosX.append(x.posX)
        x.historyPosY.append(x.posY)
        
        print("posX "+str(x.posX))
        print("posY "+str(x.posY))
        print("end planet ["+str(p.index(x))+"]")
    print("end positionStep")
    return(p)

def main(tCount,p):
    y=0
    while y<tCount:
        p = velocityStep(p,G)
        p = positionStep(p)
        y=y+1


main(int(input("How many cycles?")),p)

for x in p:
    print("Planet ["+str(p.index(x))+"]")
    print(vars(x))


#plot pos history
plt.plot(p0.historyPosX,p0.historyPosY,"b",p1.historyPosX,p1.historyPosY,"r")
plt.plot(p2.historyPosX,p2.historyPosY,"k")
plt.plot(p3.historyPosX,p3.historyPosY,"m")
#plot current pos
plt.plot(p0.posX,p0.posY,".b",p1.posX,p1.posY,".r")
plt.plot(p2.posX,p2.posY,".k")
plt.plot(p3.posX,p3.posY,".k")


plt.show()


input('Press RETURN to finish')

