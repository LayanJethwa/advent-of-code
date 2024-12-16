import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy

ll = open("input.txt",'r').read().splitlines()
#ll = open("test.txt",'r').read().splitlines()

c = g.s(ll,"S")[0]
d = (1,0)
e = g.s(ll,"E")[0]
ll[c[1]] = ll[c[1]][0:c[0]]+'.'+ll[c[1]][c[0]+1:]
ll[e[1]] = ll[e[1]][0:e[0]]+'.'+ll[e[1]][e[0]+1:]
vs = {}
q = [[c,d,0,[]]]
b = set()

a = 1000000000000000000000

while len(q) > 0:
    t = q.pop(0)
    c = t[0]
    d = t[1]
    v = t[2]
    p = t[3]
    if (c,d) in vs and vs[(c,d)] < v:
        continue

    vs[(c,d)] = v
    if c == e:
        if v < a:
            a = v
            b.clear()
            b.update(p)
        elif v == a:
            b.update(p)
        continue

    for x in list(zip(g.oa(c[0],c[1]),g.a(ll,c[0],c[1],'?'))):
        if x[1] == '.':
            if x[0] == (c[0]+d[0],c[1]+d[1]):
                q.append([x[0],d,v+1,p+[c]])
            elif x[0] == (c[0]+d[1],c[1]+d[0]):
                q.append([x[0],(d[1],d[0]),v+1001,p+[c]])
            elif x[0] == (c[0]-d[1],c[1]-d[0]):
                q.append([x[0],(-d[1],-d[0]),v+1001,p+[c]])
print(a)
print(len(b)+1)