text = open("input.txt",'r').readlines()
count = 0
for line in text:
    nums = ''
    for char in line:
        if char in '1234567890':
            nums += char
    if len(nums)>1:
        count += int(nums[0]+nums[-1])
    elif len(nums)==1:
        count += int(nums[0]+nums[0])
print(count)

count = 0
numwords3 = ['one','two','?','?','?','six']
numwords4 = ['four','five','?','?','?','nine']
numwords5 = ['three','?','?','?','seven','eight']
for line in text:
    nums = ''
    for pos in range(len(line)):
        if line[pos] in '1234567890':
            nums += line[pos]
        elif line[pos] in 'otfsen':
            for word in numwords3:
                if word in line[pos:pos+3]:
                    nums += str(numwords3.index(word)+1)
            for word in numwords4:
                if word in line[pos:pos+4]:
                    nums += str(numwords4.index(word)+4)
            for word in numwords5:
                if word in line[pos:pos+5]:
                    nums += str(numwords5.index(word)+3)
    if len(nums)>1:
        count += int(nums[0]+nums[-1])
    else:
        count += int(nums[0]+nums[0])
print(count)
