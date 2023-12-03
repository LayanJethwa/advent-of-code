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
