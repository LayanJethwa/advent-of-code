import math
import g
import re
import random
from functools import cmp_to_key
ll = open("input.txt",'r').read().splitlines()
a = 0
p = {}
r = []
c = []
for l in ll:
    if '|' in l:
        l = l.split('|')
        p[int(l[0])] = p.get(int(l[0]),[])+[int(l[1])]
    elif ',' in l:
        l = l.split(',')
        r += [[int(i) for i in l]]
        c += [1]

for x in p:
    for i in range(len(r)):
        if x in r[i]:
            if r[i][-1] != x:
                for y in p[x]:
                    if y in r[i]:
                        if not(y in r[i][r[i].index(x)+1:]):
                            c[i] = 0
            else:
                for y in p[x]:
                    if y in r[i]:
                        c[i] = 0

for i in range(len(r)):
    if c[i] == 1:
        a += r[i][len(r[i])//2]

print(a)






def cp(a,b):
    if a in p:
        if b in p[a]:
            return -1
    return 1

z = 0
c = [1 for i in c]
for x in p:
    for i in range(len(r)):
        if x in r[i]:
            if r[i][-1] != x:
                for y in p[x]:
                    if y in r[i]:
                        if not(y in r[i][r[i].index(x)+1:]):
                            c[i] = 0
            else:
                for y in p[x]:
                    if y in r[i]:
                        c[i] = 0

for i in range(len(r)):
    if c[i] == 0:
        t = r[i].copy()
        cl = 0
        t = list(sorted(t,key=cmp_to_key(cp)))
        z += t[len(t)//2]

print(z)