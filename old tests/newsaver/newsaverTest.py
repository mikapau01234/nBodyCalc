
import os
dirname = os.path.dirname(__file__)
print(dirname)

saveCounter = 0

list1 = list(range(1,20))


def saveList(path,list):
    file = open(path, "w")
    file.write(str(list))
    file.close()

saveList("Save"+str(saveCounter)+".txt",list1)

#technical EOF

file1 = open("Save1.txt", "r")
print(file1.read())
listListTest = file1.read()
file1.close()