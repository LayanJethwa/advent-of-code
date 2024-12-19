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
b = 0

p = []
@functools.cache
def c(r):
    global p
    t = []
    ct = 0
    for i in p:
        if i == r[0:len(i)] and i != r:
            t += [r[len(i):]]
        elif i == r:
            ct += 1
    if len(t) > 0:
        return sum([c(i) for i in t]) + ct
    else:
        return ct

for l in ll:
    if ',' in l:
        l = l.split(', ')
        p = l
    elif len(l) > 0:
        if c(l) != 0:
            a += 1
            b += c(l)
print(a)
print(b)