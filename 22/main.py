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

f = open("2024/22/test_input.txt").read().strip()
f = open("2024/22/input.txt").read().strip() # Overrides test input :)
numbers = [int(lin) for lin in f.split('\n')]
# secret times 64, bitwise xor it with secret number , then prune it: secret number modulo 16777216
# divide secret by 32, round to integer, bitwise xor it with secret, then prune
# secret times 2048, bitwise xor it with secret number, prune it

def get_step_1(curr_number:int):
    return ((curr_number*64)^curr_number)%16777216

def get_step_2(curr_number:int):
    return (int(curr_number/32)^curr_number)%16777216

def get_step_3(curr_number:int):
    return ((curr_number*2048)^curr_number)%16777216

def obtain_next_number(curr_number:int):
    secret_step1 = get_step_1(curr_number)
    secret_step2 = get_step_2(secret_step1)
    secret_step3 = get_step_3(secret_step2)
    return secret_step3

# Challenge 1
result = 0
STAT_ST_TIME = time.perf_counter() 
# # # # # # # # # # # #
#  START PART 1 HERE! #
# # # # # # # # # # # #

# for number in numbers:
#     curr_number = number
#     for i in range(2000):
#         curr_number = obtain_next_number(curr_number)
#     #print(number, ': ', curr_number)
#     result += curr_number

# # # # # # # # # # # #
#  STOP PART 1 HERE!  #
# # # # # # # # # # # #
STAT_EN_TIME = time.perf_counter() 
STAT_VR_ELAPSEDTIME = (STAT_EN_TIME - STAT_ST_TIME)*1000.0
print(f'[STAT TIME P1] Part 1 took [{STAT_VR_ELAPSEDTIME:.6f}] ms')
print("CH1: ",str(result), end='\n\n')
# RESULT:

# Challenge 2
result = 0
STAT_ST_TIME = time.perf_counter() 
# # # # # # # # # # # #
#  START PART 2 HERE! #
# # # # # # # # # # # #
unique_changes = set()
list_of_dict_changes = []

for number in numbers:
    curr_number = number
    old_price = int(str(curr_number)[len(str(curr_number))-1])
    #print(f'{curr_number}: {old_price}')
    dict_of_changes = {}
    current_changes = deque([])
    for i in range(2000):
        
        curr_number = obtain_next_number(curr_number)
        price = int(str(curr_number)[len(str(curr_number))-1])
        dif_price = price - old_price
        old_price = price
        
        if len(current_changes) < 4:
            current_changes.append(dif_price)
            if len(current_changes) < 4:
                continue
        else:
            current_changes.append(dif_price)
            current_changes.popleft()
            
        current_changes_tupple = (current_changes[0], \
                                  current_changes[1], \
                                  current_changes[2], \
                                  current_changes[3])
        
        if current_changes_tupple not in dict_of_changes:
            dict_of_changes[current_changes_tupple] = price
        
        #print(f'{curr_number}:   \t{price} ({dif_price})')
    #print()
    list_of_dict_changes.append(dict_of_changes)

sum_of_change_prices = {}
for dict_changes in list_of_dict_changes:
    for changes in dict_changes:
        if changes not in sum_of_change_prices:
            sum_of_change_prices[changes] = dict_changes[changes]
        else: 
            sum_of_change_prices[changes] += dict_changes[changes]

max_val = 0
for change_prices in sum_of_change_prices:
    if sum_of_change_prices[change_prices] > max_val:
        max_val = sum_of_change_prices[change_prices]
        max_changes = change_prices

result = max_val

# # # # # # # # # # # #
#  STOP PART 1 HERE!  #
# # # # # # # # # # # #
STAT_EN_TIME = time.perf_counter() 
STAT_VR_ELAPSEDTIME = (STAT_EN_TIME - STAT_ST_TIME)*1000.0
print(f'[STAT TIME P2] Part 2 took [{STAT_VR_ELAPSEDTIME:.6f}] ms')
print("CH2: ",str(result), end='\n\n')
# RESULT:
