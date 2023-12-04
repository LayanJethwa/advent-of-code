import math
import adj
ll = open("input.txt",'r').read().splitlines()
ans = 0
for l in ll:
    count= 0
    l = l[9::]
    l = l.split(' | ')
    w = l[0].split(' ')
    n = l[1].split(' ')
    for nu in w:
        if nu in n and nu != '':
            count += 1
    if count > 0:
        ans += 2**(count-1)
print(ans)

ans = 0
wins = {}
copies = {}
num = 0
for l in ll:
    count= 0
    num += 1
    l = l[9::]
    l = l.split(' | ')
    w = l[0].split(' ')
    n = l[1].split(' ')
    for nu in w:
        if nu in n and nu != '':
            count += 1
    wins[num] = count
    copies[num] = 1

for i in wins:
    for a in range(wins[i]):
        for x in range(copies[i]):
            if i+a+1 <= len(wins):
                copies[i+a+1] += 1
                #wins[i+a+1] += wins[i+a+1]
    #print(i, copies)
        
print(sum(copies.values()))
