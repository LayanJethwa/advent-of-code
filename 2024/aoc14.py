import math
import g
import re
import functools
from collections import defaultdict

d = []
w = 101
h = 103

ll = open("input.txt",'r').read().splitlines()
a = 0
for l in ll:
    n = list(re.finditer("-?\d+",l))
    d.append([(int(n[0].group()),int(n[1].group())),(int(n[2].group()),int(n[3].group()))])

for x in range(100):
    for p in d:
        p[0] = ((p[0][0]+p[1][0])%w,(p[0][1]+p[1][1])%h)

q = [0,0,0,0]
for p in d:
    if p[0][0] < w//2 and p[0][1] < h//2:
        q[0] += 1
    elif p[0][0] > w//2 and p[0][1] < h//2:
        q[1] += 1
    elif p[0][0] < w//2 and p[0][1] > h//2:
        q[2] += 1
    elif p[0][0] > w//2 and p[0][1] > h//2:
        q[3] += 1

print(math.prod(q))




c = 100
while True:
    c += 1
    m = []
    for p in d:
        p[0] = ((p[0][0]+p[1][0])%w,(p[0][1]+p[1][1])%h)
        m.append(abs(p[0][0]-w//2)+abs(p[0][1]-h//2))

    if len([i for i in m if i < 50])/len(m) >= 0.8:
        print(c)
        for y in range(h):
            t = ''
            for x in range(w):
                if (x,y) in [p[0] for p in d]:
                    t += '#'
                else:
                    t += '.'
            print(t)