input_text = open('input.txt', 'r')
lines = input_text.readlines()
current_dir = ''
numvar = ''
numvar1 = 0
current_list = []
dir_list = {}
sorted_dir_list = {}
count_list = {}
total = 0
for i in range(len(lines)):
    if '$ cd ..' in lines[i]:
        while current_dir[-1] != '.':
            current_dir = current_dir[:-1]
        if current_dir[-1] == '.':
            current_dir = current_dir[:-1]
    elif '$ cd /' in lines[i]:
        current_dir = 'u'
    elif '$ cd' in lines[i]: 
        current_dir += '.'
        current_dir += lines[i].split('$ cd ')[1].replace('\n','')

    if '$ ls' in lines[i]:
        for x in range(i+1,len(lines)):
            if '$' in lines[x]:
                break
            elif 'dir' in lines[x]:
                current_list.append(lines[x].split('dir ')[1].replace('\n',''))
            elif lines[x][0].isdigit():
                for i in lines[x]:
                    if i.isdigit():
                        numvar += str(i)
                current_list.append(numvar)
                numvar = ''
        dir_list[current_dir] = current_list
        current_list = []

for i in dir_list:
    for x in dir_list[i]:
        if x.isdigit():
            numvar1 += int(x)
    count_list[i] = numvar1
    numvar1 = 0

for k in sorted(dir_list, key=len, reverse=True):
    sorted_dir_list[k] = dir_list[k]

for i in sorted_dir_list:
    for x in sorted_dir_list[i]:
        if not x.isdigit():
            count_list[i] += count_list[i+'.'+x]


#Part 1
for i in count_list:
    if count_list[i] <= 100000:
        total += count_list[i]

print(total)

#Part 2
free_space = 70000000 - count_list['u']
needed_space = 30000000 - free_space
space_dir_list = []

for i in count_list:
    if count_list[i] >= needed_space:
        space_dir_list.append(count_list[i])

print(min(space_dir_list))
        
