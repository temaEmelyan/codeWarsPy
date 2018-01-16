def namelist(names):
    length = len(names)

    if length == 0:
        return ''

    if length == 1:
        return names[0]['name']

    if length == 2:
        return names[0]['name'] + ' & ' + names[1]['name']

    str = ''

    for i in range(length - 2):
        str += names[i]['name'] + ', '
    str += names[length - 2]['name'] + ' & ' + names[length - 1]['name']
    return str
