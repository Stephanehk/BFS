#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:03:16 2019

@author: 2020shatgiskessell
"""

import psutil
import os
process = psutil.Process(os.getpid())

def matrid_add (m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m2[i][j] = m1[i][j] + m2[i][j]
    return m2

m1 = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
m2 = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
matrid_add (m1, m2)
print ("Memory Usage: " + str(process.memory_info().rss * 0.000001) + " megabytes")
