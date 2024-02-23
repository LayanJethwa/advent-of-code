import math
import adj
import intcode
ll = open("input.txt",'r').read().splitlines()
for l in ll:
    l = l.split(',')
    l = [int(l) for l in l]
ol = l.copy()

running = True
i = 0
po = 0
o = []
g = {}
d = 0
pos = (0,0)
b = 0
le = len(l.copy())
while running:
    t = intcode.run(l,[i],True,po,b,le,1000)
    if len(t) < 5:
        running = False
    else:
        l = t[0]
        po = t[1]
        i = t[2][0]
        o += t[3]
        b = t[4]
        if len(o) == 2:
            g[pos] = o[0]
            if o[1] == 0:
                d = (d-1)%4
            elif o[1] == 1:
                d = (d+1)%4

            if d == 0:
                pos = (pos[0],pos[1]-1)
            elif d == 1:
                pos = (pos[0]+1,pos[1])
            elif d == 2:
                pos = (pos[0],pos[1]+1)
            elif d == 3:
                pos = (pos[0]-1,pos[1])

            i = g.get(pos,0)
            o = []
print(len(g))
          



l = ol.copy()
running = True
i = 1
po = 0
o = []
g = {}
d = 0
pos = (0,0)
b = 0
while running:
    t = intcode.run(l,[i],True,po,b,le,1000)
    if len(t) < 5:
        running = False
    else:
        l = t[0]
        po = t[1]
        i = t[2][0]
        o += t[3]
        b = t[4]
        if len(o) == 2:
            g[pos] = o[0]
            if o[1] == 0:
                d = (d-1)%4
            elif o[1] == 1:
                d = (d+1)%4

            if d == 0:
                pos = (pos[0],pos[1]-1)
            elif d == 1:
                pos = (pos[0]+1,pos[1])
            elif d == 2:
                pos = (pos[0],pos[1]+1)
            elif d == 3:
                pos = (pos[0]-1,pos[1])

            i = g.get(pos,0)
            o = []

for y in range(min([i[1] for i in g])-1,max([i[1] for i in g])+2):
    te = ''
    for x in range(min([i[0] for i in g])-1,max([i[0] for i in g])+2):
        if g.get((x,y),0) == 0:
            te += '█'
        else:
            te += ' '
    print(te)
