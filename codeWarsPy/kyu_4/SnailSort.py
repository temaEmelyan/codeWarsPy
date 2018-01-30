def snail(array):
    out = []
    try:
        while 1:
            list.extend(out, list.pop(array, 0)[::])
            array = rotate_counter_clockwise(array)
    except IndexError:
        return out


def rotate_counter_clockwise(array):
    array = list(map(list, list(zip(*array[::-1]))))
    array = list(map(list, list(zip(*array[::-1]))))
    array = list(map(list, list(zip(*array[::-1]))))
    return array


L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(snail(L))
