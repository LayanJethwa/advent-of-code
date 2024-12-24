import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy
import networkx as nx

gg = nx.Graph()
d = {}
v = {}
b = {}
ll = open("input.txt",'r').read().splitlines()
#ll = open("test.txt",'r').read().splitlines()
a = 0
for l in ll:
    if '-' in l:
        l = l.split(' -> ')
        t = l[0].split(' ')
        d[(t[0],t[2],t[1])] = d.get((t[0],t[2],t[1]),[])+[l[1]]
        gg.add_node(t[0])
        gg.add_node(t[2])
        gg.add_node(l[1])
        gg.add_edge(t[0],l[1])
        gg.add_edge(t[2],l[1])
        if t[0] not in v:
            v[t[0]] = -1
        if t[2] not in v:
            v[t[2]] = -1
        if l[1] not in v:
            v[l[1]] = -1
        b[l[1]] = (-1,-1)
    elif l != '':
        l = l.split(': ')
        d[l[0]] = int(l[1])
        v[l[0]] = int(l[1])
        gg.add_node(l[0])


def u(n,va):
    for x in d:
        if n in x and str(d[x]) not in '10':
            for i in d[x]:
                t = b[i]
                if t[0] == -1:
                    b[i] = (va,t[1])
                else:
                    b[i] = (t[0],va)
                    
                    if 'AND' in x:
                        nv = va & t[0]
                    elif 'OR' in x:
                        nv = va | t[0]
                    elif 'XOR' in x:
                        nv = va ^ t[0]

                    v[i] = nv
                    u(i,nv)
    
q = []
for i in v:
    if v[i] != -1:
        q.append((i,v[i]))

while len(q) > 0:
    u(*q.pop(0))

while -1 in v.values():
    for i in v:
        if v[i] == -1:
            for n in d:
                if '[' in str(d[n]):
                    if i in d[n]:
                        if v[n[0]] != -1:
                            u(n[0],v[n[0]])
                        if v[n[1]] != -1:
                            u(n[1],v[n[1]])


z = []
for i in b:
    if i[0] == 'z':
        z += [int(i[1:])]

s = ''
for i in range(max(z)+1):
    s = str(v['z'+str(i).zfill(2)]) + s
print(int('0b'+s,2))









xs = []
for i in d:
    if i[0] == 'x':
        xs += [int(i[1:])]

ys = []
for i in d:
    if i[0] == 'y':
        ys += [int(i[1:])]

sx = ''
for i in range(max(xs)+1):
    sx = str(v['x'+str(i).zfill(2)]) + sx

sy = ''
for i in range(max(ys)+1):
    sy = str(v['y'+str(i).zfill(2)]) + sy

e = bin(int('0b'+sx,2)+int('0b'+sy,2))
th = [i for i in d.keys() if 'AND' in i or 'OR' in i or 'XOR' in i]

def r(n,de=1):
    c = [n]
    v = set()
    for j in range(de):
        a = []
        for x in c:
            for q in [list(i[0:2]) for i in th if x in d[i]][0]:
                a += [q]
        for i in a:
            if i[0] in 'xy':
                v.add(i)
            else:
                c += [i]
    return v

def rb(n):
    return[i for i in th if n in d[i]]

for i in range(len('0b'+s)):
    if e[i] != ('0b'+s)[i]:
        print(len(z)+1-i)

print('\n')

for i in range(46):
    try:
        d1 = rb('z'+str(i).zfill(2))[0]
        d21 = rb(d1[0])[0]
        d22 = rb(d1[1])[0]
        if d22[0][0] in 'xy':
                d21,d22 = d22,d21
        d31 = rb(d22[0])[0]
        d32 = rb(d22[1])[0]
        if d32[0][0] in 'xy':
            d31,d32 = d32,d31
        d41 = rb(d32[0])[0]
        d42 = rb(d32[1])[0]
        if d42[0][0] in 'xy':
            d41,d42 = d42,d41
        if not(d1[2] == 'XOR' and d21[2] == 'XOR' and d22[2] == 'OR' and d31[2] == 'AND' and d32[2] == 'AND' and d41[2] == 'XOR'):
            print(i)
            print(d1,d21,d22,d31,d32,d41,d42)
            print([i[2] for i in [d1,d21,d22,d31,d32,d41,d42]])
    except:
        if d1:
            print(d1)
        if d21:
            print(d21)
        if d22:
            print(d22)
        if d31:
            print(d31)
        if d32:
            print(d32)
        if d41:
            print(d41)
        if d42:
            print(d42)
        print(f'ERROR {i}')

