def rot13(message):
    out = ''
    for c in message:
        out += encodeLetter(c)
    return out


def encodeLetter(c):
    if str.isalpha(c):
        firstChar = 'a'
        if not str.islower(c):
            firstChar = 'A'
        dist = ord(c) - ord(firstChar)
        dist += 13
        dist %= 26
        return chr(ord(firstChar) + dist)
    else:
        return c
