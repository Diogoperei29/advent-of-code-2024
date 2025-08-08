import enum
import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter, deque
from functools import cache
import copy
from tabnanny import check
import time
from typing import final

from numpy import empty
sys.setrecursionlimit(10**6)

f = open("2024/14/test_input.txt").read().strip()
f = open("2024/14/input.txt").read().strip()
ROBOTSTXT = [line for line in f.split('\n')]
ROBOTS = set()
H = 103 #HARDCODED 7
W = 101 #HARDCODED 11
SECS = 100 #HARDCODED 100

def inbounds(x, y):
    if 0<=x<W and 0<=y<H:
        return True
    return False

for rob in ROBOTSTXT:
    px = int(rob.split(' ')[0].split('=')[1].split(',')[0])
    py = int(rob.split(' ')[0].split('=')[1].split(',')[1])
    vx = int(rob.split('=')[2].split(',')[0])
    vy = int(rob.split('=')[2].split(',')[1])
    ROBOTS.add((px, py, vx, vy))

def empty_matrix(matrix):
    matrix = []
    for y in range(H):
        line = []
        for x in range(W):
            line.append('.')
        matrix.append(line)
    return matrix

def calc_pos_after_secs(robot, secs:int):
    npx = (robot[0] + robot[2]*secs)%W
    npy = (robot[1] + robot[3]*secs)%H
    return (npx, npy)

def calcQS(matrix):
    
    delim_Q_left = W//2
    delim_Q_right = W//2 if W%2==0 else W//2+1
    delim_Q_up = H//2
    delim_Q_down = H//2 if H%2==0 else H//2+1
    
    # if 11 -> 0-6, 7-12
    # if 10 -> 0-6, 6-11 
    Q1, Q2, Q3, Q4 = 0, 0, 0, 0
    
    for y in range(0, H):
        for x in range(0, W):
            if matrix[y][x]:
                
                if 0<=x<delim_Q_left and 0<=y<delim_Q_up:
                    Q1 += matrix[y][x]
                    
                if delim_Q_right<=x<W and 0<=y<delim_Q_up:
                    Q2 += matrix[y][x]
                    
                if 0<=x<delim_Q_left and delim_Q_down<=y<H:
                    Q3 += matrix[y][x]
                    
                if delim_Q_right<=x<W and delim_Q_down<=y<H:
                    Q4 += matrix[y][x]

    return Q1, Q2, Q3, Q4

# Challenge 1
result = 0
matrix = []
for y in range(H):
    line = []
    for x in range(W):
        line.append(0)
    matrix.append(line)
    
for rob in ROBOTS:
    (x,y) = calc_pos_after_secs(rob, SECS)
    if matrix[y][x] == 0:
        matrix[y][x] = 1
    else:
        matrix[y][x] += 1

Q1, Q2, Q3, Q4 = calcQS(matrix)
result = Q1*Q2*Q3*Q4

print("CH1: ",str(result))
# 208437768


def display(matrix, secs):
    print('++++++++++++++++++++++++++')
    print('secs: ', secs)
    print('++++++++++++++++++++++++++')
    for y in range(H):
        for x in range(W):
            print(matrix[y][x], end='')
        print()
            
def check_for_tree(matrix):
    
    for y in range(H):
        for x in range(W):
            if matrix[y][x] == '#':
                if inbounds(x-1, y+1) and matrix[y+1][x-1] == '#' and \
                   inbounds(x, y+1) and matrix[y+1][x] == '#' and \
                   inbounds(x+1, y+1) and matrix[y+1][x+1] == '#':
                       if inbounds(x-2, y+2) and matrix[y+2][x-2] == '#' and \
                          inbounds(x-1, y+2) and matrix[y+2][x-1] == '#' and \
                          inbounds(x, y+2) and matrix[y+2][x] == '#' and \
                          inbounds(x+1, y+2) and matrix[y+2][x+1] == '#' and \
                          inbounds(x+2, y+2) and matrix[y+2][x+2] == '#':
                            return True
    return False

def count_components(matrix, robs_pos):
    
    components = 0
    seen = set()
    to_explore = deque([])
    for pos in robs_pos:
        if pos in seen:
            continue
        seen.add(pos)
        to_explore.append(pos)
        components += 1
        while to_explore:
            exploring = to_explore.popleft()
            
            
            for dir in [(0,-1), (1,0), (0,1), (-1,0)]:
                nx, ny = exploring[0]+dir[0], exploring[1]+dir[1]
                if inbounds(nx, ny) and (nx, ny) not in seen and matrix[ny][nx] == '#':
                    to_explore.append((nx, ny))
                    seen.add((nx, ny))
                    
    return components
        
            

# Challenge 2
result = 0
matrix = []

for sec in range(0, 9999999):
    
    matrix = empty_matrix(matrix)
    robs_pos = set()
    
    for rob in ROBOTS:
        (x,y) = calc_pos_after_secs(rob, sec)
        robs_pos.add((x, y))
        
        if matrix[y][x] == '.':
            matrix[y][x] = '#'
        
    comps = count_components(matrix, robs_pos)
    if sec%1000 == 0:
        print(sec, comps)
    if comps <= 300:
        display(matrix, sec)
        # if check_for_tree(matrix):
        #     display(matrix, sec)
        
    #display(matrix, sec)



print("CH2: ",str(result))
#