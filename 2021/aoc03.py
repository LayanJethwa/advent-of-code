input_text = open('input.txt', 'r')
lines = input_text.readlines()
common_list = [[],[],[],[],[],[],[],[],[],[],[],[]]

# Part 1

for line in lines:
    for i in range(12):
        common_list[i].append(int(line[i]))

def most_common(lst):
    return max(set(lst), key=lst.count)

gamma = ''
epsilon = ''
for i in range(12):
    gamma += str(most_common(common_list[i]))
    if str(most_common(common_list[i])) == '0':
        epsilon += '1'
    else:
        epsilon += '0'

print((int(('0b'+gamma),2))*(int(('0b'+epsilon),2)))


#Part 2

temp_list = []
new_list = []
for line in lines:
    temp_list.append(int(line[0]))
    for line in lines:
        if int(line[0]) == most_common(temp_list):
            new_list.append(int(line[1]))
