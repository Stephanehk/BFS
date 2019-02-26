#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:08:05 2019

@author: 2020shatgiskessell
"""
import re

def color_code_it (input_):
    #store results
    band = []
    #dicionary of color codes
    color_codes = {0: "black", 1: "brown", 2: "red", 3: "orange", 4: "yellow", 5: "green", 6: "blue", 7: "violet", 8: "gray", 9: "white"}
    #dictionary for unit conversion
    unit_conv = {"O": 1, "k": 1000, "M": 1000000}
    try:
        #use regular expression to seperate integer from string
        r = re.compile("([0-9]+)([a-zA-Z]+)")
        converted = r.match(input_)
        #get just the integers (the ohms)
        ohms = converted.group(1)
        #get just the strings (the units)
        units = converted.group(2)
    except AttributeError:
        #if there is an error (no string next to the number), just take the integer (the ohms)
        ohms = int(re.search(r'\d+', input_).group())
        units = "O"
    #convert input into ohms by getting the conversion from dictionary
    ohms = int(ohms) * unit_conv.get(units)
    #turn ohms to string so that it can be parsed
    ohms = str(ohms)
    #get the first 2 numbers
    for i in range (2):
        #get the color code from the corrosponding number
        color = color_codes.get(int(ohms[i]))
        #store in final result
        band.append(color)
    #get the exponent of multiplier
    exponent = len(ohms) -2
    #get corrosponding color
    color = color_codes.get(exponent)
    #store in final result
    band.append(color)
    #always add gold for tolerence
    band.append("gold")
    return band

color_code_it ("10 ohms")

