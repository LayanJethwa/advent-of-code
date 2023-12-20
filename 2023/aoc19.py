import math
import adj
ll = open("input.txt",'r').read().splitlines()
r = False
w = {}
ra = ['x','m','a','s']
a = []
for l in ll:
    if l == '':
        r = True
    if not r:
        l = l.split('{')
        w[l[0]] = l[1][:-1].split(',')
    elif l != '':
        for i in '{}=xmas':
            l = l.replace(i,'')
        l = [int(i) for i in l.split(',')]
        ru = 0
        cw = 'in'
        d = False

        while not d:
            if '<' in w[cw][ru] or '>' in w[cw][ru]:
                i = '<' if '<' in w[cw][ru] else '>'
                re = w[cw][ru].split(':')[1]
                vs = w[cw][ru].split(':')[0].split(i)
                if eval(str(l[ra.index(vs[0])])+i+vs[1]):
                    if re in 'RA':
                        if re == 'A':
                            a+=(l)
                        d = True
                    else:
                        cw = re
                        ru = 0
                else:
                    ru += 1
                
            else:
                if w[cw][ru] in 'RA':
                    if w[cw][ru] == 'A':
                        a+=(l)
                    d = True
                else:
                    cw = w[cw][ru]
                    ru = 0
print(sum(a))        
            
            





ans = []
win = w['in']
out = 0

def ch(c,r):
    if r == 'A':
        ans.append(c)
    elif r!= 'R':
        for i in range(len(w[r])):
            nc = c.copy()
            ins = w[r][i].split(':')[0]
            nc.append(ins) if ('>' in ins or '<' in ins) else None
            globals().update(locals())
            nr = ins if len(w[r][i].split(':')) == 1 else w[r][i].split(':')[1]
            if i != 0:
                for j in range(1,i+1):
                    ru = w[r][i-j].split(':')[0].replace('<','#=').replace('>','@=').replace('#','>').replace('@','<')
                    nc.append(ru)
            ch(nc,nr)

for i in range(len(win)):
    nc = []
    ins = win[i].split(':')[0]
    nc.append(ins) if ('>' in ins or '<' in ins) else None
    nr = ins if len(win[i].split(':')) == 1 else win[i].split(':')[1]
    if i != 0:
        for j in range(1,i+1):
            ru = win[i-j].split(':')[0].replace('<','#=').replace('>','@=').replace('#','>').replace('@','<')
            nc.append(ru)
    ch(nc,nr)

for cs in ans:
    x=[1,4000]
    m=[1,4000]
    a=[1,4000]
    s=[1,4000]
    for c in cs:
        if '<=' in c:
            exec(c[0]+'[1] = min(int(c[c.index("=")+1:]),'+c[0]+'[1])')
        elif '>=' in c:
            exec(c[0]+'[0] = max(int(c[c.index("=")+1:]),'+c[0]+'[0])')
        elif '<' in c:
            exec(c[0]+'[1] = min(int(c[c.index("<")+1:])-1,'+c[0]+'[1])')
        elif '>' in c:
            exec(c[0]+'[0] = max(int(c[c.index(">")+1:])+1,'+c[0]+'[0])')
    out += math.prod([i[1]-i[0]+1 for i in [x,m,a,s]])
print(out)
