from operator import truediv
#blabli




from math import *
from pickle import GLOBAL

import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import random
import argparse
import yaml




#physical constants
#Gravity constant
G = 0.00000000006674
#G = 0.0000000001
#classes
class classPlanet:
    def __init__(self, id, mass, posX, posY, velocityX, velocityY):
        self.id = id
        self.mass = mass
        self.posX = posX
        self.posY = posY
        self.velocityX = velocityX
        self.velocityY = velocityY






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
    for index,x in enumerate(p):
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
    for planetNum,x in enumerate(p):

        debugPrint("start planet ["+str(planetNum)+"]")
        x.posX = x.posX + x.velocityX
        x.posY = x.posY + x.velocityY


        
        debugPrint("posX "+str(x.posX))
        debugPrint("posY "+str(x.posY))
        debugPrint("end planet ["+str(planetNum)+"]")
    debugPrint("end positionStep")
    return(p)


#this saves stuff :)
def saveStep(p):
    for planet in p:
        saveLocation = os.path.join(mainDir, posHistoryPath,str(planet.id),"1")
        print(f"saved to: {saveLocation}")
        coords = [planet.posX, planet.posY]
        savetofile(repr(coords)+",",saveLocation)







#MAIN IS HERE THIS DOES EVERYTHING DONT FUCK IT UP PEOPLE

def mainLoop(tCount,p):

    y=1
    saveStep(p)

    while y<=tCount:
        print(y)

        velocityStep(p,G)
        positionStep(p)
        if y % args.positionSampleSize == 0:
            saveStep(p)
        y=y+1

#clear up print clutter during use
def debugPrint(x):
    if args.debugMode == True:
        print(x)

def savetofile(element,file):
    with open(str(file)+".txt", "a") as file:
        file.write(str(element))

#logic functions
def isPositive(value):
    intValue = int(value)
    if intValue <=0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid int value")
    return intValue

def main():
    global mainDir, posHistoryPath, args, G

    print("start")

    # global system parameters
    parser = argparse.ArgumentParser()

    # file params
    mainDir = os.path.dirname(__file__)

    posHistoryPath = os.path.join(mainDir, "posHistory")

    # arguments
    parser.add_argument("-cn", "--cycleNumber", help="amount of cycles that are calculated, only works with values above zero", type=isPositive)
    parser.add_argument("-pra", "--planetsRandomAmount", help="amount of random planets that are produced", type=isPositive,default=0)
    parser.add_argument("-dbg", "--debugMode", help="enables debug features", action="store_true", default=False)
    parser.add_argument("-prr", "--positionRandomRange", help="defines maximum coordinate values for random planets", type=isPositive, default=50000)
    parser.add_argument("-pss", "--positionSampleSize", help="defines every how many cycles the programm saves planet positions", type=isPositive, default=250)
    parser.add_argument("-yamlcfg","--yamlConfig", help="file path for config yaml file", type=str, default="config.yaml")
    args = parser.parse_args()



    # argument constants
    # amount of cycles
    if args.cycleNumber > 0:
        cycleNumber = args.cycleNumber
    elif args.cycleNumber < 0:
        cycleNumber = args.cycleNumber * -1

    debugPrint("reading yaml file")
    with open(args.yamlConfig, "r") as file:
        loadedYaml = yaml.safe_load(file)
    debugPrint(f"loaded yaml file:{loadedYaml}")
    #set G
    G = loadedYaml["constants"]["G"]

    #convert yaml format to usable format
    p=[]
    if args.planetsRandomAmount == 0:
        for planet in loadedYaml["planets"]:
            curPlanet=classPlanet(planet["id"],planet["mass"],planet["posX"],planet["posY"],planet["velocityX"],planet["velocityY"])
            debugPrint(f"current planet (YAML=>usable): {vars(curPlanet)}")
            p.append(curPlanet)
    else:
        x = 0
        while x < args.planetsRandomAmount:
            x = x + 1

            p.append(classPlanet(x, random.randint(5000000, 100000000),
                                 random.randint(args.positionRandomRange * -1, args.positionRandomRange),
                                 random.randint(args.positionRandomRange * -1, args.positionRandomRange),
                                 random.random() * 0.1 - 0.05, random.random() * 0.1 - 0.05))


    '''
    # define planets

    p0 = classPlanet(0, 10000000000, 0, 0, 0, -0.3)

    p1 = classPlanet(1, 100, 3000, 0, 0, -0.15834)

    p2 = classPlanet(2, 10, 5500, -10000, -0.01, 0.05)

    p3 = classPlanet(3, 100000, -50000, -2000, 0, 0)
    '''
    # tupple of planets
    #p = (p0, p1, p2, p3)
    '''
    

    '''

    # initiating file structure
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

    mainLoop(cycleNumber,p)

    for x in p:
        debugPrint("Planet ["+str(p.index(x))+"]")
        debugPrint(vars(x))

    input('Press RETURN to finish')

if __name__ == "__main__":
    main()