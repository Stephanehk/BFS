#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 08:58:43 2019

@author: 2020shatgiskessell
"""

def replace_character (word):
    output = ""
    values = {"A":"@", "E":"3", "I":"!", "O":"0","U":")"}
    for ch in word:
        if ch in values.keys():
            output += values.get(ch)
    return output


def reverse_string (word):
    length = len(word)
    for i in range(length):
        word.append(word[length-1 - i])
    word = word [length:]
    return word

print(reverse_string (["h","e","l","l","o"]))