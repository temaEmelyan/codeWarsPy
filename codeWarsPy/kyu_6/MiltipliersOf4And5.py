def solution(number):
    return sum(firstn(number))


def firstn(n):
    num = 0
    while num < n - 1:
        num += 1
        if (num % 3 == 0) | (num % 5 == 0):
            yield num
    return


assert solution(10) == 23
