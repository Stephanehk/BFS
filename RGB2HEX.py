import numpy as np

def base10_to_16 (n):
    hex_dict = {10: "A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    hex = ""
    devided = None
    original_number = n

    while devided != 0:
        remainder = n%16
        if remainder > 9:
            remainder = hex_dict.get(remainder)
        hex+=str(remainder)
        devided = int(n/16)
        n = devided

    if len(str(original_number)) == 1:
        hex += "0"
    hex = "".join(reversed(hex))
    return hex

def round (n):
    if n > 255:
        return 255
    elif n < 0:
        return 0
    else:
        return n

def rgb (r,g,b):
    #round
    r = round(r)
    g = round(g)
    b = round(b)

    hex_r = base10_to_16(r)
    hex_g = base10_to_16(g)
    hex_b = base10_to_16(b)
    hex = hex_r + hex_g + hex_b
    return hex

print (rgb (-20,275,125))
