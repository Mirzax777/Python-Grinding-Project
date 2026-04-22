def find_max(numbers):
    if not numbers:
        return None
    maxim = numbers[0]
    for digit in numbers:
        if digit > maxim:
            maxim = digit
    return maxim


if __name__ == '__main__':
    numbers = [5, 3, 6, 7, 1]
    print(find_max(numbers))
