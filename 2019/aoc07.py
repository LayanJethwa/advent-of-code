import math
import adj
import intcode
import itertools
ll = open("input.txt",'r').read().splitlines()
for l in ll:
    l = l.split(',')
    l = [int(l) for l in l]
nl = l.copy()

os = []

for p in list(itertools.permutations([0,1,2,3,4])):
    o = [0]
    for i in range(5):
        o = intcode.run(l,[p[i]]+o)[-1]
    os += o

print(max(os))





l = nl
os = []
for p in list(itertools.permutations([5,6,7,8,9])):
    o = [0]
    i = 0
    amps = {}
    r = True
    while r:
        if i%5 not in amps:
            amps[i%5] = intcode.run(l,[p[i%5]]+o,True)
        else:
            amps[i%5] = intcode.run(amps[i%5][0],o,True,amps[i%5][1])
            if len(amps[i%5]) < 4:
                r = False
        po = o
        o = amps[i%5][-1]
        i += 1
    os += po

print(max(os))
