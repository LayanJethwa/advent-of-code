input_text = open('input.txt', 'r')
lines = input_text.readlines()
count = 0
temp_str = ''
temp_list = []
temp_num = 0
num = 1
up = 0
down = 0
left = 0
right = 0
score_list = []
for i in range(len(lines)):
    temp_str += '0'
lines.insert(0,temp_str)
lines.append(temp_str)
for i in range(len(lines)):
    lines[i] = '0'+lines[i]
    lines[i] = lines[i].replace('\n','')
    lines[i] += '0'

#Part 1
for i in range(len(lines)):
    for x in range(len(lines[i])):
        for a in range(i):
            temp_list.append(lines[a][x])
        if all(item < lines[i][x] for item in temp_list) or lines[i][x] == '0' and all(item == lines[i][x] for item in temp_list) and i == 1:
            temp_num += 1
            temp_list = []
        temp_list = []
        
        for a in range(i+1,len(lines)):
            temp_list.append(lines[a][x])
        if all(item < lines[i][x] for item in temp_list) or lines[i][x] == '0' and all(item == lines[i][x] for item in temp_list) and i == len(lines)-2:
            temp_num += 1
            temp_list = []
        temp_list = []
        
        for a in range(x):
            temp_list.append(lines[i][a])
        if all(item < lines[i][x] for item in temp_list) or lines[i][x] == '0' and all(item == lines[i][x] for item in temp_list) and x == 1:
            temp_num += 1
            temp_list = []
        temp_list = []
        
        for a in range(x+1,len(lines[i])):
            temp_list.append(lines[i][a])
        if all(item < lines[i][x] for item in temp_list) or lines[i][x] == '0' and all(item == lines[i][x] for item in temp_list) and x == len(lines[i])-2:
            temp_num += 1
            temp_list = []
        temp_list = []
        
        if temp_num > 0:
            count += 1
            temp_num = 0

count -= (2*len(lines[0]))+(((len(lines))-2)*2)
print(count)


#Part 2
for i in range(len(lines)):
    for x in range(len(lines[i])):
        while True:
            if i-num < 1:
                break
            elif lines[i-num][x] < lines[i][x] or lines[i-num][x] == lines[i][x] and lines[i][x] == 0 and i == 1:
                up += 1
                num += 1
            else:
                up += 1
                break
        num = 1
        
        while True:
            if i+num > len(lines)-2:
                break
            elif lines[i+num][x] < lines[i][x] or lines[i+num][x] == lines[i][x] and lines[i][x] == 0 and i == len(lines)-2:
                down += 1
                num += 1
            else:
                down += 1
                break
        num = 1

        while True:
            if x-num < 1:
                break
            elif lines[i][x-num] < lines[i][x] or lines[i][x-num] == lines[i][x] and lines[i][x] == 0 and x == 1:
                left += 1
                num += 1
            else:
                left += 1
                break
        num = 1

        while True:
            if x+num > len(lines[i])-2:
                break
            elif lines[i][x+num] < lines[i][x] or lines[i][x+num] == lines[i][x] and lines[i][x] == 0 and x == len(lines[i])-2:
                right += 1
                num += 1
            else:
                right += 1
                break
    
        score_list.append(up*down*left*right)
        up = 0
        down = 0
        left = 0
        right = 0

print(max(score_list))
                       
  
