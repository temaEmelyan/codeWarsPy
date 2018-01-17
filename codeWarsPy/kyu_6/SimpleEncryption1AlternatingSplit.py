import math


def decrypt(text, n):
    for i in range(n):
        text = rypt(text)
    return text


def encrypt(text, n):
    for i in range(n):
        text = crypt(text)
    return text


def crypt(text):
    return text[1::2] + text[::2]


def rypt(text):
    str1 = text[:math.floor(len(text) / 2):]
    str2 = text[math.floor(len(text) / 2)::]

    strout = ''

    for i in range(max([len(str1), len(str2)])):
        try:
            strout += str2[i] + str1[i]
        except IndexError:
            strout += str2[i]

    return strout
