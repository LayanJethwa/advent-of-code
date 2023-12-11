import math
import adj
ll = open("input.txt",'r').read().splitlines()
g = []
t = ''
r = []
col = []
co = 0
for i in range(len(ll[0])):
    for j in range(len(ll)):
        if ll[j][i] == '.':
            co += 1
    if co == len(ll):
        col.append(i)
    co = 0
            
for l in range(len(ll)):
    if len(set(ll[l])) == 1:
        r.append(l)

for l in range(len(ll)):
    for c in range(len(ll[l])):
        if ll[l][c] == '#':
            g.append((l,c))
a = 0
for i in g:
    for j in g:
        rl = [x for x in r if x > min(i[0],j[0]) and x < max(i[0],j[0])]
        rc = [x for x in col if x > min(i[1],j[1]) and x < max(i[1],j[1])]
        a += abs(i[0]-j[0])+abs(i[1]-j[1])+((len(rl))+(len(rc)))*1
a/=2
print(a)
            



g = []
t = ''
r = []
col = []
co = 0
for i in range(len(ll[0])):
    for j in range(len(ll)):
        if ll[j][i] == '.':
            co += 1
    if co == len(ll):
        col.append(i)
    co = 0
            
for l in range(len(ll)):
    if len(set(ll[l])) == 1:
        r.append(l)

for l in range(len(ll)):
    for c in range(len(ll[l])):
        if ll[l][c] == '#':
            g.append((l,c))
a = 0
for i in g:
    for j in g:
        rl = [x for x in r if x > min(i[0],j[0]) and x < max(i[0],j[0])]
        rc = [x for x in col if x > min(i[1],j[1]) and x < max(i[1],j[1])]
        a += abs(i[0]-j[0])+abs(i[1]-j[1])+((len(rl))+(len(rc)))*999999
a/=2
print(a)
