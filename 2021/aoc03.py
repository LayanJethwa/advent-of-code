input_text = open('input.txt', 'r')
lines = input_text.readlines()
linesnew = lines.copy()
common_list = [[],[],[],[],[],[],[],[],[],[],[],[]]

# Part 1
leng = 12

for line in lines:
    for i in range(leng):
        common_list[i].append(int(line[i]))

def most_common(lst):
    return max(set(lst), key=lst.count)

gamma = ''
epsilon = ''
for i in range(leng):
    gamma += str(most_common(common_list[i]))
    if str(most_common(common_list[i])) == '0':
        epsilon += '1'
    else:
        epsilon += '0'

print((int(('0b'+gamma),2))*(int(('0b'+epsilon),2)))


#Part 2
def o(l):
    if l.count('0') > l.count('1'):
        return '0'
    elif l.count('0') < l.count('1'):
        return '1'
    else:
        return '1'

def c(l):
    if l.count('0') < l.count('1'):
        return '0'
    elif l.count('0') > l.count('1'):
        return '1'
    else:
        return '0'
l = []
com = []
ans = 1
for i in range(leng):
    if len(lines)!=1:
        for line in lines:
            l.append(line[i])
        ox = o(l)
        new = lines.copy()
        for line in lines:
            if line[i] != ox:
                new.remove(line)
        com.append(ox)
        lines = new.copy()
        l = []
ans *= (int('0b'+''.join(lines),2))

l = []
com = []
lines = linesnew
for i in range(leng):
    if len(lines) != 1:
        for line in lines:
            l.append(line[i])
        ox = c(l)
        new = lines.copy()
        for line in lines:
            if line[i] != ox:
                new.remove(line)
        com.append(ox)
        lines = new.copy()
        l = []
ans *= (int('0b'+''.join(lines),2))
print(ans)
