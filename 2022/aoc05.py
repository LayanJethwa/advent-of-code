input_text = open('input.txt', 'r')
lines = input_text.readlines()
answer = ''

for line in lines:
    if line == '\n':
        break
    if '1' in line:
        num = int(line[-3])
        for i in range(num):
            exec('stack'+str(i)+' = []')

for line in lines:
    if '1' in line:
        stop = lines.index(line)
        break
    for i in range((len(line)+1)//4):
        if line[((i+1)*4)-3] != ' ':
            exec('stack'+str(i)+'.insert(0,(line[((i+1)*4)-3]))')
            
for i in range(stop+2, (len(lines))):
    line1 = lines[i].replace(' ','')
    line1 = line1.split("move")
    line1 = line1[1].split("from")
    line1 = [line1[0],line1[1].split("to")[0],line1[1].split("to")[1].split("\n")[0]]
    for i in range(int(line1[0])):
        exec('stack'+str(int(line1[2])-1)+'.append(stack'+str(int(line1[1])-1)+'[-'+str(int(line1[0])-i)+'])')
        exec('stack'+str(int(line1[1])-1)+'.pop(-'+str(int(line1[0])-i)+')')

for i in range(num):
    exec('answer+=(stack'+str(i)+'[-1])')

print(answer)
