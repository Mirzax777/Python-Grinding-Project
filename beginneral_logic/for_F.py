def draw_pattern(numbers):
    for digit in numbers:
        output = ""
        for x_digit in range(digit):
            output += "x"
        print(output)


if __name__ == '__main__':
    numbers = [5, 2, 5, 2, 2]
    draw_pattern(numbers)
