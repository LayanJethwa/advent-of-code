import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy
import networkx as nx

cs = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
#ll = open("test.txt",'r').read().splitlines()
a = 0
for l in ll:
    l = int(l)
    for i in range(2000):
        l = l^(l*64)
        l = l%16777216
        l = l^(l//32)
        l = l%16777216
        l = l^(l*2048)
        l = l%16777216
    a += l
print(a)






a = 0
s = {}
for j in range(len(ll)):
    l = int(ll[j])
    d = []
    for i in range(2000):
        ol = l
        l = l^(l*64)
        l = l%16777216
        l = l^(l//32)
        l = l%16777216
        l = l^(l*2048)
        l = l%16777216
        d += [(int(str(l)[-1])-int(str(ol)[-1]),int(str(l)[-1]))]
    cs = defaultdict(int)
    for x in range(len(d)-4):
        t = tuple([i[0] for i in d[x:x+4]])
        if len(s.get(t,[])) <= j and not cs[t]:
            s[t] = s.get(t,[])+[d[x+3][1]]
        cs[t] = 1

print(max([sum(s[i]) for i in s]))