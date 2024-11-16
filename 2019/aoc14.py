import math
import adj
import intcode
ll = open("test.txt",'r').read().splitlines()
d = {}
for l in ll:
    l = l.split(' => ')
    d[l[1]] = l[0]

o = []
on = {}
for i in d:
    if 'ORE' in d[i]:
        o.append(i.split(' ')[1])
        on[i.split(' ')[1]] = [int(i.split(' ')[0]),int(d[i].split(' ')[0])]

for i in d:
    if 'FUEL' in i:
        t = d[i].split(', ')

while set([i.split(' ')[1] for i in t]) != set(o):
    for i in t:
        if i.split(' ')[1] not in o:
            for j in d:
                if ' '+i.split(' ')[1] in j:
                    f = math.ceil(int(i.split(' ')[0])/int(j.split(' ')[0]))
                    for x in d[j].split(', '):
                        t += [str(int(x.split(' ')[0])*f)+' '+x.split(' ')[1]]
                    t.remove(i)
    v = {}
    for i in t:
        v[i.split(' ')[1]] = v.get(i.split(' ')[1],0) + int(i.split(' ')[0])
    t = [str(v[i])+' '+i for i in v]
    
a = 0
for i in v:
    a += math.ceil(v[i]/on[i][0]) * on[i][1]
print(a)

