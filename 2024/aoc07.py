import math
import g
import re
ll = open("input.txt",'r').read().splitlines()
s = []

def c(n,l,i):
    global s
    if i == len(l)-1:
        s.append(n*l[i])
        s.append(n+l[i])
    else:
        c(n*l[i],l,i+1)
        c(n+l[i],l,i+1)

a = 0
for l in ll:
    l = l.split(': ')
    t = int(l[0])
    n = [int(i) for i in l[1].split()]
    s = []
    c(n[0],n,1)
    if t in s:
        a += t
print(a)







s = []

def c2(n,l,i):
    global s
    if i == len(l)-1:
        s.append(n*l[i])
        s.append(n+l[i])
        s.append(int(str(n)+str(l[i])))
    else:
        c2(n*l[i],l,i+1)
        c2(n+l[i],l,i+1)
        c2(int(str(n)+str(l[i])),l,i+1)

a = 0
for l in ll:
    l = l.split(': ')
    t = int(l[0])
    n = [int(i) for i in l[1].split()]
    s = []
    c2(n[0],n,1)
    if t in s:
        a += t
print(a)