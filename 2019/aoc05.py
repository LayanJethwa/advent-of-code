import math
import adj
import intcode
ll = open("input.txt",'r').read().splitlines()
for l in ll:
    l = l.split(',')
    l = [int(l) for l in l]
ol = l.copy()

print(intcode.run(l,1)[-1][-1])




print(intcode.run(ol,5)[-1][-1])
