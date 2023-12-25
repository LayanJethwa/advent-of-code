import math
import adj
import random
ll = open("input.txt",'r').read().splitlines()
n = []
a = []
cn = {}
for l in ll:
    l = l.split(': ')
    l[1] = l[1].split(' ')
    n += [l[0]]+l[1]
    a.append(l)

for i in set(n):
    t = []
    for j in a:
        if j[0] == i:
            t+=j[1]
        elif i in j[1]:
            t.append(j[0])
    cn[i] = [t,random.randrange(-100,100,1)/100]

a = 0
while a != 3:
    a = 0
    for x in cn:
        cn[x][1] = sum([cn[i][1] for i in cn[x][0]])/len(cn[x][0])
    m1 = min([cn[x][1] for x in cn])
    m2 = max([cn[x][1] for x in cn])
    for x in cn:
        cn[x][1] = (2*(cn[x][1]-m1))/(m2-m1)-1
            
    for x in cn:
        if cn[x][1] > 0:
            for i in cn[x][0]:
                if cn[i][1] < 0:
                    a += 1
                        
print(len([cn[x][1] for x in cn if cn[x][1] < 0])*len([cn[x][1] for x in cn if cn[x][1] > 0]))

