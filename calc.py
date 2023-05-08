import math
import random as r
import tkinter as tk
top = tk.Tk()
top.title("Calculator")
for i in range(10):
    button = tk.Button(top, text= i)
    button.pack()
# Code to add widgets will go here...
top.mainloop()

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

def exp(x,y):
    return pow(x,y)

def function(oper):
    if op == '+':
        return add(n1,n2)   
    if op == '-':
        return sub(n1,n2)
    if op == '*':
        return mult(n1,n2)
    if op == '/':
        return div(n1,n2)
    if op == '^':
        return exp(n1,n2)


n1 = float(input("Enter the first number: "))
op = input("Enter the operator (+, -, *, /, ^): ")
n2 = float(input("Enter the second number: "))

print(function(op))

