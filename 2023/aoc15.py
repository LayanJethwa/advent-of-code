import math
import adj
ll = open("input.txt",'r').read().splitlines()[0].split(',')
a = 0
for l in ll:
    v = 0
    for c in l:
        v += ord(c)
        v = v*17
        v = v%256
    a += v
print(a)





a = 0
b = {i:[] for i in range(256)}
for l in ll:
    v = 0
    if '-' in l:
        for c in l[0:l.index('-')]:
            v += ord(c)
            v = v*17
            v = v%256
        for i in b[v]:
            if i[0] == l[0:l.index('-')]:
                b[v].remove(i)
    elif '=' in l:
        for c in l[0:l.index('=')]:
            v += ord(c)
            v = v*17
            v = v%256
        t = False
        for i in range(len(b[v])):
            if b[v][i][0] == l[0:l.index('=')]:
                b[v][i][1] = l.split('=')[1]
                t = True
        if not t:
            b[v].append(l.split('='))
for i in b:
    for l in range(len(b[i])):
        v = i+1
        v *= l+1
        v *= int(b[i][l][1])
        a += v
print(a)
