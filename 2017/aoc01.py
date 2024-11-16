import math
import adj
ll = open("input.txt",'r').read().splitlines()
a = 0
l = ll[0]
for i in range(len(l)):
    if l[i] == l[(i+1)%len(l)]:
        a += int(l[i])
print(a)


a = 0
for i in range(len(l)):
    if l[i] == l[(i+(len(l)//2))%len(l)]:
        a += int(l[i])
print(a)
