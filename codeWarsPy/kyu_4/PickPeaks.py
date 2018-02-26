def add_pos_and_peak_to_dict(dic, pos, peak):
    dict.get(dic, 'pos').append(pos)
    dict.get(dic, 'peaks').append(peak)


def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    if len(arr) < 3:
        return result

    lft = 0
    mid = lft + 1
    rgh = mid + 1

    for i in range(len(arr) - 2):
        if (arr[mid] > arr[lft]) & (arr[mid] > arr[rgh]):
            add_pos_and_peak_to_dict(result, mid, arr[mid])
            lft = i + 1
            mid = lft + 1
            rgh = mid + 1
            continue

        if (arr[mid] > arr[lft]) & (arr[mid] == arr[rgh]):
            rgh += 1
            continue

        lft = i + 1
        mid = lft + 1
        rgh = mid + 1

    return result
