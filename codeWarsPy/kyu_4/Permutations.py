import itertools


def permutations(string):
    s = itertools.permutations(string)

    a = []
    for ss in s:
        a.append(''.join(ss))
    return set(a)
