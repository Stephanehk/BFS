#Find the dot product of 2 matrixes without using numpy

#-------ANSWER----------------------------
import numpy as np

# A = [1,2,3,4]
# B = [1,2,3,4]

def dot_product (matrix1, matrix2):
    dp = 0
    for i,j in zip(matrix1, matrix2):
        dp += (i*j)
    return dp
