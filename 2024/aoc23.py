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
gg = nx.Graph()
a = 0
for l in ll:
    l = l.split('-')
    gg.add_node(l[0])
    gg.add_node(l[1])
    gg.add_edge(l[0],l[1])

c = set()

for n in gg.nodes():
    ns = list(gg.neighbors(n))
    for n1 in ns:
        for n2 in ns:
            if gg.has_edge(n1,n2):
                if n[0] == "t" or n1[0] == "t" or n2[0] == "t":
                    c.add(tuple(sorted((n,n1,n2))))

print(len(c))




a = 0
c = []
for i in list(nx.find_cliques(gg)):
    if len(i) > a:
        a = len(i)
        c = i

c.sort()
print(','.join(c))