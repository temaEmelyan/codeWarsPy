def gap(g, m, n):
    if m % 2 == 0:
        m += 1
    current_indx = m

    while True:
        had_prime_in_the_gap = False
        if current_indx > n - g:
            return None

        while not is_prime(current_indx) & is_prime(current_indx + g):
            current_indx += 2

        for i in range(current_indx + 2, current_indx + g, 2):
            if is_prime(i):
                current_indx = current_indx + g
                had_prime_in_the_gap = True
                break
        if not had_prime_in_the_gap:
            return [current_indx, current_indx + g]


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
