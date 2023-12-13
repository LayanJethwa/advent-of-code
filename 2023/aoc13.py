import math
import adj
ll = open("input.txt",'r').read().strip().split('\n\n')
a = 0
for l in ll:
    l = l.split('\n')
    c = []
    for i in range(len(l[0])):
        c.append(''.join([x[i] for x in l]))
    for h in range(len(l)-1):
        if l[h] == l[h+1]:
            cn = 0
            for i in range(min(h+1,len(l)-h-1)):
                if l[h-i] == l[h+1+i]:
                    cn += 1
            if cn == (min(h+1,len(l)-h-1)):
                a += 100*(h+1)
    for v in range(len(c)-1):
        if c[v] == c[v+1]:
            cn = 0
            for i in range(min(v+1,len(c)-v-1)):
                if c[v-i] == c[v+1+i]:
                    cn += 1
            if cn == (min(v+1,len(c)-v-1)):
                a += (v+1)
print(a)





def m(a,b):
    c = 0
    for i, j in zip(a,b):
        if i != j:
            c += 1
    return c

a = 0
for l in ll:
    l = l.split('\n')
    c = []
    for i in range(len(l[0])):
        c.append(''.join([x[i] for x in l]))
    for h in range(len(l)-1):
        if l[h] == l[h+1] or m(l[h],l[h+1]) == 1:
            cn = 0
            s = 0
            for i in range(min(h+1,len(l)-h-1)):
                if l[h-i] == l[h+1+i]:
                    cn += 1
                elif m(l[h-i],l[h+1+i]) == 1:
                    cn += 1
                    s += 1
            if cn == (min(h+1,len(l)-h-1)) and s == 1:
                a += 100*(h+1)
    for v in range(len(c)-1):
        if c[v] == c[v+1] or m(c[v],c[v+1]) == 1:
            cn = 0
            s = 0
            for i in range(min(v+1,len(c)-v-1)):
                if c[v-i] == c[v+1+i]:
                    cn += 1
                elif m(c[v-i],c[v+1+i]) == 1:
                    cn += 1
                    s += 1
            if cn == (min(v+1,len(c)-v-1)) and s == 1:
                a += (v+1)
print(a)
