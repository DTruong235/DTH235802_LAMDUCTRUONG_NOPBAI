import time
import os
import math
def h1(n):
    for i in range(1, n+1):
        print(" " * (n*2) + "* " * i)

    print("* " * (n*2 + 1))

    for i in range(n, 0, -1):
        print(" " *  ((n-i+1)*2)  + "* " * i)

def h2(n):
    for i in range(1, n+1):
        spaces = " " * (n*2)   
        if i == 1:
          print(spaces + "*")
        elif i == 2:
           print(spaces + "* *")
        else:
          print(spaces + "*" + " " * (2*i-3) + "*")

    print("* " * (n*2 + 1))

    for i in range(n, 0, -1):
        indent = " " * ((n-i+1)*2) 
        if i == 1:
            print(" " * (n*2) + "*")
        elif i == 2:
            print(indent + "* *")
        else:
            print(indent + "*" + " " * (2*i-3) + "*")

def h3(n):
    for i in range(n, 0, -1):
        print(" " * 8 + "* " * i)

    for i in range(1, n+1):
        print(" " * (2 * (n - i+1)) + "* " * i)

def h4(n):
    for i in range(n, 0, -1):
        print(" " * 8, end="") 
        if i == n: 
          print("* " * i)
        elif i == 1: 
          print("*")
        elif i == 2:  
            print("* *")
        else: 
            print("*" + " " * (2*i - 3) + "*")


    for i in range(1, n+1):
        indent = " " * (2 * (n - i+1)) 
        if i == 1:
           print(indent + "*")
        elif i == n: 
           print(indent + "* " * i)
        elif i == 2: 
          print(indent + "* *")
        else: 
            print(indent + "*" + " " * (2*i - 3) + "*")

n = 3
while True:
    os.system("cls")
    h1(n)
    time.sleep(1)
    os.system("cls")
    h2(n)
    time.sleep(1)
    os.system("cls")
    h3(n+1)
    time.sleep(1)
    os.system("cls")
    h4(n+1)
    time.sleep(1)


