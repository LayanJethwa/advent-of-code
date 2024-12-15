import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy

d = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
a = 0
d = 0
s = ''
for l in ll:
    if l == '':
        d = ll.index(l)
    if d != 0:
        s += l

ll = [list(i) for i in ll[0:d]]
oll = deepcopy(ll)
r = g.s(ll,'@')[0]
p = (0,0)
ll[r[1]][r[0]] = '.'

for i in s:
    ll[r[1]][r[0]] = '.'
    if i == '^':
        p = (0,-1)
    elif i == '>':
        p = (1,0)
    elif i == '<':
        p = (-1,0)
    elif i == 'v':
        p = (0,1)

    nc = (r[0]+p[0],r[1]+p[1])
    if g.c(ll,*nc,'?') == '.':
        r = nc
    elif g.c(ll,*nc,'?') == 'O':
        c = nc
        b = [c]
        while g.c(ll,*c,'?') == 'O':
            b += [c]
            c = (c[0]+p[0],c[1]+p[1])
        m = 0
        for i in reversed(b):
            if ll[i[1]+p[1]][i[0]+p[0]] == '.':
                ll[i[1]][i[0]] = '.'
                ll[i[1]+p[1]][i[0]+p[0]] = 'O'
                m = 1
        if m:
            r = nc
    ll[r[1]][r[0]] = '@'

for b in g.s(ll,'O'):
    a += 100*b[1]
    a += b[0]

print(a)






ll = deepcopy(oll)
for i in range(len(ll)):
    for j in range(len(ll[i])):
        if ll[i][j] == '#':
            ll[i][j] = '##'
        elif ll[i][j] == 'O':
            ll[i][j] = '[]'
        elif ll[i][j] == '.':
            ll[i][j] = '..'
        elif ll[i][j] == '@':
            ll[i][j] = '@.'

nll = []
a = 0

for i in ll:
    i = list(''.join(i))
    nll.append(i)

ll = deepcopy(nll)


r = g.s(ll,'@')[0]
p = (0,0)
ll[r[1]][r[0]] = '.'

for i in s:
    ll[r[1]][r[0]] = '.'
    if i == '^':
        p = (0,-1)
    elif i == '>':
        p = (1,0)
    elif i == '<':
        p = (-1,0)
    elif i == 'v':
        p = (0,1)

    nc = (r[0]+p[0],r[1]+p[1])
    if g.c(ll,*nc,'?') == '.':
        r = nc
    elif g.c(ll,*nc,'?') in '[]':
        c = nc
        if g.c(ll,*nc,'?') == '[':
            b = [(c,(c[0]+1,c[1]))]
        else:
            b = [((c[0]-1,c[1]),c)]

        if p[0] != 0:
            while g.c(ll,*c,'?') in '[]':
                if g.c(ll,*c,'?') == '[':
                    b += [(c,(c[0]+1,c[1]))]
                else:
                    b += [((c[0]-1,c[1]),c)]
                c = (c[0]+(p[0]),c[1]+(p[1]))

        elif p[1] != 0:
            cv = []
            v = [nc]
            while len(v) > 0:
                c = v.pop(0)
                cv.append(c)
                if g.c(ll,*c,'?') == '[':
                    if (c[0]+1,c[1]) not in cv and (c[0]+1,c[1]) not in v:
                        v += [(c[0]+1,c[1])]
                elif g.c(ll,*c,'?') == ']':
                    if (c[0]-1,c[1]) not in cv and (c[0]-1,c[1]) not in v:
                        v += [(c[0]-1,c[1])]
                if g.c(ll,*c,'?') in '[]':
                    if g.c(ll,*c,'?') == '[':
                        b += [(c,(c[0]+1,c[1]))]
                    elif g.c(ll,*c,'?') == ']':
                        b += [((c[0]-1,c[1]),c)]
                    c = (c[0]+(p[0]),c[1]+(p[1]))
                    if c not in cv and c not in v:
                        v.append(c)

        m = 0
        bn = []
        for i in b:
            if i not in bn:
                bn += [i]
        b = bn.copy()
        if all([ll[i[1]+p[1]][i[0]+p[0]] in '.[]' for i in sum(b,())]):
            for x in reversed(b):
                t = [ll[i[1]][i[0]] for i in x]
                for i in x:
                    ll[i[1]][i[0]] = '.'
                for j in range(len(x)):
                    i = x[j]
                    ll[i[1]+p[1]][i[0]+p[0]] = t[j]
                m = 1
        if m:
            r = nc
    ll[r[1]][r[0]] = '@'

for b in g.s(ll,'['):
    a += 100*b[1]
    a += b[0]

print(a)