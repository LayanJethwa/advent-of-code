import math
import adj
ll = open("input.txt",'r').read().splitlines()
for l in range(len(ll)):
    for c in range(len(ll[l])):
        if ll[l][c] == 'S':
            s = (l,c)
            ll[l] = ll[l][:c]+'.'+ll[l][c+1:]

pr = []
q = []
nq = [s]
c = 0

for i in range(64):
    pr = q.copy() if q != [s] else []
    q = nq.copy()
    nq = []
    for p in q:
        for a in adj.ac(ll,p[0],p[1],'#',True):
            if a[0] == '.' and a[1][0] >= 0 and a[1][1] >= 0 and a[1][0] < len(ll) and a[1][1] < len(ll[0]) and a[1] not in nq and a[1] not in pr:
                nq.append(a[1])
    if i%2 == 1: #1 for even i, 0 for odd i
        c += len(nq)
print(c)









le = len(ll)

for l in range(len(ll)):
    ll[l] = ll[l]*5
ll = ll*5
s = (int((len(ll)-1)/2),int((len(ll)-1)/2))

st = 26501365
x = [(i*le)//2 for i in range(1,6,2)]
y = []
for n in x:
    pr = []
    q = []
    nq = [s]
    c = 0
    m = 1 if n%2 == 0 else 0
    print(n,x.index(n))
    for i in range(n):
        pr = q.copy() if q != [s] else []
        q = nq.copy()
        nq = []
        for p in q:
            for a in adj.ac(ll,p[0],p[1],'#',True):
                if a[0] == '.' and a[1][0] >= 0 and a[1][1] >= 0 and a[1][0] < len(ll) and a[1][1] < len(ll[0]) and a[1] not in nq and a[1] not in pr:
                    nq.append(a[1])
        if i%2 == m:
            c += len(nq)
    y.append(c)

p1 = ((st-x[1])*(st-x[2]))/((x[0]-x[1])*(x[0]-x[2]))
p2 = ((st-x[0])*(st-x[2]))/((x[1]-x[0])*(x[1]-x[2]))
p3 = ((st-x[0])*(st-x[1]))/((x[2]-x[0])*(x[2]-x[1]))
print((p1*y[0])+(p2*y[1])+(p3*y[2]))
