# import math
# import random as r
# import tkinter as tk
# top = tk.Tk()
# top.title("Calculator")
# top.minsize(300,400)
# top.maxsize(300,400)

# entry = tk.Entry(top,font = ("Century 32"), width=300)
# entry.grid(row=0, column=0, columnspan=4)
# entry.place(height = 50, width = 300)

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
# top.mainloop()

# def add(x,y):
#     return x + y

# def sub(x,y):
#     return x - y

# def mult(x,y):
#     return x*y

# def div(x,y):
#     if(y == 0):
#         return('ERROR') #print error
#     else:
#         return (x/y)

# def exp(x,y):
#     return pow(x,y)

# def log(x,y):
#     return math.log(x,y) #the y is the base and the x is number you want to compute

# def function(oper):
#     if op == '+':
#         return add(n1,n2)   
#     if op == '-':
#         return sub(n1,n2)
#     if op == '*':
#         return mult(n1,n2)
#     if op == '/':
#         return div(n1,n2)
#     if op == '^':
#         return exp(n1,n2)


# n1 = float(input("Enter the first number: "))
# op = input("Enter the operator (+, -, *, /, ^, log): ")
# n2 = float(input("Enter the second number: "))

# print(function(op))

import tkinter as tk
import math

class Calculator:
    def __init__(self, top):
        self.top = top
        top.title("Calculator")
        top.minsize(200,250)
        top.maxsize(200,250)

        self.display = tk.Entry(top, width=30)
        self.display.grid(row=0, column=0,rowspan = 1, columnspan=4, padx=0, pady=0)
        self.display.insert(tk.END, "")

        # Create buttons
        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("/", 2, 3)

        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("*", 3, 3)

        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("-", 4, 3)

        self.create_button("0", 5, 0)
        self.create_button(".", 5, 1)
        self.create_button("=", 5, 2)
        self.create_button("+", 5, 3)

        self.create_button("C", 1, 0)
        self.create_button("DEL", 1, 1)
        self.create_button("^", 1, 3)
        self.create_button("π", 1, 2)

    def create_button(self, text, row, column, columnspan=1, padx=2, pady=2):
        button = tk.Button(self.top, text=text, width=5, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady)

    def button_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
