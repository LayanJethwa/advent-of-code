input_text = open('input.txt',)
ll = input_text.readlines()
for l in ll:
    for k in ll:
        if int(l)+int(k) == 2020:
            print(int(l)*int(k))

for l in ll:
    for k in ll:
        for j in ll:
            if int(l)+int(k)+int(j) == 2020:
                print(int(l)*int(k)*int(j))
