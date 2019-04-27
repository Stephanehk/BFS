import numpy

class Node:
    #node class to store each nodes properties
    def __init__(self, xcoordinate= None, ycoordinate= None, value = None, visited = None):
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate
        self.value = value
        self.visited = False

# region = [
#     'OOXXX',
#     'OOXXX',
#     'OOXXX',
#     'OOXXX',
#     'OOXXX'
# ]
region = [
        ['O','O','X','X','X'],
        ['O','O','X','X','X'],
        ['O','O','X','X','X'],
        ['O','O','X','X','X'],
        ['O','O','X','X','X']
    ]

def prepare_area(area):
    for i in range (len(area)):
        for j in range (len(area)):
            if area[i][j] == "O":
                current = Node()
                current.xcoordinate = i
                current.ycoordinate = j
                current.value = "O"
                area[i][j] = current
            else:
                current = Node()
                current.xcoordinate = i
                current.ycoordinate = j
                current.value = "X"
                area[i][j] = current
    return area

def print_adjacency(adjacency_list):
    for point in adjacency_list:
        print ("("+str(point.xcoordinate) + "," + str(point.ycoordinate) +")" + "-->" + point.value + "--> " + str(point.visited))
    print ("\n")

def check_neighbors (x, y,target, adjacency_list, max_votes):
    num_votes = 0
    try:
        north = area[x-1][y]
        if north.value == target and num_votes+1 <= max_votes and x-1 > -1 and y>-1 and north.visited == False:
            adjacency_list.append(north)
            north.visited = True
            num_votes +=1
    except IndexError:
        pass
    try:
        east = area[x][y+1]
        if east.value == target and num_votes+1 <= max_votes and x >-1 and y+1>-1 and east.visited == False:
            adjacency_list.append(east)
            east.visited = True
            num_votes +=1
    except IndexError:
        pass
    try:
        west = area[x][y-1]
        if west.value == target and num_votes+1 <= max_votes and x>-1 and y-1>-1 and west.visited == False:
            adjacency_list.append(west)
            west.visited = True
            num_votes +=1
    except IndexError:
        pass
    try:
        south = area[x+1][y]
        if south.value == target and num_votes+1 <= max_votes and x+1>-1 and y>-1 and south.visited == False:
            adjacency_list.append(south)
            south.visited = True
            num_votes +=1
    except IndexError:
        pass
    return adjacency_list, num_votes

def extend_adjacency (adjacency_list, opposition_adjacency_list):
    for adjacent in opposition_adjacency_list:
        if adjacent not in adjacency_list:
            adjacency_list.append(adjacent)
    return adjacency_list

def devide_area (area, current_x,current_y, adjacency_list):
    start = area[current_x][current_y]
    start.visited = True
    adjacency_list, num_votes = check_neighbors (current_x,current_y,"O", [start],3)
    current_votes = len(adjacency_list)
    while current_votes != 5:
        for i in range(len(adjacency_list)):
            point = adjacency_list[i]
            opposition_adjacency_list, num_votes = check_neighbors (point.xcoordinate,point.ycoordinate,"X", [],5-current_votes)
            current_votes += len(opposition_adjacency_list)
            adjacency_list = extend_adjacency(adjacency_list, opposition_adjacency_list)
    # for point in adjacency_list:
    #     print (str(point.xcoordinate) + "," + str(point.ycoordinate))
    return adjacency_list

def jerry(area):
    for i in range (len(area)):
        for j in range (len(area)):
            point = area[i][j]
            if point.visited == False:
                adjacency_list = devide_area (area, i,j, [])
                print_adjacency(adjacency_list)

area = prepare_area(region)
# adjacency_list = devide_area (area, 0,0, [])
# print_adjacency(adjacency_list)
jerry(area)
