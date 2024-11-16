import math
import adj
ll = open("input.txt",'r').read().splitlines()
ll = [int(i) for i in ll[0].split('\t')]

c = []

while ll not in c:
    c.append(ll.copy())
    m = ll.index(max(ll))
    b = ll[m]
    ll[m] = 0
    while b:
        m += 1
        m = m%len(ll)
        ll[m] += 1
        b -= 1
print(len(c))

print(len(c)-c.index(ll))
