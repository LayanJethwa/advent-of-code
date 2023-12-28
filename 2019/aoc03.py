import math
import adj
ll = open("input.txt",'r').read().splitlines()
ll = [l.split(',') for l in ll]

li0 = [(0,0)]
for c in ll[0]:
    sp = li0[-1]
    if c[0] == 'U':
        li0 += [(sp[0],sp[1]-(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'R':
        li0 += [(sp[0]+(i+1),sp[1]) for i in range(int(c[1:]))]
    elif c[0] == 'D':
        li0 += [(sp[0],sp[1]+(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'L':
        li0 += [(sp[0]-(i+1),sp[1]) for i in range(int(c[1:]))]

li1 = [(0,0)]
for c in ll[1]:
    sp = li1[-1]
    if c[0] == 'U':
        li1 += [(sp[0],sp[1]-(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'R':
        li1 += [(sp[0]+(i+1),sp[1]) for i in range(int(c[1:]))]
    elif c[0] == 'D':
        li1 += [(sp[0],sp[1]+(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'L':
        li1 += [(sp[0]-(i+1),sp[1]) for i in range(int(c[1:]))]

t = [abs(i[0])+abs(i[1]) for i in set(li0).intersection(set(li1))]
print(min([i for i in t if i > 0]))






li0 = [(0,0,0)]
for c in ll[0]: 
    sp = li0[-1][0:-1]
    co = li0[-1][2]
    if c[0] == 'U':
        li0 += [(sp[0],sp[1]-(i+1),co+(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'R':
        li0 += [(sp[0]+(i+1),sp[1],co+(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'D':
        li0 += [(sp[0],sp[1]+(i+1),co+(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'L':
        li0 += [(sp[0]-(i+1),sp[1],co+(i+1)) for i in range(int(c[1:]))]

li1 = [(0,0,0)]
for c in ll[1]: 
    sp = li1[-1][0:-1]
    co = li1[-1][2]
    if c[0] == 'U':
        li1 += [(sp[0],sp[1]-(i+1),co+(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'R':
        li1 += [(sp[0]+(i+1),sp[1],co+(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'D':
        li1 += [(sp[0],sp[1]+(i+1),co+(i+1)) for i in range(int(c[1:]))]
    elif c[0] == 'L':
        li1 += [(sp[0]-(i+1),sp[1],co+(i+1)) for i in range(int(c[1:]))]

t = set([i[0:2] for i in li0]).intersection(set([i[0:2] for i in li1]))
t = [li0[[i[0:2] for i in li0].index(t)][2]+li1[[i[0:2] for i in li1].index(t)][2] for t in t]
t.remove(0)
print(min(t))
