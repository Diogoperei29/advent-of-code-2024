import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time

line = open("2024/3/input.txt").read().strip()

def isNumbersValid(text):
    commacount = 0
    for ch in text:
        if ch not in '0123456789,':
            return False
        if ch == ',':
            commacount+=1
            if commacount>=2:
                return False
    return True


# Challenge 1
result = 0

for i in range(len(line)-4):
    
    if line[i:i+4] == 'mul(':
        idx = i+4
        fdx = line.find(')', idx, idx+8)
        if fdx == -1:
            continue
        if isNumbersValid(line[ idx : fdx ]):
            result += (int(line[ idx : fdx ].split(',')[0]) * int(line[ idx : fdx ].split(',')[1]))
                
print("CH1: ",str(result))
# 178538786

# Challenge 2
result = 0

enabled = True
for i in range(len(line)-4):
    
    if line[i:i+4] == 'do()':
        enabled = True
        
    if line[i:i+7] == 'don\'t()':
        enabled = False
    
    if line[i:i+4] == 'mul(' and enabled:
        idx = i+4
        fdx = line.find(')', idx, idx+8)
        if fdx == -1:
            continue
        if isNumbersValid(line[ idx : fdx ]):
            result += (int(line[ idx : fdx ].split(',')[0]) * int(line[ idx : fdx ].split(',')[1]))

print("CH2: ",str(result))
# 102467299