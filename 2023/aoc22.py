import math
import adj
bs = sorted([[eval(x) for x in l.split('~')] for l in open("input.txt",'r').read().splitlines()],key=lambda x: x[0][2])
bx = {}
c = 0
for i in bs:
    if i[0] == i[1]:
        bx[c] = [i[0]]
    else:
        t = []
        d = 0 if i[0][0] != i[1][0] else 1 if i[0][1] != i[1][1] else 2
        for x in range(i[0][d],i[1][d]+1):
            te = list(i[0])
            te[d] = x
            t.append(tuple(te))
        bx[c] = t
    c += 1

for i in bx:
    b = [x for x in [x for xs in list(bx.values()) for x in xs] if x not in bx[i]]
    l = [x for x in b for n in range(len(bx[i])) if x[0] == bx[i][n][0] and x[1] == bx[i][n][1] and x[2] < bx[i][0][2]]
    l = l if len(l)>0 else [(0,0,0)]
    h = max(i[2] for i in l)+1
    d = bx[i][0][2]-h
    bx[i] = [(n[0],n[1],n[2]-d) for n in bx[i]]

ss = []
ssa = []
for i in bx:
    b = [x for x in [x for xs in list(bx.values()) for x in xs] if x not in bx[i]] 
    s = [(n[0],n[1],n[2]-1) for n in bx[i] if (n[0],n[1],n[2]-1) in b]
    ss += [[j,i] for j in bx for su in s if su in bx[j]] if len(list(set([j for j in bx for su in s if su in bx[j]]))) == 1 else []
    ssa += [[j,i] for j in bx for su in s if su in bx[j]]

print(len(bs)-len(set([i[0] for i in ss])))







c = 0
q = []
def cs(su):
    for n in set([i[1] for i in ssa if i[0] == su]):
        s = [i[0] for i in ssa if i[1] == n]
        de = d+[su]
        if all(x in de for x in s):
            q.append(n)
    d.append(su)


for n in set([i[0] for i in ss]):
    print(len(set([i[0] for i in ss])),list(set([i[0] for i in ss])).index(n))
    d = []
    cs(n)
    while q:
        cs(q[0])
        q.pop(0)
    c += len(d)-1
print(c)




