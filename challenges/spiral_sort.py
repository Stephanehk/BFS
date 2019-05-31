import numpy as np

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

def row_col(matrix):
    spiral = []
    #while there is still a matrix
    while len(matrix)>0:
        #get top row
        for i in range (len(matrix)):
            spiral.append(matrix[0][i])
        #get right most column
        for i in range (1,len(matrix)):
            spiral.append(matrix[i][len(matrix)-1])
        #get bottom row
        for i in range (1, len(matrix)):
            spiral.append(matrix[len(matrix)-1][len(matrix)-1 - i])
        #get left most column
        for i in range (1,len(matrix)-1):
            spiral.append(matrix[len(matrix)-1 -i][0])
        #to handle odd sized matrices
        if len(matrix) != 1:
            #delete all rows and collumns just searched
            matrix = np.delete(matrix, (0), axis=0)
            matrix = np.delete(matrix, (len(matrix)-1), axis=0)
            matrix = np.delete(matrix, (0), axis=1)
            matrix = np.delete(matrix, (len(matrix)), axis=1)
        else:
            return spiral
    return spiral

print(row_col(matrix))

#print (spiral)
