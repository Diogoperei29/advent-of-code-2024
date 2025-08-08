import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time
sys.setrecursionlimit(10**6)

drr = [(0,-1),(1,0),(0,1),(-1,0)] # 0=up, 1=right, 2=down, 3=left
f = open("2024/6/input.txt").read().strip()
matrix = f.split('\n')
matrix_h = len(matrix)
matrix_w = len(matrix[0])

sx, sy = 0, 0
for y in range(matrix_h):
    for x in range(matrix_w):
        if matrix[y][x] == '^':
            sx, sy = x,y
            
def rot_dir(dir):
    return (dir+1)%4

def is_inbounds(x, y):
    if 0<=x<matrix_w and 0<=y<matrix_h:
        return True
    return False

# Challenge 1 
result = 0

dir = 0
cx, cy = sx, sy
vis_pos_p1 = set()

while is_inbounds(cx, cy):
    if (cx, cy) not in vis_pos_p1:
        result += 1
    vis_pos_p1.add((cx, cy))
    nx, ny = cx+drr[dir][0], cy+drr[dir][1]
    if not is_inbounds(nx, ny):
        break
    if matrix[ny][nx] == '#':
        dir = rot_dir(dir)
    else:  
        cx, cy = nx, ny

print("CH1: ",str(result))
# 5095

# Challenge 2
result = 0

vis_pos_p1.remove((sx, sy))
dir = 0
cx, cy = sx, sy

for pos in vis_pos_p1:

    dir = 0
    cx, cy = sx, sy
    vis_pos_dir = set()
    while is_inbounds(cx, cy):
        vis_pos_dir.add((cx, cy, dir))
        nx, ny = cx+drr[dir][0], cy+drr[dir][1]
        if not is_inbounds(nx, ny):
            break
        if matrix[ny][nx] == '#' or (nx == pos[0] and ny == pos[1]):
            dir = rot_dir(dir)
        else:  
            cx, cy = nx, ny
        if (cx, cy, dir) in vis_pos_dir:
            result += 1
            break


print("CH2: ",str(result))
# 1933