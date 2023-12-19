import math
import adj
import itertools
ll = open("input.txt",'r').read().splitlines()
vs = []
x = 0
y = 0
p = 0
for l in ll:
    l = l.split(' ')
    if l[0] == 'R':
        x += int(l[1])
    elif l[0] == 'L':
        x -= int(l[1])
    elif l[0] == 'U':
        y -= int(l[1])
    elif l[0] == 'D':
        y += int(l[1])
    vs.append((x,y))
    p += int(l[1])
ys = [i[1] for i in vs]
xs = [i[0] for i in vs]
p1 = sum([x*y for x,y in zip(xs,ys[1:]+[ys[0]])])
p2 = sum([x*y for x,y in zip(ys,xs[1:]+[xs[0]])])
print(int((abs(p1-p2)/2)+(p/2)+1))








vs = []
x = 0
y = 0
p = 0
for l in ll:
    l = l.split(' ')
    v = int(l[2][2:-2],16)
    if l[2][-2] == '0':
        x += v
    elif l[2][-2] == '2':
        x -= v
    elif l[2][-2] == '3':
        y -= v
    elif l[2][-2] == '1':
        y += v
    vs.append((x,y))
    p += v
ys = [i[1] for i in vs]
xs = [i[0] for i in vs]
p1 = sum([x*y for x,y in zip(xs,ys[1:]+[ys[0]])])
p2 = sum([x*y for x,y in zip(ys,xs[1:]+[xs[0]])])
print(int((abs(p1-p2)/2)+(p/2)+1))
