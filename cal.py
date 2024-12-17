import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
import numpy as np
from tkinter import simpledialog

def press(key):
    """Handles button presses by updating the expression field."""
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "DEL":
        entry.delete(len(entry.get())-1, tk.END)
    else:
        entry.insert(tk.END, key)

def scientific_operation(op):
    """Handles scientific operations like sin, cos, log, etc."""
    try:
        value = float(entry.get())
        if op == "sin":
            result = math.sin(math.radians(value))
        elif op == "cos":
            result = math.cos(math.radians(value))
        elif op == "tan":
            result = math.tan(math.radians(value))
        elif op == "log":
            result = math.log10(value)
        elif op == "ln":
            result = math.log(value)
        elif op == "sqrt":
            result = math.sqrt(value)
        elif op == "exp":
            result = math.exp(value)
        else:
            result = "Invalid"

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input for {op}: {e}")

def plot_graph():
    """Plots a graph based on user input for an equation."""
    try:
        equation = simpledialog.askstring("Input", "Enter equation in terms of x (e.g., x**2 + 2*x + 1):")
        if equation:
            x = np.linspace(-10, 10, 400)
            y = [eval(equation.replace("x", str(i))) for i in x]

            plt.figure("Graph of Equation")
            plt.plot(x, y, label=f"y = {equation}")
            plt.title("Graph of Equation")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
            plt.grid(True)
            plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation: {e}")

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x550")
root.resizable(False, False)

# Entry Widget
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=8, ipady=8)

# Button Layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("(", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), (")", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("DEL", 4, 4),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), bg="#f0f0f0", width=5, height=2,
                       command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Scientific Operation Buttons
scientific_buttons = [
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3), ("ln", 5, 4),
    ("sqrt", 6, 0), ("exp", 6, 1), ("Graph", 6, 3)
]

for (text, row, col) in scientific_buttons:
    if text == "Graph":
        button = tk.Button(root, text=text, font=("Arial", 14), bg="#a0f0f0", width=5, height=2,
                           command=plot_graph)
    else:
        button = tk.Button(root, text=text, font=("Arial", 14), bg="#d0f0f0", width=5, height=2,
                           command=lambda t=text: scientific_operation(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the Application
root.mainloop()