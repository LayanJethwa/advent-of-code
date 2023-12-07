import math
import adj
ll = open("input.txt",'r').read().splitlines()
c = {}
for l in ll:
    l = l.replace('T','a').replace('J','b').replace('Q','c').replace('K','d').replace('A','e').split(' ')
    if len(set(l[0]))==1:
        c[tuple(l)] = 7
    elif len(set(l[0]))==2:
        if l[0].count(list(set(l[0]))[0]) == 1 or l[0].count(list(set(l[0]))[0]) == 4:
            c[tuple(l)] = 6
        elif l[0].count(list(set(l[0]))[0]) == 3 or l[0].count(list(set(l[0]))[0]) == 2:
            c[tuple(l)] = 5
    elif len(set(l[0]))==3:
        if l[0].count(list(set(l[0]))[0]) == 3 or l[0].count(list(set(l[0]))[1]) == 3 or l[0].count(list(set(l[0]))[2]) == 3:
            c[tuple(l)] = 4
        elif l[0].count(list(set(l[0]))[0]) == 2 or l[0].count(list(set(l[0]))[1]) == 2 or l[0].count(list(set(l[0]))[2]) == 2:
            c[tuple(l)] = 3
    elif len(set(l[0]))==4:
        c[tuple(l)] = 2
    elif len(set(l[0]))==5:
        c[tuple(l)] = 1


c = dict(sorted(c.items()))
c = dict(sorted(c.items(), key = lambda item: item[1]))
co = 0
a = 0
for i in c:
    co += 1
    a += (int(i[1])*co)
print(a)

c = {}
for l in ll:
    newl = l.replace('T','a').replace('J','1').replace('Q','c').replace('K','d').replace('A','e').split(' ')
    if newl[0].count('1') == 5:
        newli = ['2','2','2','2','2']
    else:
        newli = [i for i in newl[0] if i != '1']
    l = [newl[0].replace('1', max(newli,key=newli.count))]
    l.append(newl[1])
    if len(set(l[0]))==1:
        c[tuple(newl)] = 7
    elif len(set(l[0]))==2:
        if l[0].count(list(set(l[0]))[0]) == 1 or l[0].count(list(set(l[0]))[0]) == 4:
            c[tuple(newl)] = 6
        elif l[0].count(list(set(l[0]))[0]) == 3 or l[0].count(list(set(l[0]))[0]) == 2:
            c[tuple(newl)] = 5
    elif len(set(l[0]))==3:
        if l[0].count(list(set(l[0]))[0]) == 3 or l[0].count(list(set(l[0]))[1]) == 3 or l[0].count(list(set(l[0]))[2]) == 3:
            c[tuple(newl)] = 4
        elif l[0].count(list(set(l[0]))[0]) == 2 or l[0].count(list(set(l[0]))[1]) == 2 or l[0].count(list(set(l[0]))[2]) == 2:
            c[tuple(newl)] = 3
    elif len(set(l[0]))==4:
        c[tuple(newl)] = 2
    elif len(set(l[0]))==5:
        c[tuple(newl)] = 1


c = dict(sorted(c.items()))
c = dict(sorted(c.items(), key = lambda item: item[1]))
co = 0
a = 0
for i in c:
    co += 1
    a += (int(i[1])*co)
print(a)
