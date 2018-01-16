def high_and_low(numbers):
    split = str.split(numbers)
    nums = [0 for x in range(len(split))]

    for i in range(len(nums)):
        nums[i] = int(split[i])

    return str(max(nums)) + " " + str(min(nums))


def high_and_low1(numbers):  # z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))
