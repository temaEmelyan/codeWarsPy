def gap(g, m, n):
    d = [0 for x in range(n - m + 1)]
    for i in range(m, n + 1):
        d[i - m] = is_prime(i)

    current_indx = 0

    while True:
        try:
            while not d[current_indx] & d[current_indx + g]:
                current_indx += 1
            try:
                ind = d.index(True, current_indx + 1, current_indx + g)
                current_indx = ind
            except ValueError:
                return [current_indx + m, current_indx + m + g]
        except IndexError:
            return None


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True