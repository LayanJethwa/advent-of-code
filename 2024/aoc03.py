import math
import adj
import re
ll = open("input.txt",'r').read().splitlines()
a = 0
for l in ll:
    for x in re.findall("mul\(\d+,\d+\)",l):
        t = x.replace("mul(","").replace(")","").split(",")
        a += math.prod([int(i) for i in t])
print(a)



d = True
a = 0
for l in ll:
    ds = list(re.finditer("do\(\)|don't\(\)",l))
    c = 0
    cd = ds[0].span()[0]
    cdm = ds[0].group()
    for x in re.finditer("mul\(\d+,\d+\)",l):
        if x.span()[0] > cd:
            if cdm == 'do()':
                d = True
            else:
                d = False
            if c < len(ds)-1:
                c += 1
            cd = ds[c].span()[0]
            cdm = ds[c].group()
        if d:
            t = x.group().replace("mul(","").replace(")","").split(",")
            a += math.prod([int(i) for i in t])
print(a)