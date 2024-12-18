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

t = g.ng(gg,'.')

c = (0,0)
e = (70,70)
print(len(nx.shortest_path(t,c,e))-1)









f = 1024
while nx.has_path(t,c,e):
    l = ll[f]
    l = tuple([int(i.group()) for i in re.finditer("-?\d+",l)])
    gg[l[1]] = gg[l[1]][0:l[0]]+'#'+gg[l[1]][l[0]+1:]
    t.remove_node(l)
    f += 1
print(l)