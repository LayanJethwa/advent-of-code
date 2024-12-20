import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy
import networkx as nx

pl = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
#ll = open("test.txt",'r').read().splitlines()
s = g.s(ll,"S")[0]
e = g.s(ll,"E")[0]
g.e(ll,*s,'.')
g.e(ll,*e,'.')
gg = g.ng(ll,'.')

sp = dict(nx.shortest_path_length(gg,target=e))

def r(i,s):
    rr = set()
    x,y = i
    for dx in range(-s,s+1):
        rd = s-abs(dx)
        for dy in range(-rd, rd+1):
            if dx == dy == 0:
                continue
            xn, yn = x+dx,y+dy
            if g.c(ll,xn,yn,'?') == '.':
                rr.add((xn,yn))
    return rr

a = 0
for n in gg.nodes():
    for dx,dy in r(n,2):
        c = abs(n[0]-dx)+abs(n[1]-dy)
        sv = sp[n]-(sp[(dx,dy)] + c)
        if sv >= 100:
            a += 1
print(a)






a = 0
for n in gg.nodes():
    for dx,dy in r(n,20):
        c = abs(n[0]-dx)+abs(n[1]-dy)
        sv = sp[n]-(sp[(dx,dy)] + c)
        if sv >= 100:
            a += 1
print(a)