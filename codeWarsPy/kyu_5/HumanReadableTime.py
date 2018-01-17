import math


def make_readable(seconds):
    ss = int(seconds % 60)
    mm = int(math.floor(seconds / 60))
    mm = int(mm % 60)
    hh = int(math.floor(seconds / 3600))

    return ':'.join([to_double_dig(str(hh)), to_double_dig(str(mm)), to_double_dig(str(ss))])


def to_double_dig(s):
    if len(s) < 2:
        s = '0' + s
    return s
