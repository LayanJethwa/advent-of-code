import math
import adj
import intcode
ll = open("input.txt",'r').read().splitlines()
ms = []
for l in ll:
    l = l.replace('>','').replace('<','').replace('x','').replace('y','').replace('z','').replace('=','')
    l = [int(i) for i in l.split(', ')]
    ms.append(l)

oms = []
for i in ms:
    oms.append(i.copy())

mvs = {}
for i in range(1000):
    for m in ms:
        vs = []
        for a in range(3):
            v = mvs.get(tuple(m),[0,0,0])[a]
            for m1 in ms:
                if m[a] > m1[a]:
                    v -= 1
                elif m[a] < m1[a]:
                    v += 1
            vs.append(v)
        mvs[tuple(m)] = vs

    for m in ms:
        om = m.copy()
        for a in range(3):
            m[a] += mvs[tuple(om)][a]
        mvs[tuple(m)] = mvs.pop(tuple(om))
        
c = 0
for m in mvs:
    pot = sum([abs(m) for m in m])
    kin = sum([abs(m) for m in mvs[m]])
    tot = pot*kin
    c += tot
print(c)






ps = []
for a in range(3):
    x = 0

    ms = []
    for i in oms:
        ms.append(i.copy())

    xms = [i[a] for i in ms]
    oxms = xms.copy()
    xvs = {}
    for m in range(len(xms)):
        v = xvs.get(m,0)
        for m1 in xms:
            if xms[m] > m1:
                v -= 1
            elif xms[m] < m1:
                v += 1
        xvs[m] = v

    for m in range(len(xms)):
        xms[m] += xvs[m]

    c = 1

    while x == 0:
        for m in range(len(xms)):
            v = xvs.get(m,0)
            for m1 in xms:
                if xms[m] > m1:
                    v -= 1
                elif xms[m] < m1:
                    v += 1
            xvs[m] = v

        for m in range(len(xms)):
            xms[m] += xvs[m]

        c += 1

        if xms == oxms and all([x == 0 for x in list(xvs.values())]):
            x = c
    ps.append(x)
print(math.lcm(*ps))
    


                
