import enum
import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter, deque
from functools import cache
import copy
import time
from typing import final
from heapq import *
sys.setrecursionlimit(10**6)
drr = [(0,-1), (1,0), (0,1), (-1,0)]

f = open("2024/18/test_input.txt").read().strip()
f = open("2024/18/input.txt").read().strip() # Overrides test input :)
H = 70+1 # 6+1 # 70+1
W = 70+1 # 6+1 # 70+1
NBYTES_P1 = 1024 # 12 # 1024
BYTES = []
matrix = [[0 for x in range(W)] for y in range(H)]
for i, line in enumerate(f.split('\n')):
    x, y = int(line.split(',')[0]), int(line.split(',')[1])
    BYTES.append((x, y))
    if i < NBYTES_P1:
        matrix[y][x] = 1
    
Sx, Sy = 0, 0
Ex, Ey = W-1, H-1


class Node:
    def __init__(self, position:tuple, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
        

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    # Force comparison between 2 nodes to be on position
    def __hash__(self):
        return hash(self.position)

def heuristic(a:Node, b:Node):
    # Manhattan distance
    return abs(a.position[0] - b.position[0]) + abs(a.position[1] - b.position[1])

def A_Star(Sx, Sy, Ex, Ey, matrix):
    start_node = Node((Sx, Sy))
    end_node = Node((Ex, Ey))
    path = []
    exploration_queue = []
    explored = set()
    heappush(exploration_queue, start_node)

    while (exploration_queue):
        curr_node = heappop(exploration_queue)
        explored.add(curr_node)
        
        if curr_node == end_node:
            tmp_node = curr_node
            while tmp_node:
                path.append(tmp_node.position)
                tmp_node = tmp_node.parent
            return path[::-1]
        
        for dr in drr:
            nx, ny = curr_node.position[0]+dr[0], curr_node.position[1]+dr[1]
            new_node = Node((nx, ny), curr_node)
            
            if inbounds(nx, ny) and new_node not in explored and matrix[ny][nx] == 0:
                new_node.g = curr_node.g + 1
                new_node.h = heuristic(new_node, end_node)
                new_node.f = new_node.g + new_node.h
                
                heappush(exploration_queue, new_node)
                
    return path

def inbounds(x, y):
    if 0<=x<W and 0<=y<H:
        return True
    return False

def print_path(path, matrix):
    for y in range(H):
        for x in range(W):
            if (x, y) in path:
                print('O',end='')
            elif matrix[y][x] == 0:
                print('.',end='')
            elif matrix[y][x] == 1:
                print('#',end='')
        print()
        

# Challenge 1
result = 0

path = A_Star(Sx, Sy, Ex, Ey, matrix)
            
print('path: ', path)
result = len(path)-1
print_path(path, matrix)
print("CH1: ",str(result))
# 234

# Challenge 2
result = 0

for byt in range(NBYTES_P1-1, len(BYTES)):
    bx, by = BYTES[byt][0], BYTES[byt][1]
    matrix[by][bx] = 1
    
    # test if it interfeeres with current existing path
    if (bx, by) in path:
        print('testing: ', (bx, by))
        path = A_Star(Sx, Sy, Ex, Ey, matrix)
        
    if path == []:
        result = (bx, by)
        break

print("CH2: ",str(result))
#