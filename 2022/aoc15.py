import sys
input_text = open('input.txt', 'r')
lines = input_text.readlines()
row = 2000000
row_dict = {}

for i in range(-10000000,10000000):
    row_dict[i] = '.'

def manhattan(x1,y1,x2,y2):
    return((abs(x1-x2))+(abs(y1-y2)))

for line in lines:
    line = line.split('Sensor at ')[1]
    line = line.split(': closest beacon is at')[0]+line.split(': closest beacon is at')[1]
    line = line.replace('x=','')
    line = line.replace('y=','')
    line = line.replace(',','')
    line = line.replace('\n','')
    line = line.split(' ')
    dist = manhattan((int(line[0])),(int(line[1])),(int(line[2])),(int(line[3])))
    if (int(line[1])) > row and ((int(line[1]))-dist) <= row:
        extra = row - (int(line[1])-dist)
        for i in range(int(line[0])-extra,int(line[0])+extra):
            row_dict[i] = '#'
        if extra == 0:
            row_dict[int(line[0])] = '#'
    elif (int(line[1]) < row and int(line[1])+dist >= row):
        extra = (int(line[1])+dist) - row
        for i in range(int(line[0])-extra,int(line[0])+extra):
            row_dict[i] = '#'
        if extra == 0:
            row_dict[int(line[0])] = '#'

#Part 1
print(list(row_dict.values()).count('#'))


#Part 2
sensor_dict = {}
for line in lines:
    line = line.split('Sensor at ')[1]
    line = line.split(': closest beacon is at')[0]+line.split(': closest beacon is at')[1]
    line = line.replace('x=','')
    line = line.replace('y=','')
    line = line.replace(',','')
    line = line.replace('\n','')
    line = line.split(' ')
    dist = manhattan((int(line[0])),(int(line[1])),(int(line[2])),(int(line[3])))
    sensor_dict[line[0]+'.'+line[1]] = dist

limit = 4000000

for i in range(limit):
    if i%10000 == 0:
        print(i)
    range_list = []
    for j in sensor_dict:
        if abs(i-int(j.split('.')[1])) <= sensor_dict[j]:
            left = sensor_dict[j] - (abs(i-int(j.split('.')[1])))
            x = int(j.split('.')[0])
            if x-left >= 0 and x+left <= limit:
                range_list.append([x-left,x+left])
            elif x-left >= 0:
                range_list.append([x-left,limit])
            elif x+left <= limit:
                range_list.append([0,x+left])
            else:
                range_list.append([0,limit])

    range_list.sort()
    new_range = []
    new_range.append(range_list[0][0])
    new_range.append(range_list[0][1])
    range_list.pop(0)
    for a in range_list:
      if a[0] >= new_range[0] and a[0] <= new_range[1]+1:
        if a[1] > new_range[1]:
          new_range.append(new_range[0])
          new_range.append(a[1])
          new_range.pop(1)
          new_range.pop(0)
      else:
        print(((a[0]-1)*4000000)+i)
        sys.exit()

