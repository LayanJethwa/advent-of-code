import math
import adj
import re
ll = open("input.txt",'r').read().splitlines()
a = 0

for l in range(len(ll)):
    for i in range(len(ll[l])):
        if ll[l][i] == 'X':
            if len(ll)-1-l >=3:
                if ll[l+1][i] == 'M' and ll[l+2][i] == 'A' and ll[l+3][i] == 'S':
                    a += 1
            if l >= 3:
                if ll[l-1][i] == 'M' and ll[l-2][i] == 'A' and ll[l-3][i] == 'S':
                    a += 1

            if len(ll[l])-1-i >=3:
                if ll[l][i+1] == 'M' and ll[l][i+2] == 'A' and ll[l][i+3] == 'S':
                    a += 1

            if i >=3:
                if ll[l][i-1] == 'M' and ll[l][i-2] == 'A' and ll[l][i-3] == 'S':
                    a += 1

            if l >= 3 and len(ll[l])-1-i >=3:
                if ll[l-1][i+1] == 'M' and ll[l-2][i+2] == 'A' and ll[l-3][i+3] == 'S':
                    a += 1

            if l >= 3 and i >=3:
                if ll[l-1][i-1] == 'M' and ll[l-2][i-2] == 'A' and ll[l-3][i-3] == 'S':
                    a += 1
                
            if len(ll[l])-1-l >=3 and i >=3:
                if ll[l+1][i-1] == 'M' and ll[l+2][i-2] == 'A' and ll[l+3][i-3] == 'S':
                    a += 1

            if len(ll[l])-1-l >=3 and len(ll[l])-1-i >=3:
                if ll[l+1][i+1] == 'M' and ll[l+2][i+2] == 'A' and ll[l+3][i+3] == 'S':
                    a += 1

print(a)







a = 0

for l in range(len(ll)):
    for i in range(len(ll[l])):
        if ll[l][i] == 'A':
            if l >= 1 and i >= 1 and l <= len(ll)-2 and i <= len(ll[l])-2:
                d = 0
                if ll[l-1][i-1] == 'S' and not d:
                    if ll[l+1][i+1] == 'M':
                        if ll[l+1][i-1]+ll[l-1][i+1] in ['MS','SM']:
                            d = 1

                if ll[l+1][i+1] == 'S' and not d:
                    if ll[l-1][i-1] == 'M':
                        if ll[l+1][i-1]+ll[l-1][i+1] in ['MS','SM']:
                            d = 1

                if ll[l-1][i+1] == 'S' and not d:
                    if ll[l+1][i-1] == 'M':
                        if ll[l+1][i+1]+ll[l-1][i-1] in ['MS','SM']:
                            d = 1

                if ll[l+1][i-1] == 'S' and not d:
                    if ll[l-1][i+1] == 'M':
                        if ll[l+1][i+1]+ll[l-1][i-1] in ['MS','SM']:
                            d = 1

                if d:
                    a += 1

print(a)