import math
import adj
import itertools
ll = open("input.txt",'r').read().splitlines()
a = 0
for l in ll:
    l = l.split(' ')
    if len(l) == len(set(l)):
        a += 1
print(a)



a = 0
for l in ll:
    l = l.split(' ')
    if len(l) == len(set(l)):
        if all(all(x not in l for x in [''.join(i) for i in list(itertools.permutations(j)) if i != tuple(j)]) for j in l):
            a += 1
print(a)
