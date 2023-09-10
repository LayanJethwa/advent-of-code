input_text = open('input.txt', 'r')
lines = input_text.readlines()
graph = {}
temp = set()
start = 0
end = 0

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n','')
    for a in range(len(lines[i])):
        if lines[i][a] == 'E':
            end = (str(i)+'.'+str(a))
        elif lines[i][a] == 'S':
            start = (str(i)+'.'+str(a))
    lines[i] = lines[i].replace('E','z')
    lines[i] = lines[i].replace('S','a')
    
for i in range(len(lines)):
    for a in range(len(lines[i])):
        if a < (len(lines[i])-1):
            if ord(lines[i][a+1]) < ord(lines[i][a])+2:
                temp.add(str(i)+'.'+str(a+1))
        if a > 0:
            if ord(lines[i][a-1]) < ord(lines[i][a])+2:
                temp.add(str(i)+'.'+str(a-1))
        if i < (len(lines)-1):
            if ord(lines[i+1][a]) < ord(lines[i][a])+2:
                temp.add(str(i+1)+'.'+str(a))
        if i > 0:
            if ord(lines[i-1][a]) < ord(lines[i][a])+2:
                temp.add(str(i-1)+'.'+str(a))
        graph[(str(i)+'.'+str(a))] = temp
        temp = set()

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(next_node)
        path_index += 1
    return []

#Part 1
print((len(shortest_path(graph,start,end)))-1)


#Part 2
new_path_list = []
for i in range(len(lines)):
    for a in range(len(lines[i])):
        if lines[i][a] == 'a':
            num = (str(i)+'.'+str(a))
            path = (len(shortest_path(graph,num,end)))-1
            new_path_list.append(path)
path_set = set()
for i in new_path_list:
    path_set.add(i)
if -1 in path_set:
    path_set.remove(-1)
print(min(path_set))

