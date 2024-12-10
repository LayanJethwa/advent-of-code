import math
import g
import re
ll = open("input.txt",'r').read().splitlines()
a = 0
t = []
for y in range(len(ll)):
    for x in range(len(ll[y])):
        if ll[y][x] == "0":
            t.append((x,y))

v = set()
def s(c,n):
    global a
    global v
    ad = g.a(ll,c[0],c[1])
    for i in range(4):
        if ad[i] in '0123456789':
            if int(ad[i]) -n == 1:
                x = c[0]
                y = c[1]
                if i==0:
                    q = (x+1,y)
                elif i==1:
                    q = (x,y-1)
                elif i==2:
                    q = (x-1,y) 
                elif i==3:
                    q = (x,y+1)
                if q not in v:
                    v.add(q)
                    if int(ad[i]) == 9:
                        a += 1
                    else:
                        s(q,int(ad[i]))
                    

for i in t:
    v = set()
    v.add(i)
    s(i,0)
                
print(a)











a = 0
v = set()
d = set()
def s(c,n):
    global a
    global v
    global d
    ad = g.a(ll,c[0],c[1])
    a -= 1
    for i in range(4):
        if ad[i] in '0123456789':
            if int(ad[i]) -n == 1:
                x = c[0]
                y = c[1]
                if i==0:
                    q = (x+1,y)
                elif i==1:
                    q = (x,y-1)
                elif i==2:
                    q = (x-1,y) 
                elif i==3:
                    q = (x,y+1)
                a += 1
                v.add(q)
                if int(ad[i]) == 9:
                    None
                else:
                    s(q,int(ad[i]))
                    

for i in t:
    v = set()
    v.add(i)
    s(i,0)
                
print(a+len(t))