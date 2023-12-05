import math
import adj
ll = open("input.txt",'r').read().splitlines()
ll.append(' map:')
s = {}
r = []
t = {}
for l in ll:
    if len(l)>4:
        if l[-4::] == 'map:':
            for ru in r:
                for i in s:
                    if s[i][-1] in range(int(ru[1]),int(ru[1])+int(ru[2])) and not t[int(i)]:
                        a = s[i][-1]-int(ru[1])
                        s[i].append(int(ru[0])+a)
                        t[int(i)] = True
                    else:
                        s[i].append(s[i][-1])
            r = []
            for i in t:
                t[i] = False
    n = l.split()
    if len(n) > 1 and len(n) != 3:
        if n[0] == 'seeds:':
            for i in n[1::]:
                s[int(i)] = [int(i)]
                t[int(i)] = False
    elif len(n) == 3:
        r.append(n)

ns = []
for i in s:
    ns.append(s[i][-1])
print(min(ns))

r = []
ll = ll[:-1]
ll = list(reversed(ll))
loc = 0
c = 0
while 1:
    if c == 10000:
        print(loc)
        c = 0
    done = False
    loc += 1
    c +=1
    s = loc
    for l in ll:
        if len(l)>4:
            if l[-4::] == 'map:':
                for ru in r:
                    if not done:
                        if s >= int(ru[0]) and s <= (int(ru[0])+int(ru[2])):
                            a = s-int(ru[0])
                            s = (int(ru[1])+a)
                            done = True
                r = []
                done = False
        n = l.split()
        if len(n) > 1 and len(n) != 3:
            if n[0] == 'seeds:':
                count = 1
                while count < len(n):
                    if s in range(int(n[count]),int(n[count])+int(n[count+1])):
                        print(loc)
                        raise SystemError("Finished - very good practice i know")
                    count += 2
        elif len(n) == 3:
            r.append(n)
