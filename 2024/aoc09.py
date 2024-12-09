import math
import g
import re
ll = open("input.txt",'r').read().splitlines()
a = 0

f = 0
s = ''
l = ll[0]
i = 0

for c in l:
    if not f:
        s += chr(i)*int(c)
        f = 1
        i += 1
    elif f:
        s += '田'*int(c)
        f = 0

while s[-1] == '田':
        s = s[0:-1]

while '田' in s:
    d = s.index('田')
    s = s[0:d]+s[-1]+s[d+1:-1]
    while s[-1] == '田':
        s = s[0:-1]

for i in range(len(s)):
    a += i*ord(s[i])

print(a)









a = 0

f = 0
s = ''
l = ll[0]
i = 0

for c in l:
    if not f:
        s += chr(i)*int(c)
        f = 1
        i += 1
    elif f:
        s += '田'*int(c)
        f = 0

i -= 1
while i >= 0:
    d = s.index(chr(i))
    e = (len(s)-''.join(list(reversed(s))).index(chr(i)))-1
    if '田'*((e-d)+1) in s[0:d]:
        b = s.index('田'*((e-d)+1))
        s = s[0:b]+s[d:e+1]+s[b+((e-d)+1):]
        s = s[0:d]+'田'*((e-d)+1)+s[e+1:]
    i -= 1
    print(i)

a = 0
for i in range(len(s)):
    if s[i] != '田':
        a += i*ord(s[i])

print(a)