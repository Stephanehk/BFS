#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:01:39 2019

@author: 2020shatgiskessell
"""

def string_incrementer(word):
    numbers = ["1","2","3","4","5","6","7","8","9"]
    number = ""
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
        number = int(number) + 1
    else:
        if is_zero == True:
            word[-1] = "1"
            number = ""
        else:
            number = 1
    word.append(str(number))
    word = ''.join(word)
    return word

print(string_incrementer("foobar0999"))
