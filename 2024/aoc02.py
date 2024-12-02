import math
import adj
ll = open("input.txt",'r').read().splitlines()
a = 0
for l in ll:
    l = l.split(' ')
    ts = []
    for i in range(len(l)-1):
        t = int(l[i+1]) - int(l[i])
        ts.append(t)
    if all([abs(i) <= 3 for i in ts]) and (all ([i < 0 for i in ts]) or all ([ i>0 for i in ts])):
        a += 1


print(a)





a = 0
for l in ll:
    test = ll.index(l)+1
    l = l.split(' ')
    ts = []
    for i in range(len(l)-1):
        t = int(l[i+1]) - int(l[i])
        ts.append(t)
    if all([abs(i) <= 3 for i in ts]) and (all ([i < 0 for i in ts]) or all ([ i>0 for i in ts])):
        a += 1
        print(test,l)
    else:
        d = False
        j  =0
        while (not d) and (j<len(l)):
            m = l.copy()
            m.remove(l[j])
            ts = []
            for i in range(len(m)-1):
                t = int(m[i+1]) - int(m[i])
                ts.append(t)
            if all([abs(i) <= 3 for i in ts]) and (all ([i < 0 for i in ts]) or all ([ i>0 for i in ts])):
                a += 1
                print(test,l)
                d = True
            j += 1
print(a)
