def palindrome_chain_length(n):
    counter = 0
    while not is_palyndrome(n):
        counter += 1
        n += int(str(n)[::-1])

    return counter


def is_palyndrome(numb):
    return numb == int(str(numb)[::-1])
