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



c = 0
a = 0
na = []
for n in ns:
  if n[-1] == 'A':
    na.append(n)
while ([n[-1] for n in na]).count('Z') != len(na):
  ci = i[0][c]
  if ci == 'L':
    na = [ns[n][0] for n in na]
  else:
    na = [ns[n][1] for n in na]
  if c == len(i[0])-1:
    c = 0
  else:
    c += 1
  a += 1
  print(c,ci,na)
print(a)
