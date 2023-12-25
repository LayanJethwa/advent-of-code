import math
import adj
import sympy
ll = open("input.txt",'r').read().splitlines()
h = []
for l in ll:
    l = l.split(' @ ')
    p = [int(i) for i in l[0].split(', ')]
    v = [int(i) for i in l[1].split(', ')]
    m = v[1]/v[0]
    c = p[1]-(m*p[0])
    h.append([p,v,m,c])

a = 0
lb = 200000000000000
ub = 400000000000000
for s1 in h:
    for s2 in h:
        if s1[2] != s2[2]:
            x = (-s1[3]+s2[3])/(s1[2]-s2[2])
            y = (s1[2]*x)+s1[3]
            if x >= lb and x <= ub and y >= lb and y <= ub:
                if (s1[1][0] < 0 and x < s1[0][0]) or (s1[1][0] > 0 and x > s1[0][0]) or (s1[1][1] < 0 and y < s1[0][1]) or (s1[1][1] > 0 and y > s1[0][1]):
                    if (s2[1][0] < 0 and x < s2[0][0]) or (s2[1][0] > 0 and x > s2[0][0]) or (s2[1][1] < 0 and y < s2[0][1]) or (s2[1][1] > 0 and y > s2[0][1]):
                        a += 1
print(int(a/2))






x = sympy.symbols('x')
y = sympy.symbols('y')
z = sympy.symbols('z')
dx = sympy.symbols('dx')
dy = sympy.symbols('dy')
dz = sympy.symbols('dz')

cs = []
for i in range(3):
    [a,b,c,da,db,dc] = (h[i][0]+h[i][1])
    v1 = sympy.Matrix([x-a,y-b,z-c])
    v2 = sympy.Matrix([dx-da,dy-db,dz-dc])
    cs += ([i for i in v1.cross(v2)])
s = sympy.solve(cs,x,y,z,dx,dy,dz)
print(sum(s[0][0:3]))
