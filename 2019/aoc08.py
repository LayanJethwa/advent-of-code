import math
import adj
import intcode
ll = open("input.txt",'r').read().splitlines()
for l in ll:
    l = l
d = (25,6)
a = d[0]*d[1]
m = (0,9999)
for i in range(len(l)//a):
    c = l[i*a:(i+1)*a].count('0')
    if c < m[1]:
        m = (i,c)
c1 = l[m[0]*a:(m[0]+1)*a].count('1')
c2 = l[m[0]*a:(m[0]+1)*a].count('2')
print(c1*c2)






la = {i:'2' for i in range(a)}
for i in range(len(l)//a):
    c = l[i*a:(i+1)*a]
    for i in range(len(c)):
        if c[i] != '2' and la[i] == '2':
            la[i] = c[i]

for i in range(d[1]):
    print((''.join(list(la.values()))).replace('0','█').replace('1',' ')[i*d[0]:(i+1)*d[0]])
