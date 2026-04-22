def selection_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data


if __name__ == '__main__':
    data = [1, 5, 6, 3, 8, 4, 9]
    print(selection_sort(data))
