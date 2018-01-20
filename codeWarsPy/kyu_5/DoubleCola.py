import math


def whoIsNext(names, r):
    l = len(names)
    if r <= l:
        return names[r - 1]
    level = int(math.log2((r / l))) + 1
    levelStartsAt = 0
    for i in range(0, level):
        levelStartsAt += 2 ** i
    levelStartsAt *= l
    level_width = l * 2 ** level
    width = level_width / l
    position = math.ceil((r - levelStartsAt) / width)
    name_out = names[int(position - 1)]
    return name_out
