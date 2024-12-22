# install these codes into bash/terminal
# sudo apt-get update
# sudo apt-get install -y xvfb
# xvfb-run python /workspaces/Build-Calculator/GUI_Calculator.py



import tkinter as tk
from tkinter import messagebox

def perform_operation():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Dropdown menu for operations
operation_var = tk.StringVar(value="+")
tk.Label(root, text="Select operation:").pack()
tk.OptionMenu(root, operation_var, "+", "-", "*", "/").pack()

# Perform button
tk.Button(root, text="Calculate", command=perform_operation).pack()

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the application
root.mainloop()
