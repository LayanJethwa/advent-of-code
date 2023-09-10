done = False
in_order = False

def is_packet_pair_in_order(left, right, i=0, j=0):
    global done
    global in_order
    #print(f"- Compare {left} vs {right}")
    oleft = left
    oright = right
    while i < len(left) and j < len(right) and not done: # while both lists have elements
        if type(left[i]) == list and type(right[j]) != list: # if left list element is a list and right list element is not a list, convert the right list element to a list
            right[j:j+1] = [[right[j]]]
        elif type(left[i]) != list and type(right[j]) == list: # if left list element is not a list and right list element is a list, convert the left list element to a list
            left[i:i+1] = [[left[i]]]
        if type(left[i]) == list and type(right[j]) == list: # if both list elements are lists, recursively check if they are in order
            if is_packet_pair_in_order(left[i], right[j]) == 'same':
                is_packet_pair_in_order(left,right,i+1,j+1)
        else: # if both list elements are not lists
            if left[i] == right[j] and type(left[i]) == int and type(right[j]) == int:
                None
                #print(f"- Compare {left[i]} vs {right[j]}")
            elif left[i] < right[j]: # if the left list element is smaller than the right list element, inputs are in the right order
                #print(f"- Compare {left[i]} vs {right[j]}")
                #print("  Left side is smaller, so inputs are in the right order")
                done = True
                in_order = True
            elif right[j] < left[i]: # if the right list element is smaller than the left list element, inputs are not in the right order
                #print(f"- Compare {left[i]} vs {right[j]}")
                #print("  Right side is smaller, so inputs are not in the right order")
                done = True
                in_order = False
        i += 1 # increment left list index
        j += 1 # increment right list index
        left = oleft
        right = oright
    if done == False:
        if i == len(oleft) and j == len(oright): # if both lists have the same number of elements
            #print("  Inputs are in the right order")
            #done = True
            return 'same'
        elif i == len(oleft): # if left list ran out of elements first
            #print("  Left side ran out of items, so inputs are in the right order")
            done = True
            in_order = True
        elif j == len(oright): # if right list ran out of elements first
            #print("  Right side ran out of items, so inputs are not in the right order")
            done = True
            in_order = False

#Part 1

def main():
    global done
    global in_order
    packets = []
    output = 0
    # Read in packets from file
    with open("test.txt", "r") as f:
        for line in f:
            if line != '\n':
                packets.append(eval(line.strip()))
    
    # Pair up packets and check if they are in order
    for i in range(0, len(packets), 2):
        left = packets[i]
        right = packets[i+1]
        num = i//2 + 1
        #print(f"== Pair {num} ==")
        done = False
        in_order = False
        is_packet_pair_in_order(left, right)
        if in_order == True:
            output += num

    print(output)

main()

#Part 2

def sort():
    global done
    global in_order
    packets = []
    sorted_packets = []
    # Read in packets from file
    with open("input.txt", "r") as f:
        for line in f:
            if line != '\n':
                packets.append(eval(line.strip()))

    packets.append([[2]])
    packets.append([[6]])
    print(packets)

    for i in packets:
        index = 0
        done = False
        in_order = False
        finish = False
        if len(sorted_packets) == 0:
            sorted_packets.append(i)
        else:
            while not finish:
                left = i
                right = sorted_packets[index]
                in_order = False
                done = False
                is_packet_pair_in_order(left, right)
                if in_order:
                    sorted_packets.insert(index,i)
                    finish = True
                elif index == len(sorted_packets)-1:
                    sorted_packets.append(i)
                    finish = True
                else:
                    index += 1

    print(sorted_packets)
    print((sorted_packets.index([[[[2]]]])+1)*(sorted_packets.index([[[[6]]]])+1))


sort()
