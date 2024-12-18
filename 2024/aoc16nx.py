import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy
import networkx as nx

ll = open("input.txt",'r').read().splitlines()
#ll = open("test.txt",'r').read().splitlines()

c = g.s(ll,"S")[0]
d = (1,0)
e = g.s(ll,"E")[0]
ll[c[1]] = ll[c[1]][0:c[0]]+'.'+ll[c[1]][c[0]+1:]
ll[e[1]] = ll[e[1]][0:e[0]]+'.'+ll[e[1]][e[0]+1:]

r = nx.DiGraph()
for j in range(len(ll)):
    for i in range(len(ll[j])):
        if ll[j][i] == '#':
            continue
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            r.add_node(((i,j),d))

for p,d in r.nodes:
    np = (p[0]+d[0],p[1]+d[1])
    if (np,d) in r.nodes:
        r.add_edge((p,d),(np,d),weight=1)
    for di in [(1,0),(0,1),(-1,0),(0,-1)]:
        r.add_edge((p,d),(p,di),weight=1000)
    
for d in [(1,0),(0,1),(-1,0),(0,-1)]:
    r.add_edge((e,d),"end",weight=0)

print(nx.dijkstra_path_length(r,(c,(1,0)),"end"))




b = set()
for p in nx.all_shortest_paths(r,(c,(1,0)),"end","weight"):
    for n in p:
        b.add(n[0])
print(len(b)-1)