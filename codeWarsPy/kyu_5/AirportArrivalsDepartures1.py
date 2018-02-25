def flap_display(lines, rotors):
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'

    result_array = []

    for i in range(len(lines)):
        acc = 0
        new_arr = []
        line = lines[i]
        rotor = rotors[i]
        for iii in range(len(rotor)):
            temp = rotor[iii]
            rotor[iii] = rotor[iii] + acc
            acc = acc + temp
        for ii in range(len(line)):
            letter = line[ii]
            pos = string.index(letter)
            new_pos = pos + rotor[ii]
            new_letter = string[new_pos % len(string)]
            new_arr.append(new_letter)
        new_str = ''.join(new_arr)
        result_array.append(new_str)
    return result_array


print(flap_display(["CAT", "CAT", "CAT", "CAT"], [[1, 13, 27], [1, 13, 27], [1, 13, 27], [1, 13, 27]]))
