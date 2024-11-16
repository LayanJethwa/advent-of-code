import math
import adj
ll = open("input.txt",'r').read().splitlines()
ll = [int(i) for i in ll]
nll = ll.copy()
i = 0
c = 0
while i < len(ll):
    ll[i] += 1
    i += (ll[i]-1)
    c += 1
print(c)



i = 0
c = 0
while i < len(nll):
    t = nll[i]
    if t >= 3:
        nll[i] -= 1
    else:
        nll[i] += 1
    i += (t)
    c += 1
print(c)
