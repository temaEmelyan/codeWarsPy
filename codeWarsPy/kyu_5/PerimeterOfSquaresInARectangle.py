def perimeter(n):
    if n < 3:
        return n * 4

    a = 4
    b = 4

    summ = 8

    for i in range(n - 1):
        a_b = a + b
        summ += a_b
        a = b
        b = a_b

    return summ
