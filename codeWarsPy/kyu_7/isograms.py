def is_isogram(string):
    a = [0 for x in range(26)]
    string = str.lower(string)
    for x in range(len(string)):
        a[ord(string[x]) - ord('a')] = a[ord(string[x]) - ord('a')] + 1
        if a[ord(string[x]) - ord('a')] > 1:
            return False
    return True


def is_isogram1(string):
    return len(string) == len(set(string.lower()))


def is_isogram2(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True


is_isogram3 = lambda s: len(set(s.lower())) == len(s)
