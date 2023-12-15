import math
import adj
ll = open("input.txt",'r').read().splitlines()
cp = [0]*len(ll[0])
for l in range(len(ll)):
    for c in range(len(ll[l])):
        if ll[l][c] == 'O':
            ll[l] = ll[l][:c]+'.'+ll[l][c+1::]
            ll[cp[c]] = ll[cp[c]][:c]+'O'+ll[cp[c]][c+1::]
            cp[c] +=1
        elif ll[l][c] == '#':
            cp[c] = l+1
a = 0
for l in range(len(ll)):
    a += ll[l].count('O')*(len(ll)-l)
print(a)






ll = open("input.txt",'r').read().splitlines()
lls = []
li = False
while not li:
    if ''.join(ll) in lls:
        li = True
    lls.append(''.join(ll))
    for i in range(4):
        cp = [0]*len(ll[0])
        for l in range(len(ll)):
            for c in range(len(ll[l])):
                if ll[l][c] == 'O':
                    ll[l] = ll[l][:c]+'.'+ll[l][c+1::]
                    ll[cp[c]] = ll[cp[c]][:c]+'O'+ll[cp[c]][c+1::]
                    cp[c] +=1
                elif ll[l][c] == '#':
                    cp[c] = l+1
        nll = []
        for l in range(len(ll[0])):
            t = ''
            for c in range(len(ll)):
                t += ll[c][l]
            nll.append(''.join(list(reversed(t))))
        ll = list((nll))
    
c = lls.index(lls[-1])
tll = lls[c+((1000000000 - c) % (len(lls)-c-1))]
n = len(ll[0])
tll = [tll[i:i+n] for i in range(0, len(tll), n)]
a = 0
for l in range(len(tll)):
    a += tll[l].count('O')*(len(tll)-l)
print(a)
