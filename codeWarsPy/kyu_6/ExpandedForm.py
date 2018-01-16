import math


def expanded_form(num):
    s = ''
    for i in range(int(math.floor(math.log(num, 10) + 1))):
        rem = num % 10
        if rem > 0:
            s += str(rem * 10 ** i)[::-1] + ' + '
        num = math.floor(num / 10)
    return s[len(s) - 4::-1]