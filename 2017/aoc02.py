import math
import adj
ll = open("input.txt",'r').read().splitlines()
a = 0
for l in ll:
    l = [int(i) for i in l.split('\t')]
    a += max(l)-min(l)
print(a)


a = 0
for l in ll:
    l = [int(i) for i in l.split('\t')]
    for i in l:
        for j in l:
            if i%j == 0 and i>j:
                a += i//j
print(a)
                
