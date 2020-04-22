import math
import time
"""Unit Converter"""
#Welcome and variable setting

types = {
    "k": 1000,
    "h": 100,
    "da": 10,
    "": 1,
    "d": 0.1,
    "c": 0.01,
    "m": 0.001
}

def convert(from_unit_type, to_unit_type, value):
    from_type_units = types[from_unit_type]
    to_type_units = types[to_unit_type]

    new_value = value * (from_type_units / to_type_units)

    return str(new_value) + to_unit_type

print ("Welcome to Unit Converter")
cat = raw_input ("Which category would you like to convert? [g,l,m]")

unit1 = raw_input ("Which unit would you like to convert from: ")
unit2 = raw_input ("Which unit would you like to convert to: ")
num1 = raw_input ("Enter your value: " )

print(convert(unit1, unit2, float(num1)))