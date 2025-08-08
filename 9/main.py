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

#f = open("2024/9/test_input.txt").read().strip()
f = open("2024/9/input.txt").read().strip()
line = f.strip()
    
def add_to_final(final, id, length):
    for i in range(length):
        final.append(id)
        
# Challenge 1
result = 0

FILLED = deque([])
BLANKS = deque([])
final = []
pos = 0
fid = 0
for i, ch in enumerate(line):
    bl = int(line[i])
    if i%2 == 0:
        add_to_final(final, str(fid), bl)
        for idx in range(bl):
            FILLED.append((pos, 1, str(fid)))
            pos += 1
        fid += 1
    else:
        add_to_final(final, '.', bl)
        BLANKS.append((pos, bl))
        pos += bl

for (flpos, fllen, flid) in reversed(FILLED):
    for bl_i, (blpos, bllen) in enumerate(BLANKS):
        if blpos < flpos and fllen <= bllen:
            for i in range(fllen):
                final[blpos+i] = str(flid)
                final[flpos+i] = '.'
            BLANKS[bl_i] = (blpos + fllen, bllen - fllen)
            break

for i, ch in enumerate(final):
    if ch != '.':
        result += (int(ch)*i)

print("CH1: ",str(result))
#

# Challenge 2
result = 0

FILLED = deque([])
BLANKS = deque([])
final = []
pos = 0
fid = 0
for i, ch in enumerate(line):
    bl = int(line[i])
    if i%2 == 0:
        add_to_final(final, str(fid), bl)
        FILLED.append((pos, bl, str(fid)))
        pos += bl
        fid += 1
    else:
        add_to_final(final, '.', bl)
        BLANKS.append((pos, bl))
        pos += bl

for (flpos, fllen, flid) in reversed(FILLED):
    for bl_i, (blpos, bllen) in enumerate(BLANKS):
        if blpos < flpos and fllen <= bllen:
            for i in range(fllen):
                final[blpos+i] = str(flid)
                final[flpos+i] = '.'
            BLANKS[bl_i] = (blpos + fllen, bllen - fllen)
            break

for i, ch in enumerate(final):
    if ch != '.':
        result += (int(ch)*i)

print("CH2: ",str(result))
#