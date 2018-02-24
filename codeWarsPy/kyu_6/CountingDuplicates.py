def duplicate_count(text):
    text = str.lower(text)
    counts = [0] * 26
    for s in text:
        counts[ord(s) - ord('a')] += 1
    answer = 0
    for i in counts:
        if i - 1 > 0:
            answer += 1
    return answer
