from ast import Pass
import enum
import itertools
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

f = open("2024/23/test_input.txt").read().strip()
f = open("2024/23/input.txt").read().strip() # Overrides test input :)
CONNLINES = f.split('\n')
CONNS = {}
for line in CONNLINES: 
    a, b = line.split('-')
    if a not in CONNS:
        CONNS[a] = set()
    if b not in CONNS:
        CONNS[b] = set()
    if b not in CONNS[a]:
        CONNS[a].add(b)
    if a not in CONNS[b]:
        CONNS[b].add(a)
#print(CONNS)

# Challenge 1
result = 0
STAT_ST_TIME = time.perf_counter()
# # # # # # # # # # # #
#  START PART 1 HERE! #
# # # # # # # # # # # #
trios = set()
for start_pc in CONNS:
    combs = itertools.combinations(CONNS[start_pc],2)
    for comb in combs:
        if comb[0] in CONNS[comb[1]]:
            sub_combs = itertools.permutations([start_pc, comb[0], comb[1]], 3)
            #print(list(sub_combs))
            is_in_list = False
            for sub_comb in sub_combs:
                sub = (sub_comb[0], sub_comb[1], sub_comb[2])
                if sub in trios:
                    is_in_list = True
                    break
            if not is_in_list:
                trios.add((start_pc, comb[0], comb[1]))

good_trios = set() 
for trio in trios:
    has_t = False
    for pc in trio:
        if pc[0]=='t':
            has_t = True
            break
    if has_t:
        good_trios.add(trio)
        
result = (len(good_trios))

# # # # # # # # # # # #
#  STOP PART 1 HERE!  #
# # # # # # # # # # # #
STAT_EN_TIME = time.perf_counter() 
STAT_VR_ELAPSEDTIME = (STAT_EN_TIME - STAT_ST_TIME)*1000.0
print(f'[STAT TIME P1] Part 1 took [{STAT_VR_ELAPSEDTIME:.6f}] ms')
print("CH1: ",str(result), end='\n\n')
# RESULT: 1149


# Challenge 2
result = 0
STAT_ST_TIME = time.perf_counter() 
# # # # # # # # # # # #
#  START PART 2 HERE! #
# # # # # # # # # # # #

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for v in list(P):
        new_R = R | {v}        # Add v to the current clique 
        new_P = P & graph[v]   # Potential nodes are neighbors of v still in P (intersect both sets)
        new_X = X & graph[v]   # Excluded nodes are neighbors of v still in X  (^ same)
        bron_kerbosch(new_R, new_P, new_X, graph, cliques)
        P.remove(v)
        X.add(v)

def find_largest_clique(graph):
    cliques = []
    nodes = set(graph.keys())
    bron_kerbosch(set(), nodes, set(), graph, cliques)
    largest_clique = max(cliques, key=len)
    return largest_clique


largest_clique = find_largest_clique(CONNS)
largest_clique = sorted(largest_clique)
result = ','.join(largest_clique)

# # # # # # # # # # # #
#  STOP PART 2 HERE!  #
# # # # # # # # # # # #
STAT_EN_TIME = time.perf_counter() 
STAT_VR_ELAPSEDTIME = (STAT_EN_TIME - STAT_ST_TIME)*1000.0
print(f'[STAT TIME P2] Part 2 took [{STAT_VR_ELAPSEDTIME:.6f}] ms')
print("CH2: ",str(result), end='\n\n')
# RESULT: as,co,do,kh,km,mc,np,nt,un,uq,wc,wz,yo
