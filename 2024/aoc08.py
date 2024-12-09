import math
import g
import re
ll = open("input.txt",'r').read().splitlines()
d = {}
for y in range(len(ll)):
    for x in range(len(ll[y])):
        if ll[y][x] != '.':
            d[ll[y][x]] = d.get(ll[y][x],[])+[(x,y)]

def ni(t):
    if t[1] >= 0 and t[1] < len(ll) and t[0] >= 0 and t[0] < len(ll[0]):
        return True
    else:
        return False

n = set()
for a in d:
    for i in range(len(d[a])):
        for j in range(i+1,len(d[a])):
            dy = d[a][i][1]-d[a][j][1]
            dx = d[a][i][0]-d[a][j][0]
            
            o1 = (d[a][i][0]+dx,d[a][i][1]+dy)
            o2 = (d[a][j][0]-dx,d[a][j][1]-dy)
            if ni(o1):
                n.add(o1)
            if ni(o2):
                n.add(o2)

print(len(n))











n = set()
for a in d:
    for i in range(len(d[a])):
        for j in range(i+1,len(d[a])):
            dy = d[a][i][1]-d[a][j][1]
            dx = d[a][i][0]-d[a][j][0]
        
            n.add(d[a][i])
            n.add(d[a][j])

            o1 = (d[a][i][0]+dx,d[a][i][1]+dy)
            o2 = (d[a][j][0]-dx,d[a][j][1]-dy)

            while ni(o1):
                n.add(o1)
                o1 = (o1[0]+dx,o1[1]+dy)
            while ni(o2):
                n.add(o2)
                o2 = (o2[0]-dx,o2[1]-dy)

print(len(n))