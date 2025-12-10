import os

dirname = str(os.path.dirname(__file__))
print(f"maindirname: {dirname}")
mydir = os.path.join(dirname,"numberTxt")
print(f"mydir: {mydir}")
myfiles = os.listdir(mydir)
print(myfiles)

def readfromfile(file):
    with open(str(file)) as file:
        out = file.readlines()
        a = []
        for element in out:
            element = element.strip("\n")
            a.append(element)
        out = a

    return (out)



for file in myfiles:
    cleanfile = os.path.join(dirname, "numberTxt", file)
    print(cleanfile)
    out = readfromfile(cleanfile)
    print(out)
