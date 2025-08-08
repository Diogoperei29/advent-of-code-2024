from ast import Return
import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time

from numpy import isin

f = open("2024/4/input.txt").read().strip()
matrix = [[a for a in line] for line in f.split('\n')]

drr = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
diags = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
matrix_h = len(matrix)
matrix_w = len(matrix[0])

def isInBounds(x, y):
    if x < 0 or x >= matrix_w:
        return False
    if y < 0 or y >= matrix_h:
        return False
    return True

def checkForXMAS(x, y):
    currXMAS = 0
    
    if matrix[y][x] != 'X':
        return currXMAS

    for dr in drr:
        currX, currY = x, y
        foundXMAS = True
        for ch in 'MAS':
            currX += dr[0]
            currY += dr[1]
            if not (isInBounds(currX, currY) and ch == matrix[currY][currX]):
                foundXMAS = False
                break
        if foundXMAS:
            currXMAS += 1
     
    return currXMAS

def checkForX_MAS(x, y):
    
    if matrix[y][x] != 'A':
        return False
    
    currXchs = ''.join([matrix[y+diag[1]][x+diag[0]] for diag in diags])
    if currXchs in ['MMSS', 'SMMS', 'SSMM', 'MSSM']:
        return True
    
    return False

# Challenge 1
result = 0

for y in range(0, matrix_h):
    for x in range(0, matrix_w):
        currXMAS = checkForXMAS(x, y)
        if  currXMAS != 0:
            result += currXMAS

print("CH1: ",str(result))
# 2507

# Challenge 2
result = 0

for y in range(1, matrix_h-1):
    for x in range(1, matrix_w-1):
        if  checkForX_MAS(x, y):
            result += 1

print("CH2: ",str(result))
# 1969