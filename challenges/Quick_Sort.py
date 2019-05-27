import numpy as np

def swap(array, pivot, swapped):
    #[0, 1, 2, 7, 3, 10, 8]
    p_index = array.index(pivot)
    #check to see if pivot and swapped are next to eachother
    if np.abs(p_index-swapped) == 1:
        array[p_index] = array[swapped]
        array[swapped] = pivot
        return array

    array[p_index] = array[swapped]
    intermed = array[p_index-1]
    array[p_index-1] = pivot
    array[swapped] = intermed
    return array

def sort_from_pivot(array, pivot, current):
    print ("current: " + str(array[current]))
    # print ("pivot: " + str(pivot))
    if array[current] > pivot:
        array = swap(array, pivot, current)
        # print ("after swapping " + str(array[current]) + " and " + str(pivot))
        # print (array)
        return sort_from_pivot(array, pivot, current)
    p_index = array.index(pivot)
    if array[p_index-1] > pivot:
        return sort_from_pivot(array, pivot, current + 1)
    return (array)

def quicksort(array):
    for i in range (len(array)):
        array = sort_from_pivot(array, array[-1], i)
    print (array)

array = [8,3,1,7,0,10,2]
quicksort(array)
#print(sort_from_pivot(array, 2, 0))
