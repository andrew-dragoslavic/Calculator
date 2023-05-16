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
                expression = self.display.get()
                expression = expression.replace("π", str(math.pi))
                expression = expression.replace("^", "**")
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        elif text == "π":
            if(self.display.get() and (self.display.get()[-1].isdigit() or self.display.get()[-1] == "π")):
                self.display.insert(tk.END, "*" + text)  # Insert "*" before "pi" if a digit, ")" or "pi" precedes it
            else:
                self.display.insert(tk.END, text)   
        elif text == "DEL":
            current_expression = self.display.get()
            self.display.delete(0,tk.END)
            self.display.insert(0, current_expression[0:-1])
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
