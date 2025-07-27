# app.py

import tkinter as tk
from tkinter import ttk
from conversions import convert_length, convert_temperature, convert_weight


#main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x550")


#length conversion function
def lengthConversion():
    try:
        value = float(length_entry.get())
        from_unit = length_from_var.get()
        to_unit = length_to_var.get()
        result = convert_length(value, from_unit, to_unit)
        result = format(result, '.2f')
        result_label.config(text=f"{value} {from_unit} = {result} {to_unit}")

    except ValueError:
        result_label.config(text="Please use different units for input and output")

#temperature conversion function
def tempConversion():
    try:
        value = float(temp_entry.get())
        from_unit = temp_from_var.get()
        to_unit = temp_to_var.get()
        result = convert_temperature(value, from_unit, to_unit)
        result = format(result, '.1f')
        result_label.config(text=f"{value} {from_unit} = {result} {to_unit}")
        
    except ValueError:
        result_label.config(text="Please use different units for input and output")

#weight conversion function
def weightConversion():
    try:
        value = float(mass_entry.get())
        from_unit = weight_from_var.get()
        to_unit = weight_to_var.get()
        result = convert_weight(value, from_unit, to_unit)
        result = format(result, '.2f')
        result_label.config(text=f"{value} {from_unit} = {result} {to_unit}")
        
    except ValueError:
        result_label.config(text="Please use different units for input and output")

#length conversion ui elements
length_label = tk.Label(root, text="Length conversion:")
length_label.pack(pady=5)

length_from_var = tk.StringVar()
length_to_var = tk.StringVar()

length_from = ttk.Combobox(root, textvariable=length_from_var, values=["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards"])
length_from.set("meters")
length_from.pack(pady=5)

length_to = ttk.Combobox(root, textvariable=length_to_var, values=["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards"])
length_to.set("kilometers")
length_to.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_button = tk.Button(root, text="Convert Length", command=lengthConversion, bg="#ADD8E6")
length_button.pack(pady=5)

#temperature conversion ui elements
temp_label = tk.Label(root, text="Temperature conversion:")
temp_label.pack(pady=5)


temp_from_var = tk.StringVar()
temp_to_var = tk.StringVar()

temp_from = ttk.Combobox(root, textvariable=temp_from_var, values=["Celsius", "Fahrenheit", "Kelvin"])
temp_from.set("Celsius")
temp_from.pack(pady=5)

temp_to = ttk.Combobox(root, textvariable=temp_to_var, values=["Celsius", "Fahrenheit", "Kelvin"])
temp_to.set("Fahrenheit")
temp_to.pack(pady=5)

temp_entry = tk.Entry(root)
temp_entry.pack(pady=5)
temp_button = tk.Button(root, text="Convert Temperature", command=tempConversion, bg="#ADD8E6")
temp_button.pack(pady=5)

#weight conversion elements
mass_label = tk.Label(root, text="Weight conversion:")
mass_label.pack(pady=5)


weight_from_var = tk.StringVar()
weight_to_var = tk.StringVar()

weight_from = ttk.Combobox(root, textvariable=weight_from_var, values=["grams", "kilograms", "milligrams", "pounds", "ounces"])
weight_from.set("grams")
weight_from.pack(pady=5)

weight_to = ttk.Combobox(root, textvariable=weight_to_var, values=["grams", "kilograms", "milligrams", "pounds", "ounces"])
weight_to.set("kilograms")
weight_to.pack(pady=5)

mass_entry = tk.Entry(root)
mass_entry.pack(pady=5)
mass_button = tk.Button(root, text="Convert Weight", command=weightConversion, bg="#ADD8E6")
mass_button.pack(pady=5)

#output
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

#start the GUI loop
root.mainloop()
