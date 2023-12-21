import math
import adj
ll = open("input.txt",'r').read().splitlines()

ms = {}
for l in ll:
    if 'broadcaster' in l:
        b = l.replace('broadcaster -> ','').split(', ')
    elif '%' in l:
        ms[l[l.index('%')+1:l.index('-')-1]] = ['%',0,l[l.index('>')+2:].split(', ')]
    elif '&' in l:
        ms[l[l.index('&')+1:l.index('-')-1]] = ['&',-1,l[l.index('>')+2:].split(', ')]
        
for i in ms:
    t = {}
    for j in ms:
        if ms[i][0] == '&' and i in ms[j][2]:
            t[j] = 0
    ms[i].append(t) if ms[i][0] == '&' else None


oms = ms.copy()
l = h = 0
for a in range(1000):
    q = []
    for i in b:
        q.append([i,0,'broadcast'])

    l += 1
    while len(q) != 0:
        if q[0][0] not in ms:
            if q[0][1] == 0:
                l += 1
            else:
                h += 1
        elif ms[q[0][0]][0] == '%':
            if q[0][1] == 0:
                ms[q[0][0]][1] = 1 if ms[q[0][0]][1] == 0 else 0
                for i in ms[q[0][0]][2]:
                    q.append([i,ms[q[0][0]][1],q[0][0]])
                l += 1
            else:
                h += 1
        elif ms[q[0][0]][0] == '&':
            ms[q[0][0]][3][q[0][2]] = q[0][1]
            p = 0 if list(ms[q[0][0]][3].values()).count(1) == len(list(ms[q[0][0]][3].values())) else 1
            for i in ms[q[0][0]][2]:
                q.append([i,p,q[0][0]])
            if q[0][1] == 0:
                l += 1
            else:
                h += 1
        q = q[1:]

print(l*h)





ms = {}
for l in ll:
    if 'broadcaster' in l:
        b = l.replace('broadcaster -> ','').split(', ')
    elif '%' in l:
        ms[l[l.index('%')+1:l.index('-')-1]] = ['%',0,l[l.index('>')+2:].split(', ')]
    elif '&' in l:
        ms[l[l.index('&')+1:l.index('-')-1]] = ['&',-1,l[l.index('>')+2:].split(', ')]
        
for i in ms:
    t = {}
    for j in ms:
        if ms[i][0] == '&' and i in ms[j][2]:
            t[j] = 0
    ms[i].append(t) if ms[i][0] == '&' else None

e = 'rx'
for i in ms:
    if e in ms[i][2]:
        e1 = i
e2 = list(ms[e1][3].keys())

bps = []
bp = 0
while e2:
    bp += 1
    q = []
    for i in b:
        q.append([i,0,'broadcast'])

    while len(q) != 0 and e2:
        if q[0][2] in e2 and q[0][1] == 1:
            bps.append(bp)
            e2.remove(q[0][2])
        if q[0][0] not in ms:
            None
        elif ms[q[0][0]][0] == '%':
            if q[0][1] == 0:
                ms[q[0][0]][1] = 1 if ms[q[0][0]][1] == 0 else 0
                for i in ms[q[0][0]][2]:
                    q.append([i,ms[q[0][0]][1],q[0][0]])
        elif ms[q[0][0]][0] == '&':
            ms[q[0][0]][3][q[0][2]] = q[0][1]
            p = 0 if list(ms[q[0][0]][3].values()).count(1) == len(list(ms[q[0][0]][3].values())) else 1
            for i in ms[q[0][0]][2]:
                q.append([i,p,q[0][0]])
        q = q[1:]

print(math.prod(bps))
    

    
