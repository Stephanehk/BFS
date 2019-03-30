#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:08:35 2019

@author: 2020shatgiskessell
"""
import string 
import numpy as np

#create arrays to store each line of the keyboard
line1 = ["q","w","e","r","t","y","u","i","o","p"] #0-9
line2 = ["a","s","d","f","g","h","j","k","l"]#10-18
line3 = ["z","x","c","v","b","n","m",",","."]#19-25

def shift(character_index, offset, array):
    #calculate characters total offset
    total_offset = int(character_index) + int(offset)
    #make sure the total offset is not out of bounds
    if total_offset  > len(array)-1:
        #if it is, adjust offset value accordingly
        total_offset = total_offset - len(array)
    #get index of new character at offset
    shifted = array[total_offset]
    return shifted

def shift_back(character_index, offset, array):
    #calculate characters total offset
    total_offset = int(character_index) - int(offset)
    #make sure the total offset is not out of bounds
    if total_offset < 0:
        #if it is, adjust offset value accordingly
        total_offset = total_offset + len(array)
    #get index of new character at offset
    shifted = array[total_offset]
    return shifted

def get_line_position (text, encryptKey, operation):
    #empty array to store output
    output = ""
    
    special_symbols = {",":"<", ".":">", "/":"?", ";":":","'":'"',"[":"{","]":"}","\"":"|"}
    
    #turn offset into a string so it is easier to manipulate
    encryptKey = str(encryptKey)
    #if only one offset value is passed instead of 3, handle 
    if len(encryptKey) == 1:
        encryptKey += encryptKey[0]
        encryptKey += encryptKey[0]
    #get offset values for each line from input 
    line_1_off = encryptKey[0]
    line_2_off = encryptKey[1]
    line_3_off = encryptKey[2]
    
    #loop through each character in iput string
    for character in text:
        #if the character is a space, add it to encrypted and keep going
        if character == " ":
            output += " "
            continue
        #keep track of character lowercase/uppercase status
        if character.islower() or character in special_symbols.keys():
            is_lower = True
        elif not character.islower():
            #handle uppercase symbols (previously a bug)
            if character in special_symbols.values():
                #gets the key of the special_symbols array from the value
                character = list(special_symbols.keys())[list(special_symbols.values()).index(character)]
            is_lower = False
            character = str.lower(character)
        #find what line the character is in, get character index, and call shift function accordingly
        if character in line1:
            index = line1.index(character)
            shifted = eval(operation)(index, line_1_off, line1)
        elif character in line2:
            index = line2.index(character)
            shifted = eval(operation)(index, line_2_off, line2)
        elif character in line3:
            index = line3.index(character)
            shifted = eval(operation)(index, line_3_off, line3)
        else:
            continue
        
        if not is_lower:
            #fix lowercase/upercase characters
            if shifted in special_symbols.keys():
                shifted = special_symbols.get(shifted)
            shifted = str.upper(shifted)
        output +=(shifted)
    return output

def encrypt(text, encryptKey):
    return get_line_position (text, encryptKey, "shift")

def decrypt(text, encryptKey):
    return get_line_position (text, encryptKey, "shift_back")
