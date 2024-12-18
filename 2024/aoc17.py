import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy
#import networkx as nx

d = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
#ll = open("test.txt",'r').read().splitlines()
a = 0
r = []
for l in ll:
    nl = [int(i.group()) for i in re.finditer("-?\d+",l)]
    if "Program" not in l and len(nl) > 0:
        r += [nl[0]]

l = nl.copy()

def co(op):
    global r
    if op <= 3:
        return op
    elif op == 4:
        return r[0]
    elif op == 5:
        return r[1]
    elif op == 6:
        return r[2]

p = 0
o = []
while p < len(l)-1:
    cp = 0
    oc = l[p]
    op = l[p+1]

    if oc == 0:
        r[0] = math.floor(r[0]/(2**co(op)))
    if oc == 1:
        r[1] = op ^ r[1]
    elif oc == 2:
        r[1] = co(op)%8
    elif oc == 3:
        if r[0] != 0:
            p = op
            cp = 1
    elif oc == 4:
        r[1] = r[1] ^ r[2]
    elif oc == 5:
        o += [co(op)%8]
    elif oc == 6:
        r[1] = math.floor(r[0]/(2**co(op)))
    elif oc == 7:
        r[2] = math.floor(r[0]/(2**co(op)))

    if not cp:
        p += 2


print(','.join([str(i) for i in o]))









o = []
b = len(l)-1
x = (8**b)
v = [x]

while b >= 0:
    nv = []
    for x in v:
        for a in range(8):
            r = [int(x),0,0]
            p = 0
            o = []
            while p < len(l)-1:
                cp = 0
                oc = l[p]
                op = l[p+1]

                if oc == 0:
                    r[0] = int(math.floor(r[0]/(2**co(op))))
                if oc == 1:
                    r[1] = op ^ r[1]
                elif oc == 2:
                    r[1] = co(op)%8
                elif oc == 3:
                    if r[0] != 0:
                        p = op
                        cp = 1
                elif oc == 4:
                    r[1] = r[1] ^ r[2]
                elif oc == 5:
                    o += [co(op)%8]
                elif oc == 6:
                    r[1] = int(math.floor(r[0]/(2**co(op))))
                elif oc == 7:
                    r[2] = int(math.floor(r[0]/(2**co(op))))

                if not cp:
                    p += 2
            if o[b] == l[b]:
                nv += [x]

            x += (8**b)
        
    b -= 1
    v = nv.copy()

print(min(v))
'''
B = A%8
B = B^3
C = A//(2**B)
B = B^C
A = A//8
B = B^5
OUT B%8
IF A:
    JUMP TO 0

OUT (((A%8)^3)^(A//(2**((A%8)^3)))^5)%8
(((A%8)^3)^(A//(2**((A%8)^3))))%8  ^5
((A%8)^3)%8 ^ (A//(2**((A%8)^3)))%8 ^5
A%8 ^6 ^(A//(2**((A%8)^3)))%8
6 = 110

2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0
    
Takes math.floor(math.log(A,8)+1) outputs
len(l) = 16

(8**15)+1 <= x < 8**16

END: A = 0
periodic output per bit
bit 1 changes every 1
bit 2 changes every 8
bit 3 changes every 64
etc.
'''