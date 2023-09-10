input_text = open('input.txt', 'r')
lines = input_text.readlines()
cycle = 1
x = 1
strength_list = []

#Part 1
def check():
    global cycle
    global strength_list
    if cycle == 20:
        strength_list.append(20*x)
    elif cycle == 60:
        strength_list.append(60*x)
    elif cycle == 100:
        strength_list.append(100*x)
    elif cycle == 140:
        strength_list.append(140*x)
    elif cycle == 180:
        strength_list.append(180*x)
    elif cycle == 220:
        strength_list.append(220*(x))
        
for line in lines:
    line = line.replace('\n','')          
    if line == 'noop':
        cycle += 1
        check()
    else:
        cycle += 1
        check()
        x += int(line.split('addx ')[1])
        cycle += 1
        check()

print(sum(strength_list))


#Part 2
cycle = 1
x = 1
pos = 0
picture = ''
temp = 0
def picture_add():
    global cycle
    global picture
    global x
    global pos
    global temp
    if cycle == 41:
        picture += '\n'
        temp = 1
    elif cycle == 81:
        picture += '\n'
        temp = 2
    elif cycle == 121:
        picture += '\n'
        temp = 3
    elif cycle == 161:
        picture += '\n'
        temp = 4
    elif cycle == 201:
        picture += '\n'
        temp = 5
    pos = (cycle-1)-(40*temp)
        
    if pos == x or pos == x-1 or pos == x+1:
        picture += '#'
    else:
        picture += '.'

picture_add()
for line in lines:
    line = line.replace('\n','')          
    if line == 'noop':
        cycle += 1
        picture_add()
    else:
        cycle += 1
        picture_add()
        x += int(line.split('addx ')[1])
        cycle += 1
        picture_add()
print(picture)


