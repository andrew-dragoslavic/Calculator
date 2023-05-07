import math
import random as r

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x*y

def div(x,y):
    if(y == 0):
        return('ERROR') #print error
    else:
        return (x/y)

x = input("x: ") 
y = input("y: ")
x = float(x)
y = float(y)
print (f'{x} / {y} = {div(x,y)}')