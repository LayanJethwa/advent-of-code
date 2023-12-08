import math
ll = open("input.txt").read().replace(", ",",").splitlines()
ns = {}
for l in ll:
  l = l.split(" ")
  if len(l) == 1 and l != [""]:
    i = l
  elif len(l) == 3:
    n = l[0]
    no = l[2].replace("(","").replace(")","").split(",")
    ns[n]=no
n = 'AAA'
c = 0
a = 0
while n != 'ZZZ':
  ci = i[0][c]
  if ci == 'L':
    n = ns[n][0]
  else:
    n = ns[n][1]
  if c == len(i[0])-1:
    c = 0
  else:
    c += 1
  a += 1
print(a)



def gcd(a,b): 
  if a == 0: 
      return b 
  return gcd(b % a, a) 
  
def lcm(a,b): 
  return (a // gcd(a,b))* b 
  
a = []
na = []
for n in ns:
  if n[-1] == 'A':
    na.append(n)
for n in na:
  c = 0
  ac = 0
  while n[-1] != 'Z':
    ci = i[0][c]
    if ci == 'L':
      n = ns[n][0]
    else:
      n = ns[n][1]
    if c == len(i[0])-1:
      c = 0
    else:
      c += 1
    ac += 1
  a.append(ac)
for i in range(len(a)-1):
  a[0] =lcm(a[0],a[1])
  a.remove(a[1])
print(a[0])
