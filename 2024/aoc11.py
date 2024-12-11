import math
import g
import re
import functools
from collections import defaultdict

d = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
a = 0
l = [int(i) for i in ll[0].split(' ')]

for i in l:
    d[i] += 1

def s(d):
    nd = defaultdict(int)
    for n, c in d.items():
        l = len(str(n))
        if n == 0:
            nd[1] += c
        elif l % 2 == 0:
            nd[n // 10**(l//2)] += c
            nd[n % 10**(l//2)] += c
        else:
            nd[n*2024] += c
    return nd

for x in range(25):
    d = s(d)

print(sum(d.values()))






for x in range(50):
    d = s(d)

print(sum(d.values()))