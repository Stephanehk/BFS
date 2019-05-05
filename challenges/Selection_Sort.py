def selection_sort (array):
    for i in range (len(array)):
        current_min = i
        for j in range (i, len(array)):
            if array[j] < array[current_min]:
                current_min = j
        current = array[i]
        array[i] = array[current_min]
        array[current_min] = current
    return array


print (selection_sort ([11,65,8,3,12,0]))
