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
    for i in range(len(word)):
        ch = word[i]
        print (ch)
        #check if character is a number
        if ch in numbers:
            print (ch)
            number += ch
        #disregard leading 0
        if ch == "0" and word[i-1] in numbers:
            number += ch
    
    for n in number:
        word.remove(n)
    
    number = int(number) + 1
    word.append(str(number))
    word = ''.join(word)
    return word
