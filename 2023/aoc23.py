import math
import adj
import time
ti = time.time()
ll = open("input.txt",'r').read().splitlines()
st = ll[0].index('.')
e = ll[-1].index('.')
sl = ['<','^','>','v']

ans = []
def ch(n):
    global v
    k = True
    if n[0][0] == (len(ll)-1,e):
        ans.append(n[0][1])

    if len(n[0]) == 3:
        v = n[0][2].copy()

    if ll[n[0][0][0]][n[0][0][1]] in sl:
        s = ll[n[0][0][0]][n[0][0][1]]
        if s == '<':
            q.append([((n[0][0][0],n[0][0][1]-1),n[0][1]+1)])
        elif s == '>':
            q.append([((n[0][0][0],n[0][0][1]+1),n[0][1]+1)])
        elif s == 'v':
            q.append([((n[0][0][0]+1,n[0][0][1]),n[0][1]+1)])
        v.append((n[0][0][0],n[0][0][1]))
        
    else:
        a = (adj.ac(ll,n[0][0][0],n[0][0][1],'#',True))    
        av = [i[1] for i in a if i[1] not in v and i[0] == '.']
        for i in range(len(a)):
            if sl[i] == a[i][0]:
                av += [a[i][1]]
            
        if len(av) == 1:
            q.append([(i[1],n[0][1]+1) for i in a if i[1] == av[0] and i[1] not in v])
        elif len(av) == 0:
            None
        else:
            for i in a:
                if i[1] in av and i[1] not in v:
                    if n[0][0] not in v:
                        v.append(n[0][0])
                        k = False
                    q.append([(i[1],n[0][1]+1,v.copy())])
        if k:
            v.append(n[0][0])
            
q = [[((0,st),0)]]
v = []

while q:
    s = q[-1]
    q.pop(-1)
    ch(s) if s != [] else None

print(max(ans))
print(time.time()-ti)






def bfs(n):
    global v
    o = n[0][2]
    a = (adj.ac(ll,n[0][0][0],n[0][0][1],'#',True))    
    av = [i[1] for i in a if i[1] not in v and i[0] == '.']
    if len(n[0]) == 4:
        v = [n[0][2]]
    if len(av) ==1:
        q.append([(i,n[0][1]+1,o,True) for i in av if i not in v])
    elif n[0][0] == o:
        for x in av:
            if x not in v:
                q.append([(x,n[0][1]+1,o,True)])
    else:
        ins[n[0][0]][o] = n[0][1]+1
    v.append(n[0][0])

ans = 0

for l in range(len(ll)):
    ll[l] = ll[l].replace('<','.').replace('>','.').replace('v','.')

i = [(0,st),(len(ll)-1,e)]
for l in range(len(ll)):
    for c in range(len(ll[0])):
        if adj.ac(ll,l,c,'#').count('.')>2 and ll[l][c] == '.':
            i.append((l,c))
ins = {n:{} for n in i}

for inr in i:   
    q = [[(inr,0,inr)]]
    v = []
    while q:
        s = q[-1]
        q.pop(-1)
        bfs(s) if s != [] else None

def nbfs(n):
    global ans
    if n[0][0] == (len(ll)-1,e):
        if (n[0][1]+1-len(n[0][2])) > ans:
            ans = (n[0][1]+1-len(n[0][2]))
            print(ans)
    else:
        a = [i for i in ins[n[0][0]] if i not in n[0][2]]
        for s in a:
            if [(s,n[0][1]+ins[n[0][0]][s],n[0][2]+[n[0][0]])] not in q:
                q.append([(s,n[0][1]+ins[n[0][0]][s],n[0][2]+[n[0][0]])])

q = [[((0,st),0,[(0,st)])]]
while q:
    s = q[-1]
    q.pop(-1)
    nbfs(s)

print(ans)
print(time.time()-ti)

