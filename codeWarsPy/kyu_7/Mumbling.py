def accum(s):
    low = s.lower()
    l = list(low)

    resultList = []

    for i in range(len(l)):
        ll = []
        for ii in range(i + 1):
            if ii == 0:
                ll.append(str.upper(l[i]))
            else:
                ll.append(str.lower(l[i]))
        resultList.append(''.join(ll))
    join = '-'.join(resultList)
    return join


assert accum("ZpglnRxqenU") == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
