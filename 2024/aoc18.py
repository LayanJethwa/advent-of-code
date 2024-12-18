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
gg = []
for i in range(71):
    gg.append('.'*71)
for i in range(1024):
    l = ll[i]
    l = tuple([int(i.group()) for i in re.finditer("-?\d+",l)])
    gg[l[1]] = gg[l[1]][0:l[0]]+'#'+gg[l[1]][l[0]+1:]

c = (0,0)
e = (70,70)
d[c] = 1
q = [c]
while len(q) > 0:
    c = q.pop(0)
    #q.sort(key=lambda m: abs(m[0]-e[0])+abs(m[1]-e[1]))
    if len([d[i] for i in g.oa(*c) if d[i] != 0]) > 0:
        d[c] = min([d[i] for i in g.oa(*c) if d[i] != 0])+1
    if c != e:
        for i,j in list(zip(g.a(gg,*c,'?'),g.oa(*c))):
            if i == '.' and d[j] == 0 and j not in q:
                q.append(j)
    else:
        q = []
        break

print(d[e]-1)






d = 1
f = 1024
while d:
    l = ll[f]
    l = tuple([int(i.group()) for i in re.finditer("-?\d+",l)])
    gg[l[1]] = gg[l[1]][0:l[0]]+'#'+gg[l[1]][l[0]+1:]
    c = 1
    d = 0
    q = [(0,0)]
    v = set()
    while len(q) > 0:
        c = q.pop(0)
        v.add(c)
        if c == e:
            d = 1
            break
        for i,j in list(zip(g.a(gg,*c,'?'),g.oa(*c))):
            if i == '.' and j not in v and j not in q:
                q.append(j)
    f += 1
print(l)