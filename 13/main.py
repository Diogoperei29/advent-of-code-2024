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

f = open("2024/13/test_input.txt").read().strip()
f = open("2024/13/input.txt").read().strip()
machines = f.split('\n\n')

# Challenge 1
result = 0

# QUICK MAFS
for machine in machines:
    
    lines = machine.split('\n')
    (xA, yA) = ( float(lines[0].split('+')[1].split(',')[0]), float(lines[0].split('+')[2]) )
    (xB, yB) = ( float(lines[1].split('+')[1].split(',')[0]), float(lines[1].split('+')[2]) )
    (X, Y) = ( float(lines[2].split('=')[1].split(',')[0]), float(lines[2].split('=')[2]) )
    
    D = (1.0 - (yA*xB)/(yB*xA))
    N = (X*yB - Y*xB)/(yB*xA)
    A = N/D
    B = (Y-A*yA)/yB
    
    A = round(A)
    B = round(B)
    
    if  A*xA+B*xB == X and A*yA+B*yB == Y:
        result += (int(A)*3 + int(B))
    
print("CH1: ",str(result))
# 40069

# Challenge 2
result = 0

for machine in machines:
    
    lines = machine.split('\n')
    (xA, yA) = ( float(lines[0].split('+')[1].split(',')[0]), float(lines[0].split('+')[2]) )
    (xB, yB) = ( float(lines[1].split('+')[1].split(',')[0]), float(lines[1].split('+')[2]) )
    (X, Y) = ( 10000000000000.0 + float(lines[2].split('=')[1].split(',')[0]), 10000000000000.0+float(lines[2].split('=')[2]) )
    
    D = (1.0 - (yA*xB)/(yB*xA))
    N = (X*yB - Y*xB)/(yB*xA)
    A = N/D
    B = (Y-A*yA)/yB
    
    A = round(A)
    B = round(B)

    if  A*xA+B*xB == X and A*yA+B*yB == Y:
        result += (int(A)*3 + int(B))

print("CH2: ",str(result))
# 71493195288102