input_text = open('input.txt', 'r')
chars = input_text.read()
charlist = ''
for i in range(len(chars)-1):
    if i > 12:
        charlist = ''
        for x in range(14):
            if chars[i-14+x] not in charlist:
                charlist += chars[i-14+x]
        if len(charlist) == 14:
            print(i)
            break
