#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:01:39 2019

@author: 2020shatgiskessell
"""

def string_incrementer(word):
    if word == "":
        return "1"
    numbers = ["1","2","3","4","5","6","7","8","9"]
    number = ""
    original_number = ""
    word = list(word)
    is_zero = False
    for i in range(len(word)):
        ch = word[i]
        #check if character is a number
        if ch in numbers:
            number += ch
        #disregard leading 0
        if ch == "0":
            is_zero = True
            if word[i-1] in numbers:
                number += ch
    for n in number:
        word.remove(n)

    if number != "":
        original_number = number
        number = int(number) + 1
    else:
        if is_zero == True:
            word[-1] = "1"
            number = ""
        else:
            number = 1

    if len(original_number) == len(str(number)):
        word.append(str(number))
    else:
        difference = len(str(number)) - len(original_number)
        for i in range (difference):
            if word[-1] == "0":
                word.pop(-1)
        word.append(str(number))
    word = ''.join(word)
    return word

print(string_incrementer(""))
