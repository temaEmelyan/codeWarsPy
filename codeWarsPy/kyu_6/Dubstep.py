def song_decoder(song):
    replace = str.replace(song, 'WUB', ' ')
    while 1:
        replace_new = replace.replace('  ', ' ')
        if replace_new == replace:
            break
        else:
            replace = replace_new

    l = list(replace)
    if l[0] == ' ':
        l.pop(0)
    if l[-1] == ' ':
        l.pop()

    return ''.join(l)


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
