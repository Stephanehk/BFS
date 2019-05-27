import numpy as np

class Node:
    def __init__(self, xcoordinate= None, ycoordinate= None, h=None, g=None, cost=None):
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate
        self.h = h
        self.g = g
        self.cost = cost

    def __repr__(self):
        return repr((self.xcoordinate, self.ycoordinate, self.h, self.g, self.cost))

# . = empty positons
# W = walls
#https://www.codewars.com/kata/path-finder-number-1-can-you-reach-the-exit/train/python

#a = "\n".join([
#  ".W.",
#  ".W.",
#  "..."
#])
#
#b = "\n".join([
#  ".W.",
#  ".W.",
#  "W.."
#])
#
#c = "\n".join([
#  "......",
#  "......",
#  "......",
#  "......",
#  "......",
#  "......"
#])
#
#d = "\n".join([
#  "......",
#  "......",
#  "......",
#  "......",
#  ".....W",
#  "....W."
#])

a_a = [[".","W","."],
       [".","W","."],
       [".",".","."]]

b_a = [[".","W","."],
       [".",".","."],
       ["W",".","."]]

c_a = [["0","W","3", "5","5","3"],
       ["1","2","11", "W","6","7"],
       ["2","3","W", "W","5","W"],
       ["12","5","1", "1","2","4"],
       ["4","1","2", "W","3","W"],
       ["2","1","3", "9","11","0"]]

d_a = [[".",".",".", ".",".","."],
       [".",".",".", ".",".","."],
       [".",".",".", ".",".","."],
       [".",".",".", ".",".","."],
       [".",".",".", ".",".","W"],
       [".",".",".", ".","W","."]]

e_a = [[".",".",".", ".",".","."],
       [".","W",".", ".",".","."],
       [".",".","W", ".","W","."],
       [".","W",".", "W",".","."],
       [".",".",".", ".",".","W"],
       [".",".",".", ".",".","."]]

def add_weightings (maze,destination, start):
    for i in range (len(maze)):
        for j in range (len(maze)):
            if maze[i][j] != "W":
                current = Node()
                current.xcoordinate = i
                current.ycoordinate = j
                #calculate distance from current node to end node
                #h = np.sqrt(np.power(current.xcoordinate-destination.xcoordinate,2)+np.power(current.ycoordinate -destination.ycoordinate,2))
                #calculate between nodes
                #10 if its u,d,r,l
                #15 if its diagonals (add later)
                #g = 10
                #assign values
                #current.h = h
                #current.g = g
                #calcualte cost
                current.cost = int(maze[i][j])
                maze[i][j] = current
    maze[destination.xcoordinate][destination.ycoordinate] = "D"
    return maze

possible_next_steps = []
closed_list = []

def dijsktra (maze, current, destination, start, possible_next_steps):
    #get all the possible next steps from given node
    x = current.xcoordinate
    y = current.ycoordinate

    #print current node coordinate
    print ("(" + str(x) + "," + str(y) + ") ->")

    #check if destination is reached
    if x == destination.xcoordinate and y == destination.ycoordinate:
        return "destination reached"
    try:
        north = maze[x-1][y]
        #make sure everything is in bounds
        if x-1 > 0 and north != "W" and north not in closed_list:
            #if everything checks out, add direction to possible_next_steps
            possible_next_steps.append(north)
    except IndexError:
        pass
    try:
        east = maze[x][y+1]
        if y+1 > 0 and east != "W" and east not in closed_list:
            possible_next_steps.append(east)
    except IndexError:
        pass
    try:
        south = maze[x+1][y]
        if x+1 > 0  and south != "W" and south not in closed_list:
            possible_next_steps.append(south)
    except IndexError:
        pass
    try:
        west = maze[x][y-1]
        if y-1 > 0  and west != "W" and west not in closed_list:
            possible_next_steps.append(west)
    except IndexError:
        pass

    #check to see if destination is reached
    if "D" in possible_next_steps:
        print ("D")
        return
    possible_next_steps = sorted(possible_next_steps, key=lambda x: x.cost)
    next_step = possible_next_steps[0]
    #remove next step from open list
    possible_next_steps.remove(next_step)
    closed_list.append(next_step)
    dijsktra (maze, next_step, destination, start, possible_next_steps)

#set starting point at (0,0)
start = Node()
start.xcoordinate = 0
start.ycoordinate = 0

#set ending point at (2,2)
destination = Node()
destination.xcoordinate = 5
destination.ycoordinate = 5

weighted_maze = add_weightings(c_a, destination, start)
#Perfom a star
dijsktra (weighted_maze, start, destination, start, possible_next_steps)
