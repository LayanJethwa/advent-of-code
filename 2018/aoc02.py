import math
import adj
ll = open("input.txt",'r').read().splitlines()
c2 = c3 = 0
for l in ll:
    a = b = 0
    for c in set(l):
        if l.count(c) == 2:
            a=1
        elif l.count(c) == 3:
            b=1
    if a == 1:
        c2 += 1
    if b == 1:
        c3 += 1
print(c2*c3)





a = ''
for l in ll:
    for l1 in ll:
        t = 0
        for c in range(len(l)):
            if l[c] == l1[c]:
                t += 1
        if t == len(l)-1:
            a1 = l
            a2 = l1
for i in a1:
    if i in a2:
        a += i
print(a)

        
