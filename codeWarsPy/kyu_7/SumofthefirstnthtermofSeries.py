def series_sum(n):
    if n == 0:
        return '0.00'
    sum = 0.0
    denom = 1

    for i in range(n):
        sum += 1 / denom
        denom += 3

    s = "{0:.2f}".format(sum)
    return s


assert series_sum(1) == '1.00'
assert series_sum(2) == '1.25'
assert series_sum(3) == '1.39'
