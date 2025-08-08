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

sys.setrecursionlimit(10**6)

f = open("2024/15/test_input.txt").read().strip()
f = open("2024/15/input.txt").read().strip()
MATRIX_TXT = f.split('\n\n')[0]
DIRS = {'^':(0,-1), '>':(1,0), 'v':(0,1), '<':(-1,0)}
PATH = f.split('\n\n')[1].replace('\r', '').replace('\n', '')
MATRIX = [list(line) for line in MATRIX_TXT.split('\n')]
H = len(MATRIX)
W = len(MATRIX[0])

def find_rob_pos(matrix):
    w, h = len(matrix[0]), len(matrix)
    for y in range(1, h-1):
        for x in range(2, w-2):
            if matrix[y][x] == '@':
                return (x, y)
            
def inbounds(x, y):
    if 0<=x<W and 0<=y<H:
        return True
    return False

def update_matrix(matrix, pos, inst):
    (x, y) = pos
    (xi, yi) = DIRS[inst]

    nx, ny = x+xi, y+yi
    if matrix[ny][nx] == '.':
        return matrix, (nx, ny)

    if matrix[ny][nx] == '#':
        return matrix, (x, y)
    
    if matrix[ny][nx] == 'O':
        tx, ty = nx+xi, ny+yi
        while matrix[ty][tx] == 'O':
            tx, ty = tx+xi, ty+yi
            
        if matrix[ty][tx] == '#':
            return matrix, (x, y)
        
        if matrix[ty][tx] == '.':
            matrix[ty][tx] = 'O'
            matrix[ny][nx] = '.'
            return matrix, (nx, ny)
    
    print('weird shit happened')
    return matrix, (x, y)

def widenificate_matrix(matrix):
    new_matrix = []
    for y in range(H):
        new_line = []
        for x in range(W):
            if matrix[y][x] == '#':
                new_line.append('#')
                new_line.append('#')
            elif matrix[y][x] == 'O':
                new_line.append('[')
                new_line.append(']')
            elif matrix[y][x] == '.':
                new_line.append('.')
                new_line.append('.')
            elif matrix[y][x] == '@':
                new_line.append('@')
                new_line.append('.')
        new_matrix.append(new_line)
        
    return new_matrix

def update_matrix_WIDEVER(matrix, pos, inst):
    (x, y) = pos
    (xi, yi) = DIRS[inst]
    nx, ny = x+xi, y+yi
    
    if matrix[ny][nx] == '.':
        return matrix, (nx, ny)

    if matrix[ny][nx] == '#':
        return matrix, (x, y)
    
    if matrix[ny][nx] in '[]':
    
        # calcs are dif with side moves
        if inst in '<>':
            tx, ty = nx+xi, ny+yi
            while matrix[ty][tx] in '[]':
                tx, ty = tx+xi, ty+yi
            if matrix[ty][tx] == '#':
                return matrix, (x, y)
            
            if matrix[ty][tx] == '.':
                while (ty != y or tx != x):
                    matrix[ty][tx] = matrix[ty-yi][tx-xi]
                    tx, ty = tx-xi, ty-yi
                return matrix, (nx, ny)
        
        else:
            boxes_to_move = deque([])
            boxes_to_check = deque([])
            if matrix[ny][nx] == '[':
                boxes_to_move.append(((nx, ny),(nx+1, ny)))
                boxes_to_check.append(((nx, ny),(nx+1, ny)))
            else:
                boxes_to_move.append(((nx-1, ny),(nx, ny)))
                boxes_to_check.append(((nx-1, ny),(nx, ny)))
                
            deepest_depth =  ny
            
            # BFS to check boxes
            while boxes_to_check:
                box_checking = boxes_to_check.popleft()
                cx1, cy1, cx2, cy2 = box_checking[0][0], box_checking[0][1], box_checking[1][0], box_checking[1][1]
                tx1, ty1, tx2, ty2 = cx1+xi, cy1+yi, cx2+xi, cy2+yi
                
                if matrix[ty1][tx1] == '[':
                    boxes_to_move.append(((tx1, ty1),(tx2, ty2)))
                    boxes_to_check.append(((tx1, ty1),(tx2, ty2)))
                    continue
                
                if matrix[ty1][tx1] == ']':
                    boxes_to_move.append(((tx1-1, ty1),(tx1, ty1)))
                    boxes_to_check.append(((tx1-1, ty1),(tx1, ty1)))
                if matrix[ty2][tx2] == '[':
                    boxes_to_move.append(((tx2, ty2),(tx2+1, ty2)))
                    boxes_to_check.append(((tx2, ty2),(tx2+1, ty2)))
            
            # first check if last layer can be moved
            boxes_to_check_to_move = copy.deepcopy(boxes_to_move)
            while boxes_to_check_to_move:
                box_checking = boxes_to_check_to_move.pop()
                cx1, cy1, cx2, cy2 = box_checking[0][0], box_checking[0][1], box_checking[1][0], box_checking[1][1]
                tx1, ty1, tx2, ty2 = cx1+xi, cy1+yi, cx2+xi, cy2+yi
                
                if matrix[ty1][tx1] == '#' or matrix[ty2][tx2] == '#':
                    return matrix, (x, y)
  
            # reverse the bfs and try to move boxes 
            while boxes_to_move:
                box_checking = boxes_to_move.pop()
                cx1, cy1, cx2, cy2 = box_checking[0][0], box_checking[0][1], box_checking[1][0], box_checking[1][1]
                tx1, ty1, tx2, ty2 = cx1+xi, cy1+yi, cx2+xi, cy2+yi
                
                if matrix[ty1][tx1] == '.' and matrix[ty2][tx2] == '.':
                    matrix[ty1][tx1] = '['
                    matrix[ty2][tx2] = ']'
                    matrix[cy1][cx1] = '.'
                    matrix[cy2][cx2] = '.'
                
            return matrix, (nx, ny)
    
    print('weird shit happened')
    return matrix, (x, y)             
        
def print_matrix(matrix):
    
    for l in matrix:
        print(''.join(l))
        
# Challenge 1
result = 0

matrix = MATRIX.copy()
pos = find_rob_pos(matrix)
matrix[pos[1]][pos[0]] = '.'

for path in PATH:
    matrix, pos = update_matrix(matrix, pos, path)
    
for y in range(1, H-1):
    for x in range(1, W-1):
        if MATRIX[y][x] == 'O':
            result += (100*y+x)
#print_matrix(matrix)

print("CH1: ",str(result))
# 1577255

# Challenge 2
result = 0
DIRS = {'^':(0,-1), '>':(1,0), 'v':(0,1), '<':(-1,0)}
PATH = f.split('\n\n')[1].replace('\r', '').replace('\n', '')
MATRIX = [list(line) for line in MATRIX_TXT.split('\n')]

matrix = widenificate_matrix(MATRIX)
w, h = len(matrix[0]), len(matrix)
print_matrix(matrix)
pos = find_rob_pos(matrix)
matrix[pos[1]][pos[0]] = '.'

for path in PATH:
    matrix, pos = update_matrix_WIDEVER(matrix, pos, path)
    matrix_print = copy.deepcopy(matrix)
    matrix_print[pos[1]][pos[0]] = '@'
    # print('dir: ', path)
    # print_matrix(matrix_print)
    # input()

print_matrix(matrix_print)

for y in range(1, h-1):
    for x in range(2, w-2):
        if matrix[y][x] == '[':
            result += (100*y+x)
print("CH2: ",str(result))
# 1597035