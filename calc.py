import math
import random as r
import tkinter as tk
top = tk.Tk()
top.title("Calculator")
top.minsize(300,400)
top.maxsize(300,400)

entry = tk.Entry(top,font = ("Century 32"), width=300)
entry.grid(row=0, column=0, columnspan=4)
entry.place(height = 50, width = 300)

# for i in range(10):
#     button = tk.Button(top, text= i)
#     button.pack()
# for i in range(5):
#     if(i == 0):
#         button = tk.Button(top, text= '+')
#         button.pack()
#     if(i == 1):
#         button = tk.Button(top, text= '-')
#         button.pack()
#     if(i == 2):
#         button = tk.Button(top, text= '*')
#         button.pack()
#     if(i == 3):
#         button = tk.Button(top, text= '/')
#         button.pack()
#     if(i == 4):
#         button = tk.Button(top, text= '^')
#         button.pack()
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

