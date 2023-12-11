ne = []
def a(ll,x,y,d):
    global ne
    ne = []
    n = d+d
    for i in range(len(str(ll[0]))):
        n += d
    ne.append(n)
    for l in ll:
        ne.append(d+str(l)+d)
    ne.append(n)

    n = []
    for i in range(3):
        for j in range(3):
            if not(i==1 and j==1) and ne[i+x][j+y] != d:
                n.append(ne[i+x][j+y])
    return(n)

def ac(ll,x,y,d): #w,n,e,s
    global ne
    ne = []
    n = d+d
    for i in range(len(str(ll[0]))):
        n += d
    ne.append(n)
    for l in ll:
        ne.append(d+str(l)+d)
    ne.append(n)

    n = []
    if ne[x+1][y+0] != d:
        n.append(ne[x+1][y+0])
    else:
        n.append(d)
    if ne[x+0][y+1] != d:
        n.append(ne[x+0][y+1])
    else:
        n.append(d)
    if ne[x+1][y+2] != d:
        n.append(ne[x+1][y+2])
    else:
        n.append(d)
    if ne[x+2][y+1] != d:
        n.append(ne[x+2][y+1])
    else:
        n.append(d)
    return(n)
