import math
import adj
import intcode
ll = open("input.txt",'r').read().splitlines()
for l in ll:
    l = l.split(',')
    l = [int(l) for l in l]

print(intcode.run(l.copy(),[1],False,0,10000)[-1][0])




print(intcode.run(l.copy(),[2],False,0,10000)[-1][0])
