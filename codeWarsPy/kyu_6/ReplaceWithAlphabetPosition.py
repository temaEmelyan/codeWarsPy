def alphabet_position(text):
    string = ''
    text = str.lower(text)
    for x in range(len(text)):
        if str.isalpha(text[x]):
            string += str(ord(text[x]) - ord('a') + 1) + ' '

    return string[0:len(string) - 1]


def alphabet_position1(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
