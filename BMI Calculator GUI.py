import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI")
root.configure(bg='#ebcf34')
# BMI Calculate function
def calculate_bmi():
    kg = float(entry_kg.get())
    ft = float(entry_height.get())
    height = ft/3.28
    bmi = bmi = round(kg / (height *2), 2)
    label_result['text'] = f"{bmi}"
    
# Create GUI
label_kg = tk.Label(root, text="Weight (kg): ")
label_kg.grid(column=0, row=0)

entry_kg = tk.Entry(root)
entry_kg.grid(column=1, row=0)

label_height = tk.Label(root, text="HEIGHT (ft): ")
label_height.grid(column=0, row=1)

entry_height = tk.Entry(root)
entry_height.grid(column=1, row=1)

button_calculate = tk.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=2)

label_result = tk.Label(root,)
label_result.grid(column=1, row=2)

root.mainloop() 