import math
import adj
import sys
ll = open("input.txt",'r').read().splitlines()
v = {}
q = {}
r = True
def we(co,x,y,dx,dy,d):
    global r
    x += dx; y+= dy
    if x>=0 and y>=0 and x<len(ll[0]) and y<len(ll) and r:
        c = co+int(ll[x][y])
        if x == len(ll)-1 and y == len(ll[0])-1:
            print(c)
            r = False
        if (x,y,dx,dy,d) not in v:
            v[(x,y,dx,dy,d)] = c
            q.setdefault(c,[]).append((x,y,dx,dy,d))

we(0,0,0,1,0,1)
we(0,0,0,0,1,1)
while r:
    c = min(q.keys())
    s = q.pop(c)
    for i in s:
        (x,y,dx,dy,d) = i
        we(c,x,y,dy,-dx,1)
        we(c,x,y,-dy,dx,1)
        if d < 3:
            we(c,x,y,dx,dy,d+1)






v = {}
q = {}
r = True
def we2(co,x,y,dx,dy,d):
    global r
    x += dx; y+= dy
    if x>=0 and y>=0 and x<len(ll[0]) and y<len(ll) and r:
        c = co+int(ll[x][y])
        if x == len(ll)-1 and y == len(ll[0])-1 and d >= 4:
            print(c)
            r = False
        if (x,y,dx,dy,d) not in v:
            v[(x,y,dx,dy,d)] = c
            q.setdefault(c,[]).append((x,y,dx,dy,d))
            
we2(0,0,0,1,0,1)
we2(0,0,0,0,1,1)
while r:
    c = min(q.keys())
    s = q.pop(c)
    for i in s:
        (x,y,dx,dy,d) = i
        if d < 10:
            we2(c,x,y,dx,dy,d+1)
        if d >= 4:
            we2(c,x,y,dy,-dx,1)
            we2(c,x,y,-dy,dx,1)

