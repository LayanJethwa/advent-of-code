input_text = open('input.txt', 'r')
lines = input_text.readlines()
dir_list = []
checked_list = []
done_list = []
total = 0
for i in range(len(lines)):
    if '$ ls' in lines[i]:
        current_dir = lines[i-1].split('cd ')[1].replace('\n','')
        if current_dir == '/':
            exec('uadir = []')
        else:
            exec('adir'+current_dir+' = []')
            dir_list.append(current_dir)
        for x in range(i+1,len(lines)):
            if '$' in lines[x]:
                break
        count = 1
        for y in range(x):
            try:
                if '$' in lines[i+count]:
                    break
            except:
                break
            if 'dir' in lines[i+count]:
                item = ((str(lines[i+count])).split('dir ')[1].replace('\n',''))
                if current_dir == '/':
                    exec('uadir.append(item)')
                else:
                    exec('adir'+current_dir+'.append(item)')
            elif any(char.isdigit() for char in lines[i+count]):
                item = ((str(lines[i+count])).split(' ')[0])
                if current_dir == '/':
                    exec('uadir.append(item)')
                else:
                    exec('adir'+current_dir+'.append(item)')
            count += 1

for i in dir_list:
    exec('ndir'+i+' = 0')
    for item in eval('adir'+i):
        if item.isdigit():
            exec('ndir'+i+' += int(item)')
    mynewlist = [s for s in (eval('adir'+i)) if s.isdigit()]
    if len(mynewlist) == len(eval('adir'+i)):
        done_list.append(i)

def evalu(a):
    global done_list
    num = eval('ndir'+a)
    lst = eval('adir'+a)
    exec('global num')
    exec('global lst')
    if a not in done_list:
        for x in (eval('adir'+a)):
            if not x.isdigit():
                if x not in done_list:
                    evalu(x)
                    evalu(a)
                else:
                    num = eval('ndir'+x)
                    lst = eval('adir'+x)
                    exec('global num')
                    exec('global lst')
                    exec('ndir'+a+' += '+'ndir'+x, globals())
                    done_list.append(a)

def check(a):
    global checked_list
    global dir_list
    global uadir
    for x in dir_list:
        exec('global ndir'+x)
        exec('global adir'+x)
    for x in (eval('adir'+a)):
        if not x.isdigit():
            check(x) 
            checked_list.append(x)
            checked_list.append(a) 
        for i in checked_list:
            evalu(i)
    
for i in dir_list:
    if i not in done_list:
        check(i)

for i in dir_list:
    if eval('ndir'+i) < 100001:
        total += eval('ndir'+i)

print(total)
