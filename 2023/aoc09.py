import math
import adj
ll = open("input.txt",'r').read().splitlines()
a = 0
for l in ll:
    l = l.split(' ')
    l = [int(i) for i in l]
    ns = []
    ns.append(l)
    while len(set(ns[-1])) != 1:
        t = []
        for i in range(len(ns[-1])-1):
            t.append(ns[-1][i+1]-ns[-1][i])
        ns.append(t)
    ns.reverse()
    ns[0].append(ns[0][0])
    for n in range(1,len(ns)):
        ns[n].append(ns[n][-1]+ns[n-1][-1])
    a += ns[-1][-1]
print(a)




a = 0
for l in ll:
    l = l.split(' ')
    l = [int(i) for i in l]
    ns = []
    ns.append(l)
    while len(set(ns[-1])) != 1:
        t = []
        for i in range(len(ns[-1])-1):
            t.append(ns[-1][i+1]-ns[-1][i])
        ns.append(t)
    ns.reverse()
    ns[0] = [ns[0][0]]+ns[0]
    for n in range(1,len(ns)):
        ns[n] = [(ns[n][0]-ns[n-1][0])]+ns[n]
    a += ns[-1][0]
print(a)
