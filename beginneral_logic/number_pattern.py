def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    output = ""
    for i in range(1, n+1):
        output += str(i) + " "

    return output.strip()


if __name__ == '__main__':
    print(number_pattern(4))
    print(number_pattern(12))
