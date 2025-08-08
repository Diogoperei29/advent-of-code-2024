import enum
from operator import index
import sys
import re
import math
from itertools import combinations, product
import itertools
from collections import defaultdict, Counter, deque
from functools import cache
import copy
import time
from typing import final
from heapq import *

from sympy import product
sys.setrecursionlimit(10**6)
DR = [(0,-1), (1,0), (0,1), (-1,0)]
f = open("2024/21/test_input.txt").read().strip()
f = open("2024/21/input.txt").read().strip() # Overrides test input :)
CODES = f.split('\n')
CODEPAD = [['7', '8', '9'],
           ['4', '5', '6'], 
           ['1', '2', '3'], 
           [' ', '0', 'A']]

MOVEPAD_DICT = {'^':(1, 0),
                'A':(2, 0), 
                '<':(0, 1), 
                'v':(1, 1), 
                '>':(2, 1)}

MOVEPAD = [[' ', '^', 'A'], 
           ['<', 'v', '>']]

# hardcoded memoization lol
MOVES_ON_MOVEPAD = {
            'A': {
                'A': ['A'],
                '^': ['<','A'],
                '<': ['v','<','<','A'],
                '>': ['v','A'],
                'v': ['<','v','A']
            },
            '^': {
                'A': ['>','A'],
                '^': ['A'],
                '<': ['v','<','A'],
                '>': ['v','>','A'],
                'v': ['v','A']
            },
            '<': {
                'A': ['>','>','^','A'],
                '^': ['>','^','A'],
                '<': ['A'],
                '>': ['>','>','A'],
                'v': ['>','A']
            },
            'v': {
                'A': ['^','>','A'],
                '^': ['^','A'],
                '<': ['<','A'],
                '>': ['>','A'],
                'v': ['A']
            },
            '>': {
                'A': ['^','A'],
                '^': ['<','^','A'],
                '<': ['<','<','A'],
                '>': ['A'],
                'v': ['<','A']
            }
        }

def inbounds(x, y):
    H, W = len(CODEPAD), len(CODEPAD[0])
    if 0<=x<W and 0<=y<H:
        return True
    return False

def bfs_min_cost_paths(start, end):
    queue = deque([(start, [start], 0)])  # (current position, path, cost)
    min_cost_paths = []
    min_cost = float('inf')
    while queue:
        (x, y), path, cost = queue.popleft()

        if (x, y) == end:
            if cost < min_cost:
                min_cost = cost
                min_cost_paths = [path]
            elif cost == min_cost:
                min_cost_paths.append(path)
            continue

        for (dx, dy) in DR:
            nx, ny = x + dx, y + dy
            if inbounds(nx, ny) and (nx, ny) not in path:
                if CODEPAD[ny][nx] != ' ':
                    queue.append(((nx, ny), path + [(nx, ny)], cost + 1))

    return min_cost_paths

def get_codepad_moves(goal):
    (x, y) = (2, 3)
    
    all_possible_moves = []
   
    for g in goal:
        for yy, lin in enumerate(CODEPAD):
            if g in lin:
                gx, gy = lin.index(g), yy
                break
            
        min_cost_paths = bfs_min_cost_paths((x, y), (gx, gy))
        # Transform into symbols
        literalPaths = []
        for path in min_cost_paths:
            literalp = []
            (cx, cy) = path[0]
            for nx, ny in path:
                if nx < cx:
                    literalp.append('<')
                elif nx > cx:
                    literalp.append('>')
                elif ny < cy:
                    literalp.append('^')
                elif ny > cy:
                    literalp.append('v')
                cx, cy = nx, ny
            literalp.append('A')
            literalPaths.append(literalp)
        paths_with_switch = {}
        for path in literalPaths:
            switch = 0
            oldch = ' '
            for ch in path:
                if ch != oldch:
                    switch += 1
                oldch = ch
            if switch not in paths_with_switch:
                paths_with_switch[switch] = []
            paths_with_switch[switch].append(path)
        
        good_paths = paths_with_switch[min(paths_with_switch.keys())]   
        if all_possible_moves == []:
            all_possible_moves = good_paths
        else:
            all_possible_moves = [x + y for x, y in itertools.product(all_possible_moves, good_paths)]
        
        (x, y) = (gx, gy)
        
        #moves.append('A')
        
    return all_possible_moves

@cache
def find_len_of_moves(goal_ch, button, depth):
    
    if depth == 1:
        return len(MOVES_ON_MOVEPAD[button][goal_ch])
    
    sum_of_moves = 0
    curr_button = 'A'
    for goal_next in MOVES_ON_MOVEPAD[button][goal_ch]:
        sum_of_moves += find_len_of_moves(goal_next, curr_button, depth-1)
        curr_button = goal_next
    
    return sum_of_moves

# Challenge 1
result = 0

for code in CODES:

    initial_moves = get_codepad_moves(code)

    min_len = float('inf')
    for move in initial_moves:
        lenn = 0
        button = 'A'
        for ch in move:
            lenn += find_len_of_moves(ch, button, 2)
            button = ch
        if lenn < min_len:
            min_len = lenn
        
    result += int(code[:3])*min_len
 
print("CH1: ",str(result))
# 188384


# Challenge 2
result = 0

for code in CODES:

    initial_moves = get_codepad_moves(code)

    min_len = float('inf')
    for move in initial_moves:
        lenn = 0
        button = 'A'
        for ch in move:
            lenn += find_len_of_moves(ch, button, 25)
            button = ch
        if lenn < min_len:
            min_len = lenn
        
    result += int(code[:3])*min_len

print("CH2: ",str(result))
# 232389969568832