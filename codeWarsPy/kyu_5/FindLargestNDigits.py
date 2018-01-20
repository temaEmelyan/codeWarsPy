def solution(digits):
    largest = 0
    for i in range(len(digits) - 4):
        if int(digits[i:i + 5:]) > largest:
            largest = int(digits[i:i + 5:])
    return largest
