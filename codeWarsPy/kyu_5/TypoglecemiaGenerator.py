def scramble_words(words):
    word_list = str.split(words)
    resul = []
    for word in word_list:
        chars = list(word)
        alpha_pos = []
        alphas = []

        pos_of_first_letter = -1
        for i in range(len(chars)):
            if chars[i].isalpha():
                pos_of_first_letter = i
                break

        pos_of_last_letter = -1
        for i in range(len(chars) - 1, 1, -1):
            if chars[i].isalpha():
                pos_of_last_letter = i
                break

        for i in range(pos_of_first_letter + 1, pos_of_last_letter):
            if chars[i].isalpha():
                alpha_pos.append(i)
                alphas.append(chars[i])

        alphas.sort(key=str.lower)
        for i in range(len(alpha_pos)):
            chars[alpha_pos[i]] = alphas[i]

        resul.append(''.join(chars))
    return ' '.join(resul)
