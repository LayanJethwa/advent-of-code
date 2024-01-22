import math
import adj
ll = open("input.txt",'r').read().splitlines()
o = {i.split(')')[0]:[] for i in ll}
for l in ll:
    l = l.split(')')
    o[l[0]].append(l[1])

v = {}
v['COM'] = 0

def c(obj,val):
    v[obj] = val+1
    if obj in o:
        for i in o[obj]:
            c(i,val+1)

for i in o['COM']:
    c(i,0)

print(sum(v.values()))





cn = {}
cn["YOU"] = 0

def bfs(obj):
    t = []
    if obj in o:
        t += o[obj]
    for i in o:
        if obj in o[i]:
            t.append(i)

    for i in t:
        if i in cn:
            if cn[i] > cn[obj]+1:
                cn[i] = cn[obj]+1
                bfs(i)
        else:
            cn[i] = cn[obj]+1
            bfs(i)
        
bfs("YOU")

print(cn["SAN"]-2)
