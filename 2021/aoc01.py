input_text = open('input.txt', 'r')
lines = input_text.readlines()
count = 0

# Part 1

for i in range(len(lines)):
    if i != 0:
        if int(lines[i]) > int(lines[i-1]):
            count += 1
print(count)


# Part 2

count = 0
for i in range(len(lines)):
    if i != 0 and i < len(lines)-2:
        if int(lines[i])+int(lines[i+1])+int(lines[i+2]) > int(lines[i-1])+int(lines[i])+int(lines[i+1]):
            count += 1
print(count)
    