'''
XOR(XOR(xy n),OR(AND(xy n-1), AND(XOR(xy n-2),

z10,ggn,ndw,jcb,z32,grm,z39,twr
ggn,grm,jcb,ndw,twr,z10,z32,z39

10&11
    0 OR ... -> XOR ...
    1 AND 10 -> XOR 10
    2 AND ... -> OR ...
    3 XOR 10 -> AND 9
    4 OR ... -> AND ...
    5 AND 9 -> XOR 9

    2 XOR ... -> OR ...
    3 XOR 10 -> AND 10
    4 OR ... -> AND ...
    5 AND 9 -> XOR 9

        OR ... -> z10
        XOR ... -> ggn
        AND 10 -> gvm
        XOR 10 -> hks
        OR ... -> mbv
        AND 9 -> wsd
17&18
    1 AND 17 -> XOR 17
    3 XOR 17 -> AND 17
        AND 17 -> ndw
        XOR 17 -> jcb
32&33
    0 AND ... -> XOR ...
    4 XOR ... -> AND ...
        AND ... -> z32
        XOR ... -> grm
39&40
    0 AND 39 -> XOR ...
    3 XOR ... -> AND 39
        AND 39 -> z39
        XOR ... -> twr



34
33
32
17
15
14
13
12
11
10

z0 [('x00', 'y00', 'XOR')]
z1 [('ckc', 'wrn', 'XOR')]
z2 [('cmd', 'hkc', 'XOR')]
z3 [('tpg', 'jnn', 'XOR')]
z4 [('fwq', 'trj', 'XOR')]
z5 [('jvj', 'qsf', 'XOR')]
z6 [('vvr', 'vks', 'XOR')]
z7 [('cch', 'tsc', 'XOR')]
z8 [('tch', 'mwb', 'XOR')]
z9 [('tqs', 'whg', 'XOR')]
z10 [('gvm', 'smt', 'OR')] *
z11 [('pbr', 'ggn', 'XOR')]
z12 [('kfc', 'rgk', 'XOR')]
z13 [('hwk', 'whj', 'XOR')]
z14 [('jhh', 'pvd', 'XOR')]
z15 [('bgw', 'wvb', 'XOR')]
z16 [('jcg', 'grb', 'XOR')]
z17 [('ndw', 'nvn', 'XOR')]
z18 [('rvh', 'cmq', 'XOR')]
z19 [('nmv', 'rjb', 'XOR')]
z20 [('mnj', 'kkc', 'XOR')]
z21 [('rpq', 'grd', 'XOR')]
z22 [('sqm', 'dkw', 'XOR')]
z23 [('vhk', 'ccb', 'XOR')]
z24 [('pwp', 'cms', 'XOR')]
z25 [('jks', 'njg', 'XOR')]
z26 [('jqk', 'mwc', 'XOR')]
z27 [('ghv', 'qnk', 'XOR')]
z28 [('kkb', 'wnd', 'XOR')]
z29 [('ffd', 'twv', 'XOR')]
z30 [('qnt', 'cmf', 'XOR')]
z31 [('rqp', 'vpr', 'XOR')]
z32 [('rmn', 'whq', 'AND')] *
z33 [('dpc', 'spp', 'XOR')]
z34 [('spk', 'nfv', 'XOR')]
z35 [('qqq', 'qgs', 'XOR')]
z36 [('kdq', 'fmw', 'XOR')]
z37 [('bnp', 'cnf', 'XOR')]
z38 [('scg', 'fsb', 'XOR')]
z39 [('x39', 'y39', 'AND')] *
z40 [('hdj', 'psd', 'XOR')]
z41 [('dpv', 'ptt', 'XOR')]
z42 [('jmq', 'hdh', 'XOR')]
z43 [('jvs', 'kft', 'XOR')]
z44 [('kbk', 'ngn', 'XOR')]
z45 [('ncw', 'dcj', 'OR')] *
'''