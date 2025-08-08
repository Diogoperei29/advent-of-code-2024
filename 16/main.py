from ast import Return
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

from joblib import PrintTime
sys.setrecursionlimit(10**6)

drr = [(0,-1), (1,0), (0,1), (-1,0)]
f = open("2024/16/test_input.txt").read().strip()
f = open("2024/16/input.txt").read().strip()
matrix = [[a for a in line] for line in f.split('\n')]
H = len(matrix)
W = len(matrix[0])
def inbounds(x, y):
    if 0<=x<W and 0<=y<H:
        return True
    return False

START_X = 1
START_Y = H-2
END_X = W-2
END_Y = 1
matrix[H-2][1] = '.'
matrix[END_Y][END_X] = '.'

# Challenge 1
result = 0
BEST = 0
seen_pos = set()
path = []

cost_from_S_to_P = {}

heapify(path)
heappush(path, (0, START_X, START_Y, 1))

while path:
    cost, x, y, dir = heappop(path)
    #print(x, y, dir, cost)
    
    if (x, y, dir) in seen_pos:
        continue
    
    if (x, y, dir) not in cost_from_S_to_P:
        cost_from_S_to_P[(x, y, dir)] = cost
    
    seen_pos.add((x, y, dir))
    
    if x == END_X and y == END_Y and BEST == 0:
        
        BEST = cost
        result = cost
        continue # break for part 1, for part 2 we need to consider all possible places
    
    # Try to move forward
    ncost, nx, ny, ndir = cost+1, x+drr[dir][0], y+drr[dir][1], dir
    if matrix[ny][nx] == '.':
        heappush(path, (ncost, nx, ny, ndir))
    
    # Turn 90 CW
    ncost, nx, ny, ndir = cost+1000, x, y, (dir+1)%4
    heappush(path, (ncost, nx, ny, ndir))
    
    # Turn 90 CCW
    ncost, nx, ny, ndir = cost+1000, x, y, (dir+3)%4
    heappush(path, (ncost, nx, ny, ndir))

print("CH1: ",str(result))
# 115500

# Challenge 2
result = 0
seen_pos = set()
path = []

cost_from_P_to_E = {}

heapify(path)
# Can only end pointing N or E
heappush(path, (0, END_X, END_Y, 0))
while path:
    cost, x, y, dir = heappop(path)
    
    if (x, y, dir) in cost_from_S_to_P and (x, y, dir) not in cost_from_P_to_E:
        cost_from_P_to_E[(x, y, dir)] = cost
        
    if (x, y, dir) in seen_pos:
        continue
    
    seen_pos.add((x, y, dir))
    
    # Try to move BACKWARDS, but KEEP DIRECTION FORWARD!!!!
    ncost, nx, ny, ndir = cost+1, x+drr[(dir+2)%4][0], y+drr[(dir+2)%4][1], dir
    if matrix[ny][nx] == '.':
        heappush(path, (ncost, nx, ny, ndir))
    
    # Turn 90 CW
    ncost, nx, ny, ndir = cost+1000, x, y, (dir+1)%4
    heappush(path, (ncost, nx, ny, ndir))
    
    # Turn 90 CCW
    ncost, nx, ny, ndir = cost+1000, x, y, (dir+3)%4
    heappush(path, (ncost, nx, ny, ndir))

# Is part of best path is Path S->Point + Point->E is equal to the best path calculated in P1
SITS = set()
for poss_pos in cost_from_S_to_P:
    if (cost_from_S_to_P[poss_pos]+cost_from_P_to_E[poss_pos]) == BEST:
        if (poss_pos[0], poss_pos[1]) not in SITS: 
            SITS.add((poss_pos[0], poss_pos[1]))
            
result = len(SITS)

print("CH2: ",str(result))
# 679