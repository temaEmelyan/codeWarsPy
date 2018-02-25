def thirt(n):
    seq = [1, 10, 9, 12, 3, 4]
    s = list(str(n))
    s.reverse()
    s = ''.join(s)

    prev = 0
    while 1:
        summ = 0
        for i in range(len(s)):
            summ += int(s[i]) * seq[i % len(seq)]
        if prev == summ:
            return summ
        else:
            prev = summ
            s = list(str(prev))
            s.reverse()
            s = ''.join(s)


assert thirt(1234567) == 87
assert thirt(8529) == 79
assert thirt(85299258) == 31
