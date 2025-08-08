from ast import Return
import enum
import string
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

f = open("2024/19/test_input.txt").read().strip()
f = open("2024/19/input.txt").read().strip() # Overrides test input :)

TOWELS = f.split('\n')[0].split(', ')
TOWELS = sorted(TOWELS, key=len, reverse=True)
PATTERNS = f.split('\n')[2:]

DP = {}
def possibilities(text):
    if text in DP:
        return DP[text]
    
    ans = 0
    if not text:
        ans = 1
    
    for towel in TOWELS:
        if text.startswith(towel):
            ans += possibilities(text[len(towel):])
    
    DP[text] = ans
    return ans

# Challenge 1
result = 0
# Challenge 2
result2 = 0

for pp, pattern in enumerate(PATTERNS):
    poss = possibilities(pattern)
    if poss > 0:
        result += 1
    result2 += poss

print("CH1: ",str(result))
# 369
print("CH2: ",str(result2))
# 761826581538190