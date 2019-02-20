#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:35:47 2019

@author: 2020shatgiskessell
"""
def make_array (element):
    array = []
    for i in element:
        array.append(i)
    return array

def unique_in_order (array):
    no_duplicates = []
    #if the input is not an array, turn it into one
    if type(array) is not list:
        array = make_array(array)
    #need to append an extraneous value
    array.append(0)
    #loop through every element in array
    for i in range(len(array)):
        #make sure there is a next element
        if i+1 < len(array):
            #if the next element is not equal to current element
            if array[i] != array[i+1]:
                #add to array
                no_duplicates.append(array[i])
    return no_duplicates
#
unique_in_order ("AAAABBBCCDAABBB")


