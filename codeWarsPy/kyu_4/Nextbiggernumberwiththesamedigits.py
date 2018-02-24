# todo finish that

def next_bigger(n):
    if n < 12:
        return -1

    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):
        if int(s[i] < s[i + 1]):
            for ii in range(i, len(s)):
                if int(s[ii]) > int(s[i]):
                    buf = s[ii]
                    s[ii] = s[i]
                    s[i] = buf
                    return int(''.join(s))
    return -1


print(next_bigger(1234567890))
# 1234567890 -> 1234567908
