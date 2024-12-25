import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy
import networkx as nx

d = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
#ll = open("test.txt",'r').read().splitlines()
a = 0
c = []
o = []
k = []
for l in ll:
    if l != '':
        c += [l]
    else:
        t = []
        if c[0][0] == '#':
            for i in range(5):
                t += [max([j for j in range(7) if c[j][i] == '#'])]
            o.append(t)
        elif c[6][4] == '#':
            for i in range(5):
                t += [6-min([j for j in range(7) if c[j][i] == '#'])]
            k.append(t)
        c = []

for i in o:
    for j in k:
        if all([i[x]+j[x]+2 <= 7 for x in range(5)]):
            a += 1
print(a)