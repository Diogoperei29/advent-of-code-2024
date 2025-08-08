import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time
sys.setrecursionlimit(10**6)

#f = open("test_input.txt").read().strip()
f = open("2024/8/input.txt").read().strip()
matrix = f.split('\n')
H = len(matrix)
W = len(matrix[0])


def inbounds(x, y):
    if 0<=x<W and 0<=y<H:
        return True
    return False

nodes = {}
for y in range(H):
    for x in range(W):
        if matrix[y][x] != '.':
            if matrix[y][x] not in nodes:
                nodes[matrix[y][x]] = set()
            nodes[matrix[y][x]].add((x, y))
            
# Challenge 1
result = 0

antinodes = set()
for node in nodes:
    combs = combinations(nodes[node], 2)

    for cm in combs:
        x0, y0, x1, y1 = cm[0][0], cm[0][1], cm[1][0], cm[1][1]
        difx = x0 - x1
        dify = y0 - y1

        new_anti_0 = (x0 + difx, y0 + dify)
        if inbounds(*new_anti_0) and new_anti_0 not in antinodes:
            antinodes.add(new_anti_0)
            
        new_anti_1 = (x1 - difx, y1 - dify)
        if inbounds(*new_anti_1) and new_anti_1 not in antinodes:
            antinodes.add(new_anti_1)

result = len(antinodes)

print("CH1: ",str(result))
# 249

# Challenge 2
result = 0

antinodes = set()
for node in nodes:
    combs = combinations(nodes[node], 2)

    for cm in combs:
        x0, y0, x1, y1 = cm[0][0], cm[0][1], cm[1][0], cm[1][1]
        difx = x0 - x1
        dify = y0 - y1
        
        new_anti_0 = (x1 + difx, y1 + dify)
        while(inbounds(*new_anti_0)):
            if inbounds(*new_anti_0) and new_anti_0 not in antinodes:
                antinodes.add(new_anti_0)
            new_anti_0 = (new_anti_0[0] + difx, new_anti_0[1] + dify)
  
        new_anti_1 = (x0 - difx, y0 - dify)
        while(inbounds(*new_anti_1)):
            if inbounds(*new_anti_1) and new_anti_1 not in antinodes:
                antinodes.add(new_anti_1)
            new_anti_1 = (new_anti_1[0] - difx, new_anti_1[1] - dify)

result = len(antinodes)

print("CH2: ",str(result))
# 905