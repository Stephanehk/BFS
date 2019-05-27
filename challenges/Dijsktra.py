import numpy as np

class Node:
    #node class to store each nodes properties
    def __init__(self, x=  None, y= None, value = None, visited = None, cost = None):
        self.x = x
        self.y = y
        self.value = value
        self.visited = False
        self.cost = cost

area = [
        ['0','2','1','1','X'],
        ['3','4','X','2','4'],
        ['1','3','5','3','6'],
        ['7','2','X','8','5'],
        ['8','9','X','4','END']
    ]

def prepare_area(area):
    for i in range (len(area)):
        for j in range (len(area)):
            if area[i][j] != "X" and area[i][j] != "END":
                current = Node()
                current.x = i
                current.y = j
                current.value = "O"
                current.cost = int(area[i][j])
                area[i][j] = current
            else:
                current = Node()
                current.x = i
                current.y = j
                current.value = "X"
                area[i][j] = current
    return area

def distance(x1,y1,x2,y2):
    dist = np.sqrt(np.power((x2-x1),2)+np.power((y2-y1),2))
    return dist

def print_adjacency(adjacency_list):
    for point in adjacency_list:
        print ("("+str(point.xcoordinate) + "," + str(point.ycoordinate) +")" + "-->" + point.value + "--> " + str(point.visited))
    print ("\n")

def check_neighbors (current, cost):
    adjacency_list = []
    x = current.x
    y = current.y
    lowest_cost = 100000
    lowest_cost_node = None
    try:
        north = area[x-1][y]
        if north.value == "END":
            return True, True
        if x-1 > -1 and y>-1 and north.visited == False and north.cost < lowest_cost:
            adjacency_list.append(north)
            north.visited = True
            lowest_cost = north.cost
            if lowest_cost_node != None:
                adjacency_list.remove(lowest_cost_node)
            lowest_cost_node = north
    except IndexError:
        pass
    try:
        east = area[x][y+1]
        if east.value == "END":
            return True
        if x >-1 and y+1>-1 and east.visited == False and east.cost < lowest_cost:
            adjacency_list.append(east)
            east.visited = True, True
            lowest_cost = east.cost
            if lowest_cost_node != None:
                adjacency_list.remove(lowest_cost_node)
            lowest_cost_node = east
    except IndexError:
        pass
    try:
        west = area[x][y-1]
        if west.value == "END":
            return True
        if x>-1 and y-1>-1 and west.visited == False and west.cost < lowest_cost:
            adjacency_list.append(west)
            west.visited = True, True
            lowest_cost = west.cost
            if lowest_cost_node != None:
                adjacency_list.remove(lowest_cost_node)
            lowest_cost_node = west
    except IndexError:
        pass
    try:
        south = area[x+1][y]
        if south.value == "END":
            return True
        if x+1>-1 and y>-1 and south.visited == False and south.cost < lowest_cost:
            adjacency_list.append(south)
            south.visited = True, True
            lowest_cost = south.cost
            if lowest_cost_node != None:
                adjacency_list.remove(lowest_cost_node)
            lowest_cost_node = south
    except IndexError:
        pass
    return adjacency_list, cost+lowest_cost

def main(area):
    for i in range (len(area)):
        for j in range (len(area)):
            current = area[i][j]
            if current.value == "O":
                adjacency_list, cost = check_neighbors (current, 0)
                while adjacency_list != True:
                    adjacency_list, cost = check_neighbors (adjacency_list[0], cost)
                print (adjacency_list)

area = prepare_area(area)
main(area)
