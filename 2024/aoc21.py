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

n = {'0':(1,3),'1':(0,2),'2':(1,2),'3':(2,2),'4':(0,1),'5':(1,1),'6':(2,1),'7':(0,0),'8':(1,0),'9':(2,0),'A':(2,3),'^':(1,0),'a':(2,0),'<':(0,1),'v':(1,1),'>':(2,1)}
gn = nx.grid_2d_graph(3,4)
gn.remove_node((0,3))
gd = nx.grid_2d_graph(3,2)
gd.remove_node((0,0))

def m(s,f,n=1):
    if n:
        t = nx.all_simple_paths(gn,s,f)
    else:
        t = nx.all_simple_paths(gd,s,f)

    r = []
    for p in t:
        ds = ''
        for x in range(len(p)-1):
            cd = (p[x+1][0]-p[x][0],p[x+1][1]-p[x][1])
            if cd == (1,0):
                ds += '>'
            elif cd == (-1,0):
                ds += '<'
            elif cd == (0,1):
                ds += 'v'
            elif cd == (0,-1):
                ds += '^'
        ds += 'a'
        r.append(ds)
    if r == []:
        r = ['a']
    return r

@functools.cache
def q(s,l,d):
    if d == 0:
        pn = 1
        c = n['A']
    else:
        pn = 0
        c = n['a']
    
    ln = 0
    for h in s:
        nc = n[h]
        ms = m(c,nc,pn)
        if d == l:
            ln += min([len(i) for i in ms])
        else:
            ln += min([q(s,l,d+1) for s in ms])
        c = nc
    return ln

a = 0
for l in ll:
    a += q(l,2,0)*int(l[0:-1])
print(a)




a = 0
for l in ll:
    a += q(l,25,0)*int(l[0:-1])
print(a)