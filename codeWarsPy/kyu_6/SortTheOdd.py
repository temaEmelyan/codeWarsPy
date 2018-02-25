def sort_array(source_array):
    if source_array is None or len(source_array) == 0:
        return source_array
    map_array = []
    odds = []
    for i in source_array:
        map_array.append(i % 2)
        if i % 2:
            odds.append(i)
    odds.sort()
    for i in range(len(source_array)):
        if map_array[i]:
            source_array[i] = odds.pop(0)
    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))
