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

f = open("2024/11/test_input.txt").read().strip()
f = open("2024/11/input.txt").read().strip()
stones = deque([stone for stone in f.split()])

print(stones)
# Challenge 1
result = 0

NUM_OF_ITER = 25
curr_stones = stones

for i in range(NUM_OF_ITER):
    new_stones = deque([])
    for stone in curr_stones:
        
        if stone == '0':
            new_stones.append('1')
        elif len(stone)%2 == 0:
            new_stones.append(str(int(stone[0:len(stone)//2])))
            new_stones.append(str(int(stone[len(stone)//2:])))
        else:
            new_stones.append(str(int(stone)*2024))
    curr_stones = new_stones

result = len(curr_stones)
print("CH1: ",str(result))
# 207683

NUM_OF_ITER = 75

@cache
def process_stone(stone, depth):
    if depth == 0:
        return 1

    if stone == '0':
        return process_stone( '1' , depth-1)
    elif len(stone)%2 == 0:
        return process_stone(str(int(stone[0:len(stone)//2])), depth-1) + process_stone(str(int(stone[len(stone)//2:])), depth-1)
    else:
        return  process_stone(str(int(stone)*2024), depth-1)
    

# Challenge 2
result = 0

for stone in stones:
    result += process_stone(stone, NUM_OF_ITER)

print("CH2: ",str(result))
# 244782991106220

