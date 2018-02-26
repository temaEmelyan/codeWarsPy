def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum([int(s) for s in str(n)]))


assert digital_root(942) == 6
