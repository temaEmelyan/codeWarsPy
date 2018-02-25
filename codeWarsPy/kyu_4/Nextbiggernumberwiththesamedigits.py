def next_bigger(n):
    if n < 12:
        return -1
    s = [int(i) for i in list(str(n))]
    if sorted(s, reverse=True) == s:
        return -1

    for i in range(len(s) - 2, -1, -1):
        if int(s[i] < s[i + 1]):
            tail = s[i:]
            closest = 100
            min_diff = 100
            for ii in tail:
                i_ = s[i]
                if (ii - i_ < min_diff) & (ii > i_):
                    closest = ii
                    min_diff = ii - i_
            ind = tail.index(closest)
            closest = tail.pop(ind)
            s[i] = closest

            tail.sort()
            for ii in range(len(tail)):
                s[i + 1 + ii] = tail[ii]
            return int(''.join([str(lol) for lol in s]))
    return -1


print(next_bigger(543201))
print(next_bigger(59884848459853))
