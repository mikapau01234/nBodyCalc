
import os
dirname = os.path.dirname(__file__)


def savetofile(elements,file):
    with open(str(file)+".txt", "a") as file:
        for element in elements:
            file.write(str(element)+"\n")

        

def readfromfile(file):
    with open(str(file)) as file:
        out = file.readlines()
        a = []
        for element in out:
            element = element.strip("\n")
            a.append(element)
        out = a
            
    return(out)

numbers = []
x=0
while x< 1000:
    x=x+1
    numbers.append(x)
    if x%100 == 0:
        savetofile(numbers,str(os.path.join(dirname, 'numberTxt\\'))+str(x))
        numbers = []
