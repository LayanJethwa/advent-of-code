input_text = open('input.txt', 'r')
lines = input_text.readlines()
horizontal = 0
depth = 0

# Part 1

for line in lines:
    if 'forward' in line:
        horizontal += int(line.split('forward ')[1].strip())
    if 'down' in line:
        depth += int(line.split('down ')[1].strip())
    if 'up' in line:
        depth -= int(line.split('up ')[1].strip())

print(horizontal*depth)


# Part 2
horizontal = 0
depth = 0
aim = 0

for line in lines:
    if 'forward' in line:
        horizontal += int(line.split('forward ')[1].strip())
        depth += aim*int(line.split('forward ')[1].strip())
    if 'down' in line:
        aim += int(line.split('down ')[1].strip())
    if 'up' in line:
        aim -= int(line.split('up ')[1].strip())

print(horizontal*depth)
