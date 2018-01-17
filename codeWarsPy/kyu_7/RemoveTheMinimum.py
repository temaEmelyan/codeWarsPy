def remove_smallest(numbers):
    if numbers:
        list.remove(numbers, min(numbers))
    return numbers
