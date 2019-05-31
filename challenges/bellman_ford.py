import numpy as np

class Node:
    def __init__(self, x= None, y= None, val=None, distance = None):
        self.x = x
        self.y = y
        self.val = val
        self.distance = distance

matrix = [["0","1","2"],
         ["5","-4","2"],
         ["1","3","1"]]

def add_weightings (maze,destination):
    for i in range (len(maze)):
        for j in range (len(maze)):
            if maze[i][j] != "W":
                current = Node()
                current.x = i
                current.y = j
                #assign values
                current.val = int(maze[i][j])
                current.distance = float("Inf")
                maze[i][j] = current
    # maze[destination.x][destination.y] = "D"
    return maze

def check_direction(maze, current, destination, possible_next_steps, current_cost):
    #get all the possible next steps from given node
    x,y = current.x, current.y
    dx,dy = destination.x, destination.y
    #print current node coordinate
    #print ("(" + str(x) + "," + str(y) + ") ->")

    #check if destination is reached
    # if x == dx and y == dy:
    #     return "destination reached"
    try:
        north = maze[x-1][y]
        #make sure everything is in bounds
        if x-1 > 0 and north != "W" and north not in possible_next_steps:
            #if everything checks out, add direction to possible_next_steps
            if current_cost + north.val < north.distance:
                north.distance = current_cost + north.val
                possible_next_steps.append(north)
    except IndexError:
        pass
    try:
        east = maze[x][y+1]
        if y+1 > 0 and east != "W" and east:
            if current_cost + east.val < east.distance:
                east.distance = current_cost + east.val
                possible_next_steps.append(east)
    except IndexError:
        pass
    try:
        south = maze[x+1][y]
        if x+1 > 0  and south != "W" and south not in possible_next_steps:
            if current_cost + south.val < south.distance:
                south.distance = current_cost + south.val
                possible_next_steps.append(south)
    except IndexError:
        pass
    try:
        west = maze[x][y-1]
        if y-1 > 0  and west != "W" and west not in possible_next_steps:
            if current_cost + west.val < west.distance:
                west.distance = current_cost + west.val
                possible_next_steps.append(west)
    except IndexError:
        pass
    return possible_next_steps

def travel_lowest (maze, current, closed_list, destination):
    x,y = current.x,current.y
    dx,dy = destination.x, destination.y
    next_septs = []
    try:
        north = maze[x-1][y]
        if dx == x-1 and dy == y:
            return closed_list
        #make sure everything is in bound
        if x-1 > 0:
            next_septs.append(north)
    except IndexError:
        pass
    try:
        east = maze[x][y+1]
        if dx == x and dy == y+1:
            return closed_list
        if y+1 > 0:
            next_septs.append(east)
    except IndexError:
        pass
    try:
        south = maze[x+1][y]
        if dx == x+1 and dy == y:
            return closed_list
        if x+1 > 0:
            next_septs.append(south)
    except IndexError:
        pass
    try:
        west = maze[x][y-1]
        if dx == x and dy == y-1:
            return closed_list
        if y-1 > 0:
            next_septs.append(west)
    except IndexError:
        pass
    next_step = sorted(next_septs, key=lambda x: x.distance)
    closed_list.append(next_step[0])
    return travel_lowest (matrix, next_step[0], closed_list, destination)

def belmman_ford(matrix):

    start = Node()
    start.x = 0
    start.y = 0

    desitnation = Node()
    desitnation.x = 2
    desitnation.y = 2


    matrix = add_weightings(matrix, desitnation)
    pns = []
    old_len = -1
    current_cost = 0
    current = start
    #check direction while there are still nodes to be checked
    # while len(pns) != old_len:
    #     old_len = len(pns)

    pns = check_direction(matrix, current, desitnation, pns, current_cost)
    for point in pns:
        current_cost = point.distance
        pns = check_direction(matrix, point, desitnation, pns, current_cost)

    closed_list = travel_lowest (matrix, start, [], desitnation)

    for point in closed_list:
        print (str(point.distance) + " to get to (" + str(point.x) + "," + str(point.y) + ")")

belmman_ford(matrix)
