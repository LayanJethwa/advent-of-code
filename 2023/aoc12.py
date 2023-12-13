import math
import adj
import re
import functools
from sympy.utilities.iterables import multiset_permutations
ll = open("input.txt",'r').read().splitlines()
a = 0

@functools.cache
def ca(l,n):
    if not n:
        if '#' not in l:
            return 1
        else:
            return 0
    if not l:
        return 0
    nc = l[0]
    ng = n[0]
    def d():
        return ca(l[1:], n)
    def h():
        tg = l[:ng].replace('?','#')
        if tg != ng*'#':
            return 0
        if len(l) == ng:
            if len(n) == 1:
                return 1
            else:
                return 0
        if l[ng] in '?.':
            return ca(l[ng+1:],n[1:])
        return 0
    if nc == '.':
        out = d()
    elif nc == '#':
        out = h()
    else:
        out = d()+h()
    return out


for l in ll:
    l = l.split(' ')
    n = [int(l) for l in l[1].split(',') if l != ',']
    a += ca(l[0],tuple(n))
print(a)





a = 0
for l in ll:
    l = l.split(' ')
    n = [int(l) for l in l[1].split(',') if l != ',']*5
    l[0] = ((l[0]+'?')*5)[0:-1]
    a += ca(l[0],tuple(n))
print(a)
