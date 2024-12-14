import math
import g
import re
import functools
from collections import defaultdict
import sympy
from sympy.abc import x,y,z

d = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
a = 0

def c(v):
    p = []
    for a in range(101):
        x = y = 0
        x = v[0][0]*a
        y = v[0][1]*a
        if x == v[2][0] and y == v[2][1]:
            p.append((a,0))
        for b in range(1,101):
            x += v[1][0]
            y += v[1][1]
            if x == v[2][0] and y == v[2][1]:
                p.append((a,b))
    return p

v = []
for l in ll:
    v.append(tuple([int(i.group()) for i in re.finditer("\d+", l)]))
    if () in v: v.remove(())
    if len(v) == 3:
        p = c(v)
        m = 0
        if len(p) != 0:
            for i in p:
                if m == 0 or (i[0]*3 + i[1]*1) < m:
                    m = (i[0]*3 + i[1]*1)
        v = []
        a += m

print(a)















a = 0
v = []
for l in ll:
    v.append(tuple([int(i.group()) for i in re.finditer("\d+", l)]))
    if 'Prize' in l:
        v[-1] = (v[-1][0]+10000000000000,v[-1][1]+10000000000000)
    if () in v: v.remove(())
    if len(v) == 3:
        m = 0
        s = sympy.solve([(x*v[0][0])+(y*v[1][0])-v[2][0],(x*v[0][1])+(y*v[1][1])-v[2][1]], [x,y], dict=True)
        for r in s:
            if r[x] == int(r[x]) and r[y] == int(r[y]):
                i = (int(r[x]),int(r[y]))
                if m == 0 or (i[0]*3 + i[1]*1) < m:
                    m = (i[0]*3 + i[1]*1)
        v = []
        a += m
print(a)