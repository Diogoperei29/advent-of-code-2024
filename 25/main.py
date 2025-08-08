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

f = open("2024/25/test_input.txt").read().strip() 
f = open("2024/25/input.txt").read().strip() # Overrides test input :)

# # # # # # # # # # # #
#  PROCESS INPUT HERE #
# # # # # # # # # # # #

KEYS = []
LOCKS = []
SCHEMS = [l.split('\n') for l in f.split('\n\n')]
H, W = len(SCHEMS[0]), len(SCHEMS[0][0])
for schem in SCHEMS:
    vals = [0 for _ in range(W)]
    if schem[0] == '#####':
        for y in range(1, H-1):
            for x in range(W):
                if schem[y][x] == '.':
                    vals[x] += 1
        LOCKS.append(tuple(vals))
    else:
        for y in range(1, H-1):
            for x in range(W):
                if schem[y][x] == '#':
                    vals[x] += 1
        KEYS.append(tuple(vals))

######################################################################## Challenge 1
result = 0
STAT_ST_TIME = time.perf_counter()
# # # # # # # # # # # #
#  START PART 1 HERE! #
# # # # # # # # # # # #

for lock in LOCKS:
    for key in KEYS:
        fit = True
        for x in range(W):
            if key[x] > lock[x]:
                fit = False
                break
        result += 1 if fit else 0







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









# # # # # # # # # # # #
#  STOP PART 2 HERE!  #
# # # # # # # # # # # #
STAT_EN_TIME = time.perf_counter() 
STAT_VR_ELAPSEDTIME = (STAT_EN_TIME - STAT_ST_TIME)*1000.0
print(f'[STAT TIME P2] Part 2 took [{STAT_VR_ELAPSEDTIME:.6f}] ms')
print("CH2: ",str(result), end='\n\n')
# RESULT:
