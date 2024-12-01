import math
import adj
ll = open("input.txt",'r').read().splitlines()
l1 = []
l2 = []
for l in ll:
    l = l.split('   ')
    l1 += [int(l[0])]
    l2 += [int(l[1])]

l1 = list(sorted(l1))
l2 = list(sorted(l2))

a  = 0
for i in range(len(l1)):
    a += abs(l1[i]-l2[i])


print(a)

a  = 0
for i in l1:
    a += i*l2.count(i)

print(a)