import math
import adj
import functools
sp = (0,-1)
ll = open("input.txt",'r').read().splitlines()

#0,1,2,3 = w,n,e,s
cp = sp
cd = 2

@functools.cache
def np(cp,di):
    if di == 0:
        return((cp[0],cp[1]-1))
    elif di == 1:
        return((cp[0]-1,cp[1]))
    elif di == 2:
        return((cp[0],cp[1]+1))
    elif di == 3:
        return((cp[0]+1,cp[1]))

@functools.cache
def nd(cp,cd):
    if ll[cp[0]][cp[1]] == '/':
        if cd == 0:
            return 3
        elif cd == 1:
            return 2
        elif cd == 2:
            return 1
        elif cd == 3:
            return 0
    elif ll[cp[0]][cp[1]] == "\\":
        if cd == 0:
            return 1
        elif cd == 1:
            return 0
        elif cd == 2:
            return 3
        elif cd == 3:
            return 2
    else:
        return cd

cp = sp
cd = 2
cps = [(cp,cd)]
lp = []
lds = [[[] for c in range(len(ll[0]))] for l in range(len(ll))]
while cps:
    cps = list(set(cps))
    lp = list(set(lp))
    r = []
    for p in range(len(cps)):
        nep = np(cps[p][0],cps[p][1])
        if (nep[0] < 0 or nep[0] >= len(ll) or nep[1] < 0 or nep[1] >= len(ll[0]) or cps[p][1] in lds[nep[0]][nep[1]]):
            r.append(cps[p])
        else:
            cps[p] = (nep,cps[p][1])
            cp = cps[p][0]
            cd = cps[p][1]
            lds[nep[0]][nep[1]].append(cd)
            lp.append(cp)
            if ll[cp[0]][cp[1]] == "|":
                if cd == 0 or cd == 2:
                    cps[p] = (cps[p][0],1)
                    cps.append((cp,3))
            elif ll[cp[0]][cp[1]] == "-":
                if cd == 1 or cd == 3:
                    cps[p] = (cps[p][0],0)
                    cps.append((cp,2))
            else:
                cps[p] = (cps[p][0],nd(cp,cd))
    for i in r:
        cps.remove(i)
print(len(set(lp)))






sps = []
for a in range(len(ll)):
    sps.append(((a,-1),2))
    sps.append(((a,len(ll[0])),0))
for a in range(len(ll[0])):
    sps.append(((-1,a),3))
    sps.append(((len(ll),a),1))
lpn = []
for sp in range(len(sps)):
    print(sp,len(sps))
    cps = [sps[sp]]
    lp = []
    lds = [[[] for c in range(len(ll[0]))] for l in range(len(ll))]
    while cps:
        cps = list(set(cps))
        lp = list(set(lp))
        r = []
        for p in range(len(cps)):
            nep = np(cps[p][0],cps[p][1])
            if (nep[0] < 0 or nep[0] >= len(ll) or nep[1] < 0 or nep[1] >= len(ll[0]) or cps[p][1] in lds[nep[0]][nep[1]]):
                r.append(cps[p])
            else:
                cps[p] = (nep,cps[p][1])
                cp = cps[p][0]
                cd = cps[p][1]
                lds[nep[0]][nep[1]].append(cd)
                lp.append(cp)
                if ll[cp[0]][cp[1]] == "|":
                    if cd == 0 or cd == 2:
                        cps[p] = (cps[p][0],1)
                        cps.append((cp,3))
                elif ll[cp[0]][cp[1]] == "-":
                    if cd == 1 or cd == 3:
                        cps[p] = (cps[p][0],0)
                        cps.append((cp,2))
                else:
                    cps[p] = (cps[p][0],nd(cp,cd))
        for i in r:
            cps.remove(i)
    lpn.append(len(set(lp)))
print(max(lpn))

