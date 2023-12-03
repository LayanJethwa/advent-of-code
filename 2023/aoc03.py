ll = open("input.txt",'r').readlines()
c = ''
count = 0
ye = False
new = []
def adj(ll,x,y):
    global new
    ye = False
    new = []
    n = '..'
    for i in range(len(ll[0])):
        n += '.'
    new.append(n)
    for l in ll:
        new.append('.'+l+'.')
    new.append(n)
    for i in range(3):
        for j in range(3):
            if new[x+i][y+j] not in '1234567890.\n':
                ye = True
    return(ye)
for x in range(len(ll)):
    for y in range(len(ll[x])):
        if ll[x][y] in '1234567890':
            c += ll[x][y]
            if adj(ll,x,y):
                ye = True
        else:
            if ye:
                count += int(c)
            c = ''
            ye = False
print(count)

count = 0
c = ''
ye = 0
g = {}
curg = (0,0)

def adjg(ll,x,y):
    global new
    global curg
    ye = False
    new = []
    n = '..'
    for i in range(len(ll[0])):
        n += '.'
    new.append(n)
    for l in ll:
        new.append('.'+l+'.')
    new.append(n)
    for i in range(3):
        for j in range(3):
            if new[x+i][y+j] == '*':
                curg = ((x+i-1),(y+j-1))
                ye = True
    return(ye)

for x in range(len(ll)):
    for y in range(len(ll[x])):
        if ll[x][y] == '*':
            g[(x,y)] = [0,1]
            
for x in range(len(ll)):
    for y in range(len(ll[x])):
        if ll[x][y] in '1234567890':
            c += ll[x][y]
            if adjg(ll,x,y):
                ye = True
        else:
            if ye:
                g[curg][0] += 1
                g[curg][1] *= int(c)
            c = ''
            curg = (0,0)
            ye = False

for ge in g:
    if g[ge][0] == 2:
        count += g[ge][1]
        
print(count)
    
