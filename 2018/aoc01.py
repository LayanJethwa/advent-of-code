import math
import adj
ll = open("input.txt",'r').read().splitlines()
f = 0
for l in ll:
    f+=int(l)
print(f)





fs = set()
f = 0
a = 0
c = 0
while a == 0:
    f+=int(ll[c])
    if f in fs:
        a = f
    else:
        fs.add(f)
    c=c+1 if c < len(ll)-1 else 0
print(a)
