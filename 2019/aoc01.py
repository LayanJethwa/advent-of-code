import math
import adj
ll = open("input.txt",'r').read().splitlines()
a = 0
for l in ll:
    l = int(l)
    a+= (l//3)-2
print(a)





a = 0
for l in ll:
    t = 0
    l = int(l)
    t += (l//3)-2
    a += t
    while t>0:
        t = (t//3)-2
        a += t if t>0 else 0
print(a)
