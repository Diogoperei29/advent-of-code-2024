from pickle import FALSE
import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time

f = open("2024/2/input.txt").read().strip()
matrix = [[int(a) for a in line.split()] for line in f.split('\n')]
matrix_h = len(matrix)
matrix_w = len(matrix[0])


def is_safe(report):
    
    dif = report[1] - report[0]
    for i in range(1, len(report)):
        newdif = report[i] - report[i-1]
        if  (dif>0)!=(newdif>0) or abs(newdif) > 3 or abs(newdif) == 0:
            return False
        dif = newdif

    return True
        
# Challenge 1
result = 0

for report in matrix:
    if is_safe(report):
        result += 1

print("CH1: ",str(result))
# 670

# Challenge 2
result = 0

for report in matrix:
    if is_safe(report):
        result += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i]+report[i+1:]):
                result += 1
                break
    
print("CH2: ",str(result))
# 700