import dis
import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time

f = open("2024/1/input.txt").read().strip()
matrix = [line for line in f.split('\n')]
GA = []
GB = []
for line in matrix:
    GA.append(int(line.split()[0]))
    GB.append(int(line.split()[1]))
    
GA.sort()
GB.sort()
dists = []
for i in range(0, len(GA)):
    dists.append(max(GA[i], GB[i])-min(GA[i], GB[i]))

# Challenge 1
result = sum(dists)
print("CH1: ",str(result))
# 2192892

# Challenge 2
result = 0

sims = []
for g in GA:
    sims.append(g * GB.count(g))
           
result = sum(sims)

print("CH2: ",str(result))
# 22962826