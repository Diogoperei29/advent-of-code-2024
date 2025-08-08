import enum
from os import close
import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter, deque
from functools import cache
import copy
import time
import operator
from typing import final
from heapq import *
sys.setrecursionlimit(10**6)
DR = [(0,-1), (1,0), (0,1), (-1,0)]

f = open("2024/20/test_input.txt").read().strip()
f = open("2024/20/input.txt").read().strip() # Overrides test input :)
matrix = [[(a) for a in line] for line in f.split('\n')]
H = len(matrix)
W = len(matrix[0])
    
Sx, Sy = -1, -1
Ex, Ey = -1, -1
for y in range(H):
    for x in range(W):
        if matrix[y][x] == 'S':
            Sx, Sy = x, y
        elif matrix[y][x] == 'E':
            Ex, Ey = x, y
print(f'S: ({Sx},{Sy})', end=' ')
print(f'E: ({Ex},{Ey})')

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
    return None

def close_inbounds(x, y):
    if 1<=x<W-1 and 1<=y<H-1:
        return True
    return False

def inbounds(x, y):
    if 0<=x<W and 0<=y<H:
        return True
    return False

def print_path(path, matrix, cheats):
    for y in range(H):
        for x in range(W):
            if (x, y) in cheats:
                if (x, y) == cheats[0]:
                    print('1',end='')
                else:
                    print('2',end='')
            #elif (x, y) in path:
            #    #print('O',end='')
            elif matrix[y][x] == '.':
                print('.',end='')
            elif matrix[y][x] == '#':
                print('#',end='')
            else:
                print('H',end='')
        print()

# Challenge 1
result = 0

STAT_ST_TIME = time.perf_counter()
orig_path = A_Star(Sx, Sy, Ex, Ey, matrix)
orig_picosecs = len(orig_path)-1
print('orig len: ', orig_picosecs)

SAVED = {}

for tt, (x, y) in enumerate(orig_path):
    for dr in DR:
        nx, ny = x+dr[0], y+dr[1]
        if close_inbounds(nx, ny) and matrix[ny][nx] == '#':
            for ddd, ddr in enumerate(DR):
                if dr == DR[(ddd+2)%4]:
                    continue # skip if going backwards
                nnx, nny = nx+ddr[0], ny+ddr[1]
                
                if close_inbounds(nnx, nny) and (nnx, nny) in orig_path:
                    pos_in_path = orig_path.index((nnx, nny))
                    if pos_in_path < tt: # skip if shortcut to behind
                        continue
                    
                    # Continue down the path from current pos to see how many spots were saved
                    saved = 0
                    for ttt in range(tt, len(orig_path)):
                        if orig_path[ttt] != (nnx, nny):
                            saved += 1
                        if orig_path[ttt] == (nnx, nny):
                            break
                    saved -= 2 # remove the 2 new paths that are added from cheat
                    if 0 < saved <= 100:
                        result += 1
                        
                            
                        

#for k in SAVED:
#    print(k, SAVED[k])
STAT_EN_TIME = time.perf_counter() 
STAT_VR_ELAPSEDTIME = (STAT_EN_TIME - STAT_ST_TIME)*1000.0
print(f'[STAT TIME P1] Part 1 took [{STAT_VR_ELAPSEDTIME:.6f}] ms')
print("CH1: ",str(result))
#

# Challenge 2
result = 0





print("CH2: ",str(result))
#

# 1358
# 1005853