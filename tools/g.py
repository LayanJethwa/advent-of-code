import networkx as nx

def c(ll,x,y,d='.'): #check(grid,x,y,blocker)
    if x < 0 or y < 0:
        return d
    else:
        try:
            return ll[y][x]
        except:
            return d
        
def oa(x,y): #adjacent_coords(x,y)
    return [(x+1,y),(x,y-1),(x-1,y),(x,y+1)]

def oc(x,y): #adjacent_corners_coords(x,y)
    return [(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    
def a(ll,x,y,d='.'): #adjacent(grid,x,y,blocker)
    return [c(ll,x+1,y,d),c(ll,x,y-1,d),c(ll,x-1,y,d),c(ll,x,y+1,d)]

def ac(ll,x,y,d='.'): #adjacent_corners(grid,x,y,blocker)
    return [c(ll,x+1,y,d),c(ll,x+1,y-1,d),c(ll,x,y-1,d),c(ll,x-1,y-1,d),c(ll,x-1,y,d),c(ll,x-1,y+1,d),c(ll,x,y+1,d),c(ll,x+1,y+1,d)]

def l(ll,x,y,i,j,e,d='.'): #line(grid,x,y,dx,dy,length,blocker)
    t = []
    for a in range(e):
        t.append(c(ll,x+(a*i),y+(a*j),d))
    return t
    
def s(ll,c,d='.'): #search(grid,char)
    t = []
    for y in range(len(ll)):
        for x in range(len(ll[y])):
            if ll[y][x] == c:
                t += [(x,y)]
    return t

def ng(ll,p='.'): #networkxgraph(grid,path_char)
    g = nx.Graph()
    for y in range(len(ll)):
        for x in range(len(ll[y])):
            if ll[y][x] == p:
                g.add_node((x,y))
    
    for y in range(len(ll)):
        for x in range(len(ll[y])):
            for i,j in list(zip(a(ll,x,y,'?'),oa(x,y))):
                if i == p and (x,y) in g.nodes():
                    g.add_edge((x,y),j,weight=1)
    return g

def e(ll,x,y,c): #set(grid,x,y,char)
    ll[y] = ll[y][0:x]+str(c)+ll[y][x+1:]
    return ll