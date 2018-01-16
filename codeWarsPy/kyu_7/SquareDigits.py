def square_digits(num):
    s = str(num)
    out = ''
    for i in range(len(s)):
        int1 = int(s[i])
        out += str(int1 * int1)
    return int(out)
