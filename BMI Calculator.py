import tkinter as tk
from tkinter import messagebox

# Calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height * height)

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nStatus: {status}"
        )

    except:
        messagebox.showerror(
            "Error",
            "Enter valid numbers"
        )

# Window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")

# Title
title = tk.Label(
    window,
    text="BMI Calculator",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)

# Weight
tk.Label(
    window,
    text="Weight (kg)"
).pack()

weight_entry = tk.Entry(window, width=25)
weight_entry.pack(pady=5)

# Height
tk.Label(
    window,
    text="Height (m)"
).pack()

height_entry = tk.Entry(window, width=25)
height_entry.pack(pady=5)

# Button
calculate_btn.pack(pady=15)
clear_btn = tk.Button(
    window,
    text="Clear",
    command=clear_fields,
    width=20
)

clear_btn.pack(pady=5)

# Result
result_label = tk.Label(
    window,
    text="Enter your details",
    font=("Arial", 12)
)
