from ast import List
import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time
sys.setrecursionlimit(10**6)
drr = [(0,-1), (1,0), (0,1), (-1,0)]
f = open("2024/10/test_input.txt").read().strip()
f = open("2024/10/input.txt").read().strip()
matrix = [[int(a) for a in line] for line in f.split('\n')]
H = len(matrix)
W = len(matrix[0])


def inbounds(x, y):
    if 0<=x<W and 0<=y<H:
        return True
    return False

def get_trailheads_bfs(val, x, y, visited):
    if val == 9:
        return 1
    ans = 0
    for (xi, yi) in drr:
        nx, ny = x+xi, y+yi
        if inbounds(nx, ny) and matrix[ny][nx] == val + 1 and (nx, ny) not in visited:
            visited.append((nx, ny))
            ans += get_trailheads_bfs(val + 1, nx, ny, visited)
    return ans

def get_trailheads_dfs(val, x, y):
    if val == 9:
        return 1
    ans = 0
    for (xi, yi) in drr:
        nx, ny = x+xi, y+yi
        if inbounds(nx, ny) and matrix[ny][nx] == val + 1:
            ans += get_trailheads_dfs(val + 1, nx, ny)
    return ans

# Challenge 1
result = 0

for y in range(H):
    for x in range(W):
        if matrix[y][x] == 0:
            result += get_trailheads_bfs(0, x, y, [])

print("CH1: ",str(result))
# 550

# Challenge 2
result = 0

for y in range(H):
    for x in range(W):
        if matrix[y][x] == 0:
            result += get_trailheads_dfs(0, x, y)

print("CH2: ",str(result))
# 1255