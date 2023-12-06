import math
ll = open("input.txt").read().splitlines()
for l in ll:
  l = l.split(" ")
  for i in range(l.count("")):
    l.remove("")
  if len(l[0]) == 5:
    t = l[1::]
  else:
    d = l[1::]
count = 1
for ti in range(len(t)):
  pr = (-int(t[ti]) + math.sqrt((int(t[ti])**2)-(4*int(d[ti]))))/-2
  nr = (-int(t[ti]) - math.sqrt((int(t[ti])**2)-(4*int(d[ti]))))/-2
  if max(pr,nr) % 1 == 0:
    if max(pr,nr) == pr:
      pr -= 1
    else:
      nr -= 1
  if min(pr,nr) % 1 == 0:
    if min(pr,nr) == pr:
      pr += 1
    else:
      nr += 1
  count *= ((math.floor(max(nr,pr)) - math.ceil(min(nr,pr)))+1)
print(count)

for l in ll:
  l = l.split(" ")
  for i in range(l.count("")):
    l.remove("")
  if len(l[0]) == 5:
    t = ''.join(l[1::])
  else:
    d = ''.join(l[1::])
count = 1
pr = (-int(t) + math.sqrt((int(t)**2)-(4*int(d))))/-2
nr = (-int(t) - math.sqrt((int(t)**2)-(4*int(d))))/-2
if max(pr,nr) % 1 == 0:
  if max(pr,nr) == pr:
    pr -= 1
  else:
    nr -= 1
if min(pr,nr) % 1 == 0:
  if min(pr,nr) == pr:
    pr += 1
  else:
    nr += 1
count *= ((math.floor(max(nr,pr)) - math.ceil(min(nr,pr)))+1)
print(count)
