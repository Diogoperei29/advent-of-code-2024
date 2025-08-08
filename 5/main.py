import sys
import re
import math
from itertools import combinations
from collections import defaultdict, Counter
from functools import cache
import copy
import time

f = open("2024/5/input.txt").read().strip()

lines = [line for line in f.split('\n')]
idx_null = lines.index('')

rules_str = lines[0:idx_null]
updates_str = lines[idx_null+1:]

rules = {}
for rule_s in rules_str:
    if rule_s.split('|')[0] not in rules:
        rules[rule_s.split('|')[0]] = []
    rules[rule_s.split('|')[0]] += [rule_s.split('|')[1]]
    
def verify_rules(update, rules):
    checked_n = []
    for up in update:
        if up in rules:
            for rul in rules[up]:
                if rul in checked_n:
                    return False
        checked_n.append(up)
    
    return True

def enforce_rules(update, rules):
    checked_n = []
    for up in update:
        wrong_idx = []
        if up in rules:
            for rul in rules[up]:
                if rul in checked_n:
                    wrong_idx.append(checked_n.index(rul))
        if wrong_idx == []:
            checked_n.append(up)
        else : 
            wrong_idx.sort()
            checked_n.insert(wrong_idx[0], up)
    
    return checked_n
    
# Challenge 1
result = 0

for update_s in updates_str:
    update = [a for a in update_s.split(',')]
    if verify_rules(update, rules):
        middle_n = update[len(update)//2]
        result += int(middle_n)

print("CH1: ",str(result))
# 7198

# Challenge 2
result = 0

for update_s in updates_str:
    update = [a for a in update_s.split(',')]
    
    if not verify_rules(update, rules):
        new_update = enforce_rules(update, rules)
        middle_n = new_update[len(new_update)//2]
        result += int(middle_n)

print("CH2: ",str(result))
# 4230