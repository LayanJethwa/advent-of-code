input_text = open('input.txt', 'r')
lines = input_text.readlines()
inv = []
op_list = []
test_list = []
inspect = []

for line in lines:
    if 'Starting items' in line:
        inv.append(line.split(' Starting items: ')[1].replace('\n','').split(', '))
    elif 'Operation' in line:
        op_list.append(line.split('  Operation: new = ')[1].replace('\n',''))
    elif 'Test' in line:
        temp = [line.split('  Test: divisible by ')[1].replace('\n',''),(lines[(lines.index(line))+1].split('If true: throw to monkey ')[1].replace('\n','')),(lines[(lines.index(line))+2].split('If false: throw to monkey ')[1].replace('\n',''))]
        test_list.append(temp)

for i in range(len(inv)):
    inspect.append(0)

# Part 1
for n in range(20):
    for i in range(len(inv)):
        for a in range(len(inv[i])):
            worry = int(inv[i][0])
            worry = eval(op_list[i].replace('old','worry'))
            worry = worry//3
            inv[i].remove(inv[i][0])
            if worry % int(test_list[i][0]) == 0:
                inv[int(test_list[i][1])].append(str(worry))
            else:
                inv[int(test_list[i][2])].append(str(worry))
            inspect[i] += 1
        
a = max(inspect)
inspect.remove(a)
b = max(inspect)
print(a*b)


#Part 2
inspect = []
inv = []
op_list = []
test_list = []
supermod = 1

for line in lines:
    if 'Starting items' in line:
        inv.append(line.split(' Starting items: ')[1].replace('\n','').split(', '))
    elif 'Operation' in line:
        op_list.append(line.split('  Operation: new = ')[1].replace('\n',''))
    elif 'Test' in line:
        temp = [line.split('  Test: divisible by ')[1].replace('\n',''),(lines[(lines.index(line))+1].split('If true: throw to monkey ')[1].replace('\n','')),(lines[(lines.index(line))+2].split('If false: throw to monkey ')[1].replace('\n',''))]
        test_list.append(temp)
        
for i in range(len(inv)):
    inspect.append(0)
for i in test_list:
    supermod *= int(i[0])
    
for n in range(10000):
    for i in range(len(inv)):
        for a in range(len(inv[i])):
            worry = int(inv[i][0])%supermod
            worry = eval(op_list[i].replace('old','worry'))
            inv[i].remove(inv[i][0])
            if worry % int(test_list[i][0]) == 0:
                inv[int(test_list[i][1])].append((worry))
            else:
                inv[int(test_list[i][2])].append((worry))
            inspect[i] += 1

a = max(inspect)
inspect.remove(a)
b = max(inspect)
print(a*b)

