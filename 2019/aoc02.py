import math
import adj
import intcode
ll = open("input.txt",'r').read().splitlines()
for l in ll:
    l = l.split(',')
    l = [int(l) for l in l]
ol = l.copy()
l[1] = 12
l[2] = 2

print(intcode.run(l)[0])





for n in range(100):
    for v in range(100):
        l = ol.copy()
        l[1] = n
        l[2] = v
        if intcode.run(l)[0] == 19690720:
            print((100*n)+v)
