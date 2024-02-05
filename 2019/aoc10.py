import math
import adj
import intcode
ll = open("input.txt",'r').read().splitlines()
a = []
for l in range(len(ll)):
    for i in range(len(ll[l])):
        if ll[l][i] == '#':
            a.append((i,l))

ans = 0
for i in a:
    u = set()
    for j in a:
        if i != j:
            dx = j[0]-i[0]
            dy = j[1]-i[1]
            gcd = math.gcd(abs(dx),abs(dy))
            u.add((dx/gcd,dy/gcd))
    if len(u) > ans:
        ans = len(u)
        bp = i

print(ans)





def man(p):
    global bp
    return abs(bp[0]-p[0]) + abs(bp[1]-p[1])

u = set()
b = {}
a = sorted(a,key=man)
for i in a:
    if i != bp:
        dx = bp[0]-i[0]
        dy = bp[1]-i[1]
        gcd = math.gcd(abs(dx),abs(dy))
        gcd = (dx/gcd,dy/gcd,math.atan2(dy,dx))
        if gcd not in b:
            b[gcd] = [i]
        else:
            b[gcd].append(i)

def matan2(i):
    global bp
    i = (bp[0]-i[0],bp[1]-i[1])
    r = math.atan2(i[0],i[1])
    if r<0:
        r += math.pi*2
    return r

s = [b[i][0] for i in b]
b = {(b[i][0]):b[i][1:] for i in b}
s = [sorted(s,key=matan2,reverse=True)[-1]]+sorted(s,key=matan2,reverse=True)[0:-1]

for i in range(200):
    c = s[0]
    s = s[1:]
    if len(b[c]) > 0:
        b[b[c][0]] = b[c][1:]
        s.append(b[c][0])
        del b[c]

print((c[0]*100)+c[1])
