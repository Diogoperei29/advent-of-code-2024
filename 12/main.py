import enum
import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter, deque
from functools import cache
import heapq
import copy
import time
from typing import final
sys.setrecursionlimit(10**6)

drr = [(0,-1), (1,0), (0,1), (-1,0)]
drr_h = [(0,-1), (0,1)]
drr_w = [(1,0), (-1,0)]

f = open("2024/12/test_input.txt").read().strip()
f = open("2024/12/input.txt").read().strip()
matrix = [[a for a in line] for line in f.split('\n')]
H = len(matrix)
W = len(matrix[0])
def inbounds(x, y):
    if 0<=x<W and 0<=y<H:
        return True
    return False

def perimeter_of_plant(x, y):
    ans = 0
    for (xi, yi) in drr:
        if (not inbounds(x+xi, y+yi)) or matrix[y+yi][x+xi] != matrix[y][x]:
            ans += 1
    return ans

def explore_plants_perim(x, y, explored_plants:set):
    
    total_perim = 0
    explored_plants.add((x, y))
    plants_to_explore = deque([(x, y)])
    
    while plants_to_explore:
        (cx, cy) = plants_to_explore.popleft()
        
        for (xi, yi) in drr:
            nx, ny = cx+xi, cy+yi
            if (nx, ny) in explored_plants:
                continue
            if inbounds(nx, ny) and matrix[ny][nx] == matrix[y][x]:
                plants_to_explore.append((nx, ny))
                explored_plants.add((nx, ny))
            else:
                total_perim += 1
        
    return total_perim

def explore_plants_sides(x, y, explored_plants:set):
    
    explored_plants.add((x, y))
    plants_to_explore = deque([(x, y)])
    outs = dict()
    
    while plants_to_explore:
        (cx, cy) = plants_to_explore.popleft()
        
        for (xi, yi) in drr:
            nx, ny = cx+xi, cy+yi
            if (nx, ny) in explored_plants:
                continue
            if inbounds(nx, ny) and matrix[ny][nx] == matrix[y][x]:
                plants_to_explore.append((nx, ny))
                explored_plants.add((nx, ny))
            else:
                if (xi, yi) not in outs:
                    outs[(xi, yi)] = set()
                outs[(xi, yi)].add((nx, ny))
                
    sides = 0          
    for k, vdr in outs.items():
        
        
        visited_pos = set()
        
        for (cx, cy) in vdr:

            if (cx, cy) in visited_pos:
                continue
            
            sides += 1
            visited_pos.add((cx, cy))
            outs_to_explore = deque([(cx, cy)])

            while(outs_to_explore):
                (tx, ty) = outs_to_explore.popleft()
                
                for (xi, yi) in drr:
                    nx, ny = tx+xi, ty+yi
                    if (nx, ny) in visited_pos or (nx, ny) not in outs[k]:
                        continue
                    
                    outs_to_explore.append((nx, ny))
                    visited_pos.add((nx, ny))

    return sides


# Challenge 1
result = 0

explored = []
for y in range(H):
    for x in range(W):
        if (x, y) not in explored:
            new_explored = set()
            add = explore_plants_perim(x, y, new_explored)
            #print(matrix[y][x],' area: ', len(new_explored), ' perim: ', add)
            result += add*(len(new_explored))
            explored += new_explored
    
print("CH1: ",str(result))
# 1467094

# Challenge 2
result = 0

explored = []
for y in range(H):
    for x in range(W):
        if (x, y) not in explored:
            new_explored = set()
            add = explore_plants_sides(x, y, new_explored)
            #print(matrix[y][x],' area: ', len(new_explored), ' sides: ', add)
            result += add*(len(new_explored))
            explored += new_explored
    
print("CH2: ",str(result))
#