#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:34:36 2019

@author: 2020shatgiskessell
"""
import numpy as np

def fib (n):
    a = np.power((1 + np.sqrt(5))/2,n)
    b = np.power((1 - np.sqrt(5))/2,n)
    fib = (a-b)/np.sqrt(5)
    return int(fib)

fib (1000)