import math
import g
import re
import functools
from collections import defaultdict

d = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
oll = ll.copy()
a = 0
i = (0,0)
while set(''.join(ll)) != {'.'}:
    while ll[i[1]][i[0]] == '.':
        if i[0] < len(ll[0])-1:
            i = (i[0]+1,i[1])
        else:
            i = (0,i[1]+1)

    p = {i}
    c = ll[i[1]][i[0]]
    ll[i[1]] = ll[i[1]][0:i[0]]+'.'+ll[i[1]][i[0]+1:]
    q = [i]
    while len(q) > 0:
        j = q.pop(0)
        ll[j[1]] = ll[j[1]][0:j[0]]+'.'+ll[j[1]][j[0]+1:]
        for x in [*zip(g.a(ll,*j),g.oa(*j))]:
            if x[0] == c:
                if x[1] not in p:
                    p.add(x[1])
                    q.append(x[1])

    s = set()
    for o in p:
        x,y = o
        for d in [(x+0.5,y),(x,y-0.5),(x-0.5,y),(x,y+0.5)]:
            if d not in s:
                s.add(d)
            else:
                s.remove(d)

    a += len(p)*len(s)

print(a)









a = 0
d = defaultdict(int)
ll = []
ll = oll.copy()
i = (0,0)
while set(''.join(ll)) != {'.'}:
    while ll[i[1]][i[0]] == '.':
        if i[0] < len(ll[0])-1:
            i = (i[0]+1,i[1])
        else:
            i = (0,i[1]+1)

    p = {i}
    c = ll[i[1]][i[0]]
    ll[i[1]] = ll[i[1]][0:i[0]]+'.'+ll[i[1]][i[0]+1:]
    q = [i]
    while len(q) > 0:
        j = q.pop(0)
        ll[j[1]] = ll[j[1]][0:j[0]]+'.'+ll[j[1]][j[0]+1:]
        for x in [*zip(g.a(ll,*j),g.oa(*j))]:
            if x[0] == c:
                if x[1] not in p:
                    p.add(x[1])
                    q.append(x[1])

    s = set()
    for o in p:
        x,y = o
        c = oll[y][x]
        for d in [(x+0.5,y),(x,y-0.5),(x-0.5,y),(x,y+0.5)]:
            if d not in s:
                s.add(d)
            else:
                s.remove(d)

    cn = 0
    ct = []
    dc = 0
    for v in s:
        if v[0] != math.floor(v[0]):
            h = [(math.floor(v[0]),v[1]+0.5),(math.floor(v[0]),v[1]-0.5),(math.ceil(v[0]),v[1]+0.5),(math.ceil(v[0]),v[1]-0.5)]
        elif v[1] != math.floor(v[1]):
            h = [(v[0]+0.5,math.floor(v[1])),(v[0]-0.5,math.floor(v[1])),(v[0]+0.5,math.ceil(v[1])),(v[0]-0.5,math.ceil(v[1]))]

        for x in h:
            if x in s:
                if v[0] != math.floor(v[0]):
                    xv = math.floor(v[0])
                    yv = math.floor(x[1])
                else:
                    xv = math.floor(x[0])
                    yv = math.floor(v[1])

                co = [(xv,yv),(xv+1,yv),(xv,yv+1),(xv+1,yv+1)]
                cov = [t in p for t in co]
                if cov.count(True) != 4:
                    if cov.count(True) == 2:
                        dc += 1
                    if [x,v] not in ct and [v,x] not in ct:
                        ct.append([x,v])
                        cn += 1

    a += len(p)*(cn-(dc//4))

print(a)