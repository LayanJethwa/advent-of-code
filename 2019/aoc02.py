import math
import adj
ll = open("input.txt",'r').read().splitlines()
for l in ll:
    l = l.split(',')
    l = [int(l) for l in l]
ol = l.copy()
l[1] = 12
l[2] = 2

i = 0
while l[i] != 99:
    if l[i] == 1:
        l[l[i+3]] = l[l[i+1]]+l[l[i+2]]
    elif l[i] == 2:
        l[l[i+3]] = l[l[i+1]]*l[l[i+2]]
    i += 4
print(l[0])
        



for n in range(100):
    for v in range(100):
        l = ol.copy()
        l[1] = n
        l[2] = v

        i = 0
        while l[i] != 99:
            if l[i] == 1:
                l[l[i+3]] = l[l[i+1]]+l[l[i+2]]
            elif l[i] == 2:
                l[l[i+3]] = l[l[i+1]]*l[l[i+2]]
            i += 4
        if l[0] == 19690720: print((100*n)+v)
