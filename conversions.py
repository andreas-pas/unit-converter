#converter.py

def convertLength(value, from_unit, to_unit):
    """Convert between different length units."""
    length_units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144
    }
    
    if from_unit not in length_units or to_unit not in length_units:
        return "Invalid unit"
    
    #convert to metres first then to the desired unit
    #simpler than making separate calculations for every conversion
    meters = value * length_units[from_unit]
    result = meters / length_units[to_unit]
    
    return result

def convertTemperature(value, from_unit, to_unit):
    """Convert between Celsius, Fahrenheit, and Kelvin."""
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid temperature units"

def convertWeight(value, from_unit, to_unit):
    """Convert between weight units."""
    weight_units = {
        "grams": 1,
        "kilograms": 1000,
        "milligrams": 0.001,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    
    if from_unit not in weight_units or to_unit not in weight_units:
        return "Invalid unit"
    
    #convert to grams first then to the desired unit
    #simpler than making separate calculations for every conversion
    grams = value * weight_units[from_unit]
    result = grams / weight_units[to_unit]
    
    return result
