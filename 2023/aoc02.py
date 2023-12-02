text = open("input.txt",'r').readlines()
count = 0
for line in text:
    r = b = g = 0
    rs = []
    bs = []
    gs = []
    cur = 0
    for block in line.strip().split(' '):
        if block[0:3] == 'red':
            r += cur
            cur = 0
        elif block[0:5] == 'green':
            g += cur
            cur = 0
        elif block[0:4] == 'blue':
            b += cur
            cur = 0
        if block[-1] in ';dne' and block[0] != 'G':
            rs.append(r)
            bs.append(b)
            gs.append(g)
            r = b = g = 0
        elif block[-1] not in ':;,dne':
            cur += int(block)
    if max(rs) < 13 and max(gs) < 14 and max(bs) < 15:
        count += int(line.strip().split(' ')[1][0:-1])
print(count)

count = 0
for line in text:
    r = b = g = 0
    rs = []
    bs = []
    gs = []
    cur = 0
    for block in line.strip().split(' '):
        if block[0:3] == 'red':
            r += cur
            cur = 0
        elif block[0:5] == 'green':
            g += cur
            cur = 0
        elif block[0:4] == 'blue':
            b += cur
            cur = 0
        if block[-1] in ';dne' and block[0] != 'G':
            rs.append(r)
            bs.append(b)
            gs.append(g)
            r = b = g = 0
        elif block[-1] not in ':;,dne':
            cur += int(block)
    count += max(rs)*max(bs)*max(gs)
print(count)
