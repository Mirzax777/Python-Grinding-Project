celsius = [0, 10, 20, 30, 40]


def to_fahrenheit(temp):
    return (temp * 9/5) + 32


if __name__ == '__main__':
    fahrenheit = list(map(to_fahrenheit, celsius))
    print(fahrenheit)
