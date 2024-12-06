import math
import g
import re
ll = open("input.txt",'r').read().splitlines()
a = 0
p = set()
d = (0,-1)
ds = [(0,-1),(1,0),(0,1),(-1,0)]
for l in range(len(ll)):
    if '^' in ll[l]:
        c = (ll[l].index("^"),l)
while g.c(ll,c[0],c[1],'!') != '!':
    p.add(c)
    while g.c(ll,c[0]+d[0],c[1]+d[1],"!") == '#':
        d = ds[(ds.index(d)+1)%4]
    c = (c[0]+d[0],c[1]+d[1])
print(len(p))




for l in range(len(ll)):
    if '^' in ll[l]:
        oc = (ll[l].index("^"),l)

oll = ll.copy()
for l in range(len(ll)):
    for j in range(len(ll[l])):
        ll = oll.copy()
        ll[l] = ll[l][0:j]+'#'+ll[l][j+1:]
        p = set()
        d = (0,-1)
        c = oc
        ds = [(0,-1),(1,0),(0,1),(-1,0)]
        f = 0
        while (g.c(ll,c[0],c[1],'!') != '!') and not f:
            if (c,d) not in p:
                p.add((c,d))
            else:
                f = 1
                a += 1
            while g.c(ll,c[0]+d[0],c[1]+d[1],"!") == '#':
                d = ds[(ds.index(d)+1)%4]
            c = (c[0]+d[0],c[1]+d[1])
print(a)