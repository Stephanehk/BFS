#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 20:18:13 2019

@author: 2020shatgiskessell
"""

import pprint
from numpy.random import choice

def generate_maze (size, difficulty):
    #all the maze components (can add more)
    components = [".","W"]
    #weightings for each diffiuclty
    easy = [0.9,0.1]
    medium = [0.7,0.3]
    hard = [0.6,0.4]

    #create maze of 0s
    maze = [[0 for i in range(size)]for j in range(size)]
    for i in range (size):
        for j in range (size):
            #randomley chose . or ,to populate maze (based on weightings)
            if difficulty == "hard":
                component = components[choice([0,1],p=hard)]
            elif difficulty == "medium":
                component = components[choice([0,1],p=medium)]
            elif difficulty == "easy":
                component = components[choice([0,1],p=easy)]
            maze[i][j] = component
    return maze

def possible_paths(matrix, node):
    possible_paths = []
    #get x,y coordinates from node
    x = node[0]
    y = node[1]
    length = len(matrix)
    #check N,S,W,E,NE,NW,SE,SW
    for x,y in (x, y+1), (x, y-1), (x+1, y), (x-1, y), (x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1):
        if x >= 0 and x < length and y >= 0 and y < length:
            #add to possible paths if the current direction is clear
            if matrix[x][y] == '.':
                possible_paths.append([x,y])
    return possible_paths

def bfs(maze, node, goal):

    queue = [[node]]
    visited = []
    #while there are still unvisited paths
    while queue:
        path = queue.pop(0)
        node = path[-1]
        #if there is a new node
        if node not in visited:
            #add to list of visited
            visited.append(node)
            #get all possible paths from given node
            possible_paths_ = possible_paths(maze, node)
            #for every position in each possible path
            for position in possible_paths_:
                #keep track of position and path
                path_found = list(path)
                path_found.append(position)
                queue.append(path_found)
                #if the position is the goal
                if position == goal:
                    for x,y in path_found:
                        maze[x][y] = 'x'
                    return True
    return False

def bfs(maze):
    matrix = list(map(list, maze.splitlines()))
    stack = [[0, 0]]
    length = len(matrix)
    while len(stack):
      x, y = stack.pop()
      if matrix[x][y] == '.':
        matrix[x][y] = 'x'
        for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
          if 0 <= x < length and 0 <= y < length:
            stack.append((x, y))
    if matrix[length-1][length-1] == 'x':
        return True
    else:
        return False

maze = generate_maze(5,"medium")
pprint.pprint(bfs(maze,[0,0], [4,4]))
