import threading
import time

number = 0

def function():
    global number
    number = number + 1

t1 = threading.Thread(target=function, args=())
t1.start()
print(number)