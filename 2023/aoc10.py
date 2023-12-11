import math
import adj
sp = (0,0)
ll = open("input.txt",'r').read().splitlines()
for l in range(len(ll)):
    for c in range(len(ll[l])):
        if ll[l][c] == 'S':
            sp = (l,c)
def d(s):
    if s == '|':
        return([1,3])
    elif s == '-':
        return([2,0])
    elif s == 'L':
        return([1,2])
    elif s == 'J':
        return([1,0])
    elif s == '7':
        return([3,0])
    elif s == 'F':
        return([3,2])
    else:
        return([])

#0,1,2,3 = w,n,e,s
ss = []
for x in range(4):
    if (x+2)%4 in d(adj.ac(ll,sp[0],sp[1],'.')[x]):
        ss.append(x)
cp = sp
cd = ss[0]

def np(cp,di):
    if di == 0:
        return((cp[0],cp[1]-1))
    elif di == 1:
        return((cp[0]-1,cp[1]))
    elif di == 2:
        return((cp[0],cp[1]+1))
    elif di == 3:
        return((cp[0]+1,cp[1]))

cp = np(cp,cd)
nd = d(ll[cp[0]][cp[1]])
nd.remove((cd+2)%4)
cd = nd[0]
c = 0
lp = [cp]
while cp != sp:
    cp = np(cp,cd)
    if ll[cp[0]][cp[1]] != 'S':
        nd = d(ll[cp[0]][cp[1]])
    else:
        cp = sp
        nd = [0,1,2,3]
    nd.remove((cd+2)%4)
    cd = nd[0]
    c += 1
    lp.append(cp)
    
if c%2 == 1:
    print(int((c+1)/2))
else:
    print(int(c/2))






for x in range(len(ll)):
    for y in range(len(ll[0])):
        if (x,y) not in lp:
            ll[x] = ll[x][:y]+'.'+ll[x][y+1:]
            
if set(ss) == set([1,3]):
    ll[sp[0]] = ll[sp[0]].replace('S','|')
elif set(ss) == set([2,0]):
    ll[sp[0]] = ll[sp[0]].replace('S','-')
elif set(ss) == set([1,2]):
    ll[sp[0]] = ll[sp[0]].replace('S','L')
elif set(ss) == set([1,0]):
    ll[sp[0]] = ll[sp[0]].replace('S','J')
elif set(ss) == set([3,0]):
    ll[sp[0]] = ll[sp[0]].replace('S','7')
elif set(ss) == set([3,2]):
    ll[sp[0]] = ll[sp[0]].replace('S','F')

a = 0
for l in ll:
    w = 0
    for c in l:
        if c == '.' and w%2 == 1:
            a += 1
        elif c not in '.-F7':
            w += 1
print(a)
