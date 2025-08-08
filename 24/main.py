from doctest import FAIL_FAST
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
sys.setrecursionlimit(10**6)

f = open("2024/24/test_input.txt").read().strip()
f = open("2024/24/input.txt").read().strip() # Overrides test input :)

# # # # # # # # # # # #
#  PROCESS INPUT HERE #
# # # # # # # # # # # #
inputs_lines, gates_lines = f.split('\n\n')

GATES = set()
WIRES = {}
for line in gates_lines.split('\n'):
    key = 'AND' if 'AND' in line else ('XOR' if 'XOR' in line else 'OR')
    A = line.split(f' {key} ')[0]
    B = line.split(f' {key} ')[1].split(' -> ')[0]
    C = line.split(f' {key} ')[1].split(' -> ')[1]

    GATES.add((A, B, key, C))
    if A not in WIRES:
        WIRES[A] = None
    if B not in WIRES:
        WIRES[B] = None
    if C not in WIRES:
        WIRES[C] = None
        
for line in inputs_lines.split('\n'):
    key, val = line.split(': ')
    WIRES[key] = True if val == '1' else False

WIRES = dict(sorted(WIRES.items()))

def runGates(wires, gates):
    for _ in range(len(gates)):
    
        seen_all = True
        for (a, b, oper, out) in gates:
            if wires[a] != None and wires[b] != None:
                match oper:
                    case 'AND': wires[out] = wires[a] and wires[b]
                    case 'OR' : wires[out] = wires[a] or  wires[b]
                    case 'XOR': wires[out] = wires[a] !=  wires[b]
            else:
                seen_all = False
        if seen_all:
            break

    binary_output = ''
    for wire in wires:
        if wire.startswith('z'):
            binary_output += '1' if wires[wire] else '0'
    return binary_output



######################################################################## Challenge 1
result = 0
STAT_ST_TIME = time.perf_counter()
# # # # # # # # # # # #
#  START PART 1 HERE! #
# # # # # # # # # # # #

gates = copy.deepcopy(GATES)
wires = copy.deepcopy(WIRES)

binary_output = runGates(wires, gates)

binary_output = ''.join(reversed(binary_output))
result = int(binary_output, 2)


# # # # # # # # # # # #
#  STOP PART 1 HERE!  #
# # # # # # # # # # # #
STAT_EN_TIME = time.perf_counter() 
STAT_VR_ELAPSEDTIME = (STAT_EN_TIME - STAT_ST_TIME)*1000.0
print(f'[STAT TIME P1] Part 1 took [{STAT_VR_ELAPSEDTIME:.6f}] ms')
print("CH1: ",str(result), end='\n\n')
# RESULT:


######################################################################## Challenge 2
result = 0
STAT_ST_TIME = time.perf_counter() 
# # # # # # # # # # # #
#  START PART 2 HERE! #
# # # # # # # # # # # #

def calc_difs(a, b):
    ans = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ans += 1
    return ans

x_binary = ''
y_binary = ''
for wire in WIRES:
    if wire.startswith('x'):
        x_binary += str(1 if WIRES[wire] else 0)
    if wire.startswith('y'):
        y_binary += str(1 if WIRES[wire] else 0)
x_binary = ''.join(reversed(x_binary))
y_binary = ''.join(reversed(y_binary))   
x_val = int(x_binary, 2)
y_val = int(y_binary, 2)
expected_binary = ''.join(reversed(bin(x_val+y_val)[2:]))

gates = copy.deepcopy(GATES)
wires = copy.deepcopy(WIRES)
current_binary_output = runGates(wires, gates)

print(expected_binary)
print(current_binary_output)

print(calc_difs(expected_binary, current_binary_output))











# # # # # # # # # # # #
#  STOP PART 2 HERE!  #
# # # # # # # # # # # #
STAT_EN_TIME = time.perf_counter() 
STAT_VR_ELAPSEDTIME = (STAT_EN_TIME - STAT_ST_TIME)*1000.0
print(f'[STAT TIME P2] Part 2 took [{STAT_VR_ELAPSEDTIME:.6f}] ms')
print("CH2: ",str(result), end='\n\n')
# RESULT:
