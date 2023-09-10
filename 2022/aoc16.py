input_text = open('test.txt', 'r')
lines = input_text.readlines()
valves = {}
for line in lines:
    valve_name = (line.split(' has flow rate')[0].replace('Valve ',''))
    flow = int((line.split('flow rate=')[1].split(';'))[0])
    tunnel = (line.split('to ')[1].replace('\n','').replace('valves ','').replace('valve ','')).split(', ')
    valves[valve_name] = [flow,tunnel]

valves = dict(sorted(valves.items(), key=lambda item: item[1], reverse=True))
paths = {'AA':[0,[]]}

actual_path = ('AA.DD.DD.CC.BB.BB.AA.II.JJ.JJ.II.AA.DD.EE.FF.GG.HH.HH.GG.FF.EE.EE.DD.CC.CC').split('.')

for i in range(1,31):
    print(i)
    print(len(paths))
    print(list(paths.keys())[list(paths.values()).index((max(paths.values())))])
    print(paths[(list(paths.keys())[list(paths.values()).index((max(paths.values())))])])
    new_path = ''
    for x in range(0,i):
        new_path += actual_path[x]
        if x != i-1:
            new_path += '.'
    print(paths[new_path])
        
    print('\n')
    new_paths = {}
    for j in paths:
        count = 0
        max_value = 0
        flow = paths[j][0]
        opened = paths[j][1]
        for x in valves:
            if valves[x][0] != 0 and x not in opened:
                max_value += (30-(i+count))*valves[x][0]
            count += 2
        if (flow+max_value) >= (max(paths.values()))[0]:
            for k in valves[j.split('.')[-1]][1]:
                new_paths[j+'.'+k] = [flow,opened]
            if int(valves[j.split('.')[-1]][0])>0 and j.split('.')[-1] not in opened:
                temp_opened = []
                for z in opened:
                    temp_opened.append(z)
                temp_opened.append(j.split('.')[-1])
                new_paths[j+'.'+(j.split('.')[-1])] = [(int(flow) + (int(valves[j.split('.')[-1]][0])*(30-i))),temp_opened]

    paths = new_paths

print((max(paths.values()))[0])
            
#AA.DD.DD.CC.BB.BB.AA.II.JJ.JJ.II.AA.DD.EE.FF.GG.HH.HH.GG.FF.EE.EE.DD.CC.CC
    
