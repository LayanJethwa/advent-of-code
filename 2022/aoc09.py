input_text = open('input.txt', 'r')
lines = input_text.readlines()
coord_list = []
for i in range(10):
    coord_list.append((0,0))
tail_set = set()

def chase(a,b):
    global coord_list
    global tail_set
    if coord_list[a][0] > (coord_list[b][0]+1):
        if coord_list[a][1] > coord_list[b][1]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(1,1))))
        elif coord_list[a][1] < coord_list[b][1]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(1,-1))))
        elif coord_list[a][1] == coord_list[b][1]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(1,0))))
    elif coord_list[a][0] < coord_list[b][0]-1:
        if coord_list[a][1] > coord_list[b][1]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(-1,1))))
        elif coord_list[a][1] < coord_list[b][1]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(-1,-1))))
        elif coord_list[a][1] == coord_list[b][1]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(-1,0))))
    elif coord_list[a][1] > coord_list[b][1]+1:
        if coord_list[a][0] > coord_list[b][0]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(1,1))))
        elif coord_list[a][0] < coord_list[b][0]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(-1,1))))
        elif coord_list[a][0] == coord_list[b][0]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(0,1))))
    elif coord_list[a][1] < coord_list[b][1]-1:
        if coord_list[a][0] > coord_list[b][0]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(1,-1))))
        elif coord_list[a][0] < coord_list[b][0]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(-1,-1))))
        elif coord_list[a][0] == coord_list[b][0]:
            coord_list[b] = tuple(map(sum,zip(coord_list[b],(0,-1))))

    tail_set.add(coord_list[9])

#Part 1
for line in lines:
    for i in range(int((line.split(' '))[1].replace('\n',''))):
        if line.split(' ')[0] == 'L':
            coord_list[0] = tuple(map(sum,zip(coord_list[0],(-1,0))))
        elif line.split(' ')[0] == 'R':
            coord_list[0] = tuple(map(sum,zip(coord_list[0],(1,0))))
        elif line.split(' ')[0] == 'U':
            coord_list[0] = tuple(map(sum,zip(coord_list[0],(0,1))))
        elif line.split(' ')[0] == 'D':
            coord_list[0] = tuple(map(sum,zip(coord_list[0],(0,-1))))
        chase(0,9)
        
print(len(tail_set))


#Part 2
tail_set = set()
coord_list = []
for i in range(10):
    coord_list.append((0,0))
    
for line in lines:
    for i in range(int((line.split(' '))[1].replace('\n',''))):
        if line.split(' ')[0] == 'L':
            coord_list[0] = tuple(map(sum,zip(coord_list[0],(-1,0))))
        elif line.split(' ')[0] == 'R':
            coord_list[0] = tuple(map(sum,zip(coord_list[0],(1,0))))
        elif line.split(' ')[0] == 'U':
            coord_list[0] = tuple(map(sum,zip(coord_list[0],(0,1))))
        elif line.split(' ')[0] == 'D':
            coord_list[0] = tuple(map(sum,zip(coord_list[0],(0,-1))))
        chase(0,1)
        chase(1,2)
        chase(2,3)
        chase(3,4)
        chase(4,5)
        chase(5,6)
        chase(6,7)
        chase(7,8)
        chase(8,9)
        
print(len(tail_set))  

