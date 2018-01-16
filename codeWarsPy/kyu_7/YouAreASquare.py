import math


def is_square(n):
    if n < 0:
        return False
    return math.floor(math.sqrt(n)) == math.sqrt(n)
