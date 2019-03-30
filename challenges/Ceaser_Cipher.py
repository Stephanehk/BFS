#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:30:23 2019

@author: 2020shatgiskessell
"""

#(x+n) % 26
import string

def encyrpt (word, offset):
    encrypted_word = []
    alphabet = list(string.ascii_lowercase)
    for i in range (len(word)):
        index_ = alphabet.index(word[i])
        encrypted  = alphabet[(index_ + offset) % 26]
        encrypted_word.append(encrypted)
    return encrypted_word

def decrypt (word, offset):
    encrypted_word = []
    alphabet = list(string.ascii_lowercase)
    for i in range (len(word)):
        index_ = alphabet.index(word[i])
        encrypted  = alphabet[(index_ - offset) % 26]
        encrypted_word.append(encrypted)
    return encrypted_word
#
encrypted = encyrpt ("science", 4)
print (encrypted)
#decrypt (encrypted, 20)
