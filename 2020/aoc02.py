input_text = open('input.txt')
ll = input_text.readlines()
count = 0
for l in ll:
    l = l.split(' ')
    p = l[0]; pl = l[1][0:-1]; pas = l[2]
    p = p.split('-')
    if pas.count(pl) >= int(p[0]) and pas.count(pl) <= int(p[1]):
        count += 1
print(count)

count = 0
for l in ll:
    l = l.split(' ')
    p = l[0]; pl = l[1][0:-1]; pas = l[2]
    p = p.split('-')
    num = 0
    if pas[int(p[0])-1] == pl:
        num += 1
    if pas[int(p[1])-1] == pl:
        num += 1
    if num ==1:
        count += 1
print(count)
