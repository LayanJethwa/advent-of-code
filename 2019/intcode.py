def run(program,input_vals=[0],pause_on_output=False,pointer=0,base=0,program_len=0,extra=0):
    output = []
    input_num = 0
    if program_len == 0:
        program_len = len(program)
    if len(program) == program_len:
        program += [0]*extra
    
    while program[pointer] != 99:
        modes = []
        pointer_mod = False

        for i in range(len(str(program[pointer]))-2):
            modes.append(str(program[pointer])[:-2][-(i+1)])
        opcode = int(str(program[pointer])[-2:])

        
        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            values,inputs = 4,2
            
        elif opcode == 3:
            values,inputs = 2,0
            
        elif opcode == 4:
            values,inputs = 2,1

        elif opcode == 5 or opcode == 6:
            values,inputs = 3,2

        elif opcode == 9:
            values, inputs = 2,1


        if opcode == 3:
            write = 1
        else:
            write = 3


        modes = [int(i) for i in modes]
        for i in range((values-1)-len(modes)):
            modes += [0]


        parameters = [0 for i in range(inputs)]
        for i in range(inputs):
            if modes[i] == 0:
                parameters[i] = program[program[pointer+(i+1)]]
            elif modes[i] == 1:
                parameters[i] = program[pointer+(i+1)]
            elif modes[i] == 2:
                parameters[i] = program[program[pointer+(i+1)]+base]


        if modes[-1] == 0:
            write_to = program[(pointer+write) % len(program)]
        elif modes[-1] == 2:
            write_to = program[pointer+write]+base

        if opcode == 1:
            program[write_to] = parameters[0]+parameters[1]
            
        elif opcode == 2:
            program[write_to] = parameters[0]*parameters[1]

        elif opcode == 3:
            program[write_to] = input_vals[input_num]
            input_num += 1
            input_num %= len(input_vals)

        elif opcode == 4:
            output.append(parameters[0])

        elif opcode == 5:
            if parameters[0] != 0:
                pointer = parameters[1]
                pointer_mod = True

        elif opcode == 6:
            if parameters[0] == 0:
                pointer = parameters[1]
                pointer_mod = True

        elif opcode == 7:
            if parameters[0] < parameters[1]:
                program[write_to] = 1
            else:
                program[write_to] = 0

        elif opcode == 8:
            if parameters[0] == parameters[1]:
                program[write_to] = 1
            else:
                program[write_to] = 0

        elif opcode == 9:
            base += parameters[0]


        if not pointer_mod:
            pointer += values
        pointer = pointer % program_len


        if pause_on_output and opcode == 4:
            return program.copy(), pointer, input_vals.copy(), output.copy(), base

    return program[0:program_len].copy(), output.copy()
