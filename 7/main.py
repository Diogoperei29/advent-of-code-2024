import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time
sys.setrecursionlimit(10**6)

f = open("2024/7/input.txt").read().strip()
lines = f.split('\n')
results = [ int(a.split(': ')[0]) for a in lines ]
values = [ a.split(': ')[1].split() for a in lines ]

def evaluate_p1(expected, curr, n, sig, values_l):
    
    if sig != '':
        curr = curr * int(values_l[n]) if sig == '*' else curr + int(values_l[n])
    else:
        curr = int(values_l[n])
    
    if curr == expected and n >= len(values_l)-1:
        return True
    
    if curr > expected or n >= len(values_l)-1:
        return False
    
    if evaluate_p1(expected, curr, n+1, '+', values_l) or \
       evaluate_p1(expected, curr, n+1, '*', values_l):
        return True
    
    return False

def evaluate_p2(expected, curr, n, sig, values_l):
    
    if sig != '':
        if sig == '*':
            curr = curr * int(values_l[n])
        elif sig == '+':
            curr = curr + int(values_l[n])
        elif sig == '||':
            curr = int(str(curr) + values_l[n])
    else:
        curr = int(values_l[n])
    
    if curr == expected and n >= len(values_l)-1:
        return True
    
    if curr > expected or n >= len(values_l)-1:
        return False
    
    if evaluate_p2(expected, curr, n+1, '+', values_l) or \
       evaluate_p2(expected, curr, n+1, '*', values_l) or \
       evaluate_p2(expected, curr, n+1, '||', values_l):
        return True
    
    return False
        
# Challenge 1
result = 0

for idx in range(len(results)):
    if evaluate_p1(results[idx], 0, 0, '', values[idx]):
        result += results[idx]

print("CH1: ",str(result))
# 267566105056

# Challenge 2
result = 0

for idx in range(len(results)):
    if evaluate_p2(results[idx], 0, 0, '', values[idx]):
        result += results[idx]

print("CH2: ",str(result))
# 116094961956019