import math
import adj
import re
ll = open("input.txt",'r').read().splitlines()
r = [int(i) for i in ll[0].split('-')]
a = 0
for p in range(r[0],r[1]):
    if ''.join(sorted(str(p))) == str(p):
        if re.findall(r'(\d)\1', str(p)):
            a += 1
print(a)




a = 0
for p in range(r[0],r[1]):
    if ''.join(sorted(str(p))) == str(p):
        t = 0
        for i in range(10):
            i = str(i)
            if re.findall('([^'+i+']|^)'+i+i+'([^'+i+']|$)',str(p)):
                t += 1
        if t>0:
            a += 1
print(a)
